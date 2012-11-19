import slumber
from colorama import init, Fore, Back, Style
from time import sleep
import local_settings as settings
import json
# We're using slumber (http://slumber.in/), a python library that makes RESTfull calls amazingly easy,  to access the API

def main():
	init()
	base_url = "%s/api/v2/" % settings.scrumdo_host
	api = slumber.API(base_url, auth=(settings.scrumdo_username, settings.scrumdo_password))

	read_examples(api)
	
	if settings.write_example:
		write_examples(api)
	


def write_examples(api):
	try:
		# First, let's make sure we have a valid org / project, this call will return a 500
		original_project = api.organizations(settings.write_organization_slug).projects(settings.write_project_slug).get()
		print "Project info: %s" % json.dumps(original_project, sort_keys=True, indent=4) # slumber converts JSON to python dicts for us, but to print it pretty, out lets output json

		# Let's change the name / description of the project...
		api.organizations(settings.write_organization_slug).projects(settings.write_project_slug).put({'name':'API EXAMPLE NAME', 'description':'Here is the new desc'})

		# Now, lets set it back to the original values.
		api.organizations(settings.write_organization_slug).projects(settings.write_project_slug).put({'name':original_project['name'], 'description':original_project['description']})

		# Cache this for less wordy slumber API calls
		api_project = api.organizations(settings.write_organization_slug).projects(settings.write_project_slug)
		# Now, 
		#     api_project.iterations.get() 
		# is equivalent to
		#     api.organizations(settings.write_organization_slug).projects(settings.write_project_slug).iterations.get() 


		
		# Next, lets' create a new iteration.
		iteration = api_project.iterations.post({'name':'API Test Iteration', 'start_date':'2012-11-01', 'end_date':'2012-11-15'})
		# name is the only required field, so any of these would have worked too:
		# iteration = api_project.iterations.post({'name':'API Test iteration'})
		# iteration = api_project.iterations.post({'name':'API Test Iteration', 'start_date':None})
		# iteration = api_project.iterations.post({'name':'API Test Iteration','locked':False, 'include_in_velocity':False,'detail':''})
		
		# When creating an object, it's returned in the body, so you can access it
		iteration_id = iteration['id']
		print "Created iteration id: %d" % iteration_id

		# We could also retrieve it now.
		print json.dumps(api_project.iterations(iteration_id).get(), sort_keys=True, indent=4)

		# We could tell the user about it.
		print "Go here to see your iteration: %s%s" % (settings.scrumdo_host, iteration['url'] )
		
		# After we have an iteration, we could modify it.
		iteration['name'] = "Modified API iteration name"
		api_project.iterations(iteration_id).put( iteration )
		
		# Note: Not all fields are writable.  To make the read & write API's more compatible, we
		# ignore extra fields.  This has the benefit of allowing you to PUT back the result you get.
		# But it can lead to some confusion if you expected those fields to update.
		#
		# For example. doing this:
		#    iteration['id'] = 100
		#    api_project.iterations(iteration_id).put( iteration )
		# would do nothing.
		#
		# See the API browser for allowable fields to change.


		# Now, let's cache that iteration api piece.
		api_iteration = api_project.iterations(iteration_id)
		# Remember, now
		#   api_iteration.stories.get()
		# is equivalent to
		#   api.organizations(settings.write_organization_slug).projects(settings.write_project_slug).iterations(iteration_id).stories.get()

		# Set this to a comma separated list of usernames you'd like to assign the new story to.
		assignees = ""
		# assignees = "mhughes, ajay, mhughes109"

		# Create a new story
		story = api_iteration.stories.post(	{ "rank":1, "category":"", "detail":"Here is my story detail, in markdown format.", "status":10, 
											  "summary":"As a user...", "points":"20", "extra_1":"The first custom field", "extra_2":None, 
											  "extra_3":None,"epic_id":None,"assignees":assignees, "tags":"tag1, tag2"} )
		
		print json.dumps(story, indent=4, sort_keys=True)
		# Note: story['extra_1'] corresponds to your first custom field, extra_2 to the next...


		story['summary'] = 'Modified Story Summary.  \n\n# Markdown Formatted'
		api_iteration.stories( story['id'] ).put( story )
		

		# To delete a story...
		# api_iteration.stories( story['id'] ).delete()
		# You don't have to specify the iteration so this would work too:
		# api_project.stories( story['id'] ).delete()




	except slumber.exceptions.HttpServerError as e:
		print e
		print e.content


def read_examples(api):

	# Get all of our organizations and loop through them
	organization_list = api.organizations.get()
	api_count = check_throttle(1)

	for organization in organization_list:

		# Print out the name & slug of each organization (Fore.GREEN colors it...)
		print Fore.GREEN + "%s\t%s" % (organization["name"], organization["slug"])		

		# Get all of our projects in that organization and loop through them
		project_list = api.organizations(organization["slug"]).projects.get()
		api_count = check_throttle(api_count)

		for project in project_list:

			# Print out the project name and slug
			print Fore.BLUE + "\t%s\t%s" % (project['name'],project['slug'])

			# Get all the iterations...
			iteration_list = api.organizations(organization["slug"]).projects(project['slug']).iterations.get()
			api_count = check_throttle(api_count)

			for iteration in iteration_list:
				print Fore.YELLOW + "\t\t%s %s to %s" % (iteration['name'], iteration['start_date'], iteration['end_date'])

				# Get all the stories in the iteration
				story_list = api.organizations(organization["slug"]).projects(project['slug']).iterations(iteration['id']).stories.get()
				api_count = check_throttle(api_count)

				# Compute some summary data for each iteration and print it out
				points = 0
				completed_tasks = 0
				for story in story_list:
					completed_tasks += story['completed_task_count']
					points += story['points_value']

				print Fore.RESET + "\t\t\t%d Stories, %d Points, %d Completed tasks" % (len(story_list), points, completed_tasks)




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