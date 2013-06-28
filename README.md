ScrumDo API Version 2
=====================


Authentication
--------------

We provide two methods of authenticating against the API.


## OAuth

If you're creating a web application that you will make available to others, authenticating via OAuth is the only allowed mechanism.  This allows users to authenticate wtihout giving out their username and password to third parties.  It also allows users to revoke access to applications.

To register a new OAuth consumer app, visit http://www.scrumdo.com/api/v2/oauth/apps

Users can manage the access of apps they've grated access to here: http://www.scrumdo.com/developer/user_keys

A Django based example showing how to authenticate can be found here:
https://github.com/ScrumDoLLC/ScrumDoAPIV2/tree/master/examples/django

You can see that app running here:
http://scrumdo-api-example.herokuapp.com/

## HTTP Basic
If you're creating a script that will **only be used personally or internally within your company**, you may use HTTP Basic authentication with your username and password to speed development.

A Python based example showing this can be found here:
https://github.com/ScrumDoLLC/ScrumDoAPIV2/tree/master/examples/python

## In Browser

For debugging purposes, if you make requests from your browser and are logged in, you session info will be carried over.  Example:
http://www.scrumdo.com/api/v2/organizations/

We do not respond with CORS headers, so this is not a good way to authenticate for any real use.


REST
----

Our calls generally follow RESTfull principles.

POST - Creates new items
PUT - Updates existing items
GET - Retrieves data
DELETE - Removes an item

JSON
----

All of our calls return results in JSON by default.  When expecting data (POST or PUT), you should JSON encode your data in the body of the request.

What's a SLUG?
--------------

Projects and organizations are identified by a slug, a short string consisting of alpha-numeric characters or dashes.  Most other objects are identified by a numeric id.  You can find out the slug of an organization by calling the getOrganizations call: https://www.scrumdo.com/api/v2/docs#!/organizations/getOrganizations_get


API Browser
-----------

You can browse all the available API calls in our interactive API Browser: https://www.scrumdo.com/api/v2/docs

If you are logged into ScrumDo, you will be able to actually execute API calls against your account via that page (ie. It's for real, be careful.) to see the inputs, URL's and outputs of each command.  Click the "Try it out" button under each call.

Some properties are read-only via the API.  When posting or putting data, please consult the body parameter of the API browser.  It lists all valid fields and gives examples for the format of the data expected.

![API Browser](https://raw.github.com/ScrumDoLLC/ScrumDoAPIV2/master/images/browser.png "API Browser")


Rate Throttling
---------------

GET requests - We allow up to 50 requests per 5 seconds.

POST or PUT requests - We allow up to 10 requests per 5 seconds.

Paged Results
-------------

In general, in order to make working with our API as easy as possible, we try to return all relevant data in a single call.  However, there are a few calls that may generate way too much information.  Those results will be paged.  The API Browser lists which calls will be paged in this way.

Support
-------

All calls have at least a minimal amount of documentation in the API browser.  If anything is unclear, please post a message in our support form.
http://support.scrumdo.com/discussions/api-access

Please note - We have a limited staff able to respond to API access requests, and there may occasionally be a delay in a response.


Contributions
-------------

Have an example in another language, find an error in this documentation?  We'd love to include it, feel free to send a pull request via GitHub our way.


Older versions of the API
-------------------------

Version 1 of our API should now be considered deprecated.  We will do our best to make sure it remains functional for at least the next 6 months (until 8/1/2013) but have no plans on maintaining it after that.  

Information on Version 1 of the API can be found here: http://www.scrumdo.com/developer/
