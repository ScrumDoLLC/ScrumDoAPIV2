import slumber
from colorama import init, Fore, Back, Style
from time import sleep
import urllib2
import local_settings as settings
import json
import os
# We're using slumber (http://slumber.in/), a python library that makes RESTfull calls amazingly easy,  to access the API

def main():
	init()
	base_url = "%s/api/v2/" % settings.scrumdo_host
	api = slumber.API(base_url, auth=(settings.scrumdo_username, settings.scrumdo_password))

	for project in api.organizations(settings.organization_slug).projects.get():
		exportProject(project, api)

def exportProject(project, api):
	print "Exporting project {slug}".format(slug=project['slug'])
	ensure_dir('output/{slug}'.format(slug=project['slug']) )

	filename = 'output/{slug}/project.json'.format(slug=project['slug'])
	with open(filename, 'w') as output:
		output.write( json.dumps(project, indent=2) )

	for iteration in api.organizations(settings.organization_slug).projects(project['slug']).iterations.get():
		exportIteration(project, iteration, api)

def exportIteration(project, iteration, api):
	print "  Exporting iteration {id}".format(id=iteration['id'])	
	ensure_dir('output/{slug}/{id}'.format(slug=project['slug'], id=iteration['id']) )

	filename = 'output/{slug}/{id}/iteration.json'.format(slug=project['slug'], id=iteration['id'])
	with open(filename, 'w') as output:
		output.write( json.dumps(iteration, indent=2) )


	for story in api.organizations(settings.organization_slug).projects(project['slug']).iterations(iteration['id']).stories.get():
		exportStory(project, iteration, story, api)

def exportStory(project, iteration, story, api):
	comments = api.comments.story(story['id']).get()
	ensure_dir('output/{slug}/{id}/{number}'.format(slug=project['slug'], id=iteration['id'], number=story['number']))
	
	filename = 'output/{slug}/{id}/{number}/card.json'.format(slug=project['slug'], id=iteration['id'], number=story['number'])
	with open(filename, 'w') as output:
		output.write( json.dumps(story, indent=2) )

	if len(comments) > 0:
		filename = 'output/{slug}/{id}/{number}/comments.json'.format(slug=project['slug'], id=iteration['id'], number=story['number'])
		with open(filename, 'w') as output:
			output.write( json.dumps(comments, indent=2) )

	attachments = api.organizations(settings.organization_slug).projects(project['slug']).stories(story['id']).attachments.get()
	for attachment in attachments:
		df = urllib2.urlopen(attachment['url'])
		filename = u"output/{slug}/{id}/{number}/{filename}".format(slug=project['slug'], id=iteration['id'], number=story['number'], filename=attachment['filename'])
		output = open(filename,'wb')
		output.write(df.read())
		output.close()
		print filename



def ensure_dir(f):    
    if not os.path.exists(f):    	
        os.makedirs(f)


# Since we're iterating over your entire account in this example, there could be a lot of API calls.
# This function is a dumb way to make sure we don't go over the throttle limit.
def check_throttle(requests):	
	requests += 1
	if requests >= 49: 
		sleep(5) # Add in a delay when we get close the our max # of requests per 5 seconds.
		return 0
	return requests

if __name__ == "__main__":
    main()