ScrumDo API Version 2
=====================

Beta Status
===========

This version of the API is currently in Beta status, and is only available on the ScrumDo Beta server.  Make sure all references to URL's are to beta.scrumdo.com, and not www.scrumdo.com, no matter what this document says.  

Take Care: The beta server points to the live production database, so you'll be dealing with your live projects.


Repository Contents
===================

README.md - This document

examples/python - A basic command line example of using the API with Python and the Slumber library
examples/django - A basic django/python application showing how to connect to the API via openid



Authentication
==============

We provide two methods of authenticating against the API.


OpenID
------

If you're creating a web application that you will make available to others, authenticating via OpenID is the only allowed mechanism.  This allows users to authenticate wtihout giving out their username and password to third parties.  It also allows users to revoke access to applications.

HTTP Basic
----------
If you're creating a script that will only be used personally or internally within your company, you may use HTTP Basic authentication with your username and password to speed development.