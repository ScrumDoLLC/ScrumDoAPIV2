# Quick example to show how to create a story queue item.  This support is experimental and you should talk with us before
# trying to use it.

import slumber
import local_settings as settings
import json

def main():
	base_url = "%s/api/v3/" % settings.scrumdo_host
	api = slumber.API(base_url, auth=(settings.scrumdo_username, settings.scrumdo_password))
	story_queue_example(api)

def story_queue_example(api):
	try:
		# First, let's make sure we have a valid org / project, this call will return a 404 if not
		project = api.organizations(settings.organization_slug).projects(settings.project_slug).get()

		# Create a new story - ex. POST https://app.scrumdo.com/api/v3/organizations/myorganization/projects/myproject/storyqueue/
		story = api.organizations(settings.organization_slug).projects(settings.project_slug).storyqueue.post(
							{	'action': 'create',     # This is a hack since we were already using this API end point for other things
								'extra_slug': 'HUBOT',  # Use a constant to identify the source, < 25 chars, no spaces, symbols, etc
                        		'external_id': '', # Optional - an identifying ID of the original item
                        		'external_url': 'http://mychatserver.com/link/to/discussion', # A URL to the original item (it's where the user goes when clicking the github icon)
                        		'summary':'Here is my new story queue item',  # Required
                        		'detail':'This is the detail for this item',  # Optional
                        		'points': '10', # Optional, but if you fill it in, make sure to use a valid value for that project
                        		'extra_1': '', # Optional - Custom field #1
                        		'extra_2': '', # Optional - Custom field #2
                        		'extra_3': '' # Optional - Custom field #3
							} )

		print json.dumps(story, indent=4, sort_keys=True)

	except slumber.exceptions.HttpServerError as e:
		print e
		print e.content



if __name__ == "__main__":
    main()
