ScrumDo API Version 2
=====================

Beta Status
-----------

This version of the API is currently in Beta status, and is only available on the ScrumDo Beta server.  Make sure all references to URL's are to beta.scrumdo.com, and not www.scrumdo.com, no matter what this document says.  

Take Care: The beta server points to the live production database, so you'll be dealing with your live projects.


Repository Contents
-------------------

README.md - This document

examples/python - A basic command line example of using the API with Python and the Slumber library
examples/django - A basic django/python application showing how to connect to the API via openid

Have an example in another language?  We'd love to include it, feel free to send a pull request via GitHub our way.


Authentication
--------------

We provide two methods of authenticating against the API.


## OAuth

If you're creating a web application that you will make available to others, authenticating via OAuth is the only allowed mechanism.  This allows users to authenticate wtihout giving out their username and password to third parties.  It also allows users to revoke access to applications.

To register a new OAuth consumer app, visit http://beta.scrumdo.com/api/v2/oauth/apps

Users can manage the access of apps they've grated access to here: http://beta.scrumdo.com/developer/user_keys

A Django based example showing how to authenticate can be found here:
https://github.com/ScrumDoLLC/ScrumDoAPIV2/tree/master/examples/django


## HTTP Basic
If you're creating a script that will **only be used personally or internally within your company**, you may use HTTP Basic authentication with your username and password to speed development.


REST
----

Our calls generally follow RESTfull principles.

POST - Creates new items
PUT - Updates existing items
GET - Retrieves data

JSON
----

All of our calls return results in JSON by default.  When expecting data, you should JSON encode your data in the body of the request.


API Browser
-----------

You can browse all the available API calls in our interactive API Browser: http://beta.scrumdo.com/api/v2/docs

If you are logged into ScrumDo, you will be able to actually execute API calls against your account via that page (ie. It's for real, be careful.) to see the inputs, URL's and outputs of each command.  Click the "Try it out" button under each call.


Support
-------

All calls have at least a minimal amount of documentation in the API browser.  If anything is unclear, please post a message in our support form.
http://support.scrumdo.com/discussions/api-access

Please note - We have a limited staff able to respond to API access requests, and there may occasionally be a delay in a response.

Rate Throttling
---------------

GET requests - We allow up to 25 requests per 5 seconds.
POST or PUT requests - We allow up to 5 requests per 5 seconds.

Paged Results
-------------

In general, in order to make working with our API as easy as possible, we try to return all relevant data in a single call.  However, there are a few calls that may generate way too much information.  Those results will be paged.  The API Browser lists which calls will be paged in this way.


Older versions of the API
-------------------------

Version 1 of our API should now be considered deprecated.  We will do our best to make sure it remains functional for at least the next 6 months (until 6/1/2013) but have no plans on maintaining it after that.  


