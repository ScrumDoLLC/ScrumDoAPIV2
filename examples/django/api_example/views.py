from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.template import RequestContext
import oauth2 as oauth
import urlparse
import urllib
import slumber

import logging

logger = logging.getLogger(__name__)



request_token_url = "%s/api/v2/oauth/request_token/" % settings.SCRUMDO_HOSTNAME
access_token_url = "%s/api/v2/oauth/access_token/" % settings.SCRUMDO_HOSTNAME
authorize_url = "%s/api/v2/oauth/authorize/" % settings.SCRUMDO_HOSTNAME

callback_url = "%s/oauth_callback" % settings.HOSTNAME


# We'll return a homepage depending on whether or not the user is authenicated already
def home(request):    
    
    if request.session.get("access_token",False):
        try:    
            return authenticated_home(request)
        except:
            logger.warn("Could not use previous token.")

    return unauthenticated_home(request)



# Step 1 of the OAuth dance... 
# Here, we're generating the URL we should send the user to and displaying it to the user asking them
# to click on it.
# When they click on it, they'll be brought to the scrumdo server and can grant access.  After which, they 
# will be redirect back to callback_url, which maps to oauth_callback() below
def unauthenticated_home(request):
    consumer = oauth.Consumer(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    client = oauth.Client(consumer)
    resp, content = client.request(request_token_url, "POST", body=urllib.urlencode({'oauth_callback':callback_url}))

    if resp['status'] != '200':
        logger.error("Could not contact the scrumdo server to get our url.  Did you set up your CONSUMER_KEY/CONSUMER_SECRET ?")
        raise Exception("Invalid response %s." % resp['status'])

    request_token = dict(urlparse.parse_qsl(content))
    login_url = "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])

    request.session['oauth_token_secret'] = request_token['oauth_token_secret']

    return render_to_response("home_unauthenticated.html", {'SCRUMDO_LOGIN_URL':login_url}, context_instance = RequestContext(request) )

# Step 2, the user has now granted access and we got a one time use token back
# we need to turn that token in to get a permanent token.
# Then, we'll save that permanent token in the users session so we can use it again later.
# If you were making a normal DB backed app, you'd probably want to save it and associate 
# it with the user at this point.
# After that, we'll serve up authenticated_home() below
def oauth_callback(request):    
    oauth_verifier = request.GET.get("oauth_verifier")
    token = oauth.Token(request.GET.get('oauth_token'), request.session.get('oauth_token_secret') )    
    token.set_verifier(oauth_verifier)
    consumer = oauth.Consumer(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    client = oauth.Client(consumer, token)

    resp, content = client.request(access_token_url, "POST")
    logger.info("Received %s / %s from oauth request" % (resp, content) )    
    access_token = dict(urlparse.parse_qsl(content))
    request.session['access_token'] = access_token['oauth_token']
    logger.info("Set token to %s" % access_token['oauth_token'] )
    return authenticated_home(request)
    

# Now that we're authenticated, lets show the user a list of organization they are a member of.
def authenticated_home(request):
    try:
        access_token = request.session.get("access_token")        
        logger.info("Making request to %s with %s" % (("%s/api/v2/" % settings.SCRUMDO_HOSTNAME),access_token) )
        api = slumber.API("%s/api/v2/" % settings.SCRUMDO_HOSTNAME)
        organizations = api.organizations.get(access_token=access_token)
    except slumber.exceptions.HttpServerError as e:
        print e
        print e.content        
        return unauthenticated_home(request)
        

    return render_to_response("home_authenticated.html", {'organizations': organizations}, context_instance = RequestContext(request) )
    

# We could also show a list of projects.
def project_list(request, organization_slug):
    access_token = request.session.get("access_token")
    api = slumber.API("%s/api/v2/" % settings.SCRUMDO_HOSTNAME)
    projects = api.organizations(organization_slug).projects.get(access_token=access_token)
    return render_to_response("project_list.html", {'projects': projects}, context_instance = RequestContext(request) )

def logout(request):
    request.session.flush()
    return HttpResponseRedirect("/")
