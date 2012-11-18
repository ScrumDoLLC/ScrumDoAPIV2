import slumber
from colorama import init, Fore, Back, Style
from time import sleep
import local_settings as settings

# We're using slumber (http://slumber.in/), a python library that makes RESTfull calls amazingly easy,  to access the API

def main():
	init()
	base_url = "%s/api/v2/" % settings.scrumdo_host
	api = slumber.API(base_url, auth=(settings.scrumdo_username, settings.scrumdo_password))

	read_examples(api)



def read_examples(api):
	organization_list = api.organizations.get()
	api_count = check_throttle(1)

	for organization in organization_list:
		print Fore.GREEN + "%s\t%s" % (organization["name"], organization["slug"])		

		project_list = api.organizations(organization["slug"]).projects.get()
		api_count = check_throttle(api_count)

		for project in project_list:
			print Fore.BLUE + "\t%s\t%s" % (project['name'],project['slug'])

			iteration_list = api.organizations(organization["slug"]).projects(project['slug']).iterations.get()
			api_count = check_throttle(api_count)

			for iteration in iteration_list:
				print Fore.YELLOW + "\t\t%s %s to %s" % (iteration['name'], iteration['start_date'], iteration['end_date'])

				story_list = api.organizations(organization["slug"]).projects(project['slug']).iterations(iteration['id']).stories.get()
				api_count = check_throttle(api_count)

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