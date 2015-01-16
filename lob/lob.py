import urllib, json
import collections
import sys

# gather filename
filename = sys.argv[1]


# read from the json file all the necessary information
with open(filename) as json_file:
    json_data = json.load(json_file)
    skills = json_data['skills']
    relocate = bool(json_data['relocate'])
    location = json_data['location'].lower()

# read from the angellist API and load into python object
# max results are only 50 at a time, so we'll grab the last 
# 5 pages and concatenate results
data = []

for page_number in range(1,5):
	url = "https://api.angel.co/1/jobs?page=%s" % str(page_number)
	response = urllib.urlopen(url);
	data = data + json.loads(response.read())['jobs']


jobs = []
tag_map = collections.defaultdict(lambda: 0)
skills_list = collections.defaultdict(list)

for index, job in enumerate(data):
	for tag in job['tags']:
		# using the key as the job id, increment a counter that records the # of 
		# matches between skills/tags
		if tag['name'] in skills:
			tag_map[job['id']] += 1
			skills_list[job['id']].append(tag['name'])

		# if the seeker is not willing to relocate, only add jobs that match location
		if tag['tag_type'] == 'LocationTag' and tag['name'] == location and not relocate:
			jobs.append(job)
		# else if willing to relocate, add the job
		elif(relocate and tag['tag_type'] == 'LocationTag'):
			jobs.append(job)



# sort the list of jobs by the number of matched skill occurrences
jobs = sorted(jobs, key=lambda job: tag_map[job['id']], reverse=True)

for index,top_job in enumerate(jobs[:10]):
	#print top_job
	print "----------------------------"
	print " Company Rank: %s" % str(index+1)
	print " Company Name: %s" % top_job['startup']['name']
	print "\n Relevant Job Opportunities:\n"
	print "Title: %s\n" % top_job['title']
	print "Matched Skills: \n"
	for i in skills_list[top_job['id']]:
		print "- %s" % i
	print "----------------------------\n\n\n "
