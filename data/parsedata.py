import csv
import json

jsonfile = open('topo_wi_modified_pnames.json', 'r')
results_data = json.load(jsonfile)
jsonfile.close()


running_total = 0
num_of_const = 0
for con in results_data['objects']['const_all']["geometries"]:
	if con["properties"]["vote_summary"]["winner"]["party"] == "Conservative" and con["properties"]["vote_summary"]['winner']["votes"] < 34805:
		high_score = 1
		second_place = {}
		for cand in con["properties"]["results"]:
			if cand["party"] != "Conservative" and cand['votes'] > high_score:
				second_place = cand
				high_score = cand['votes']
		con["properties"]["vote_summary"]['second']	= second_place
		if con["properties"]["vote_summary"]['second']['party'] != 'UKIP':
			running_total += high_score + 1
		num_of_const += 1	

print num_of_const
print running_total

print 3299537/float(30691680)
print 3299537/float(46420413)

# high_score = 1
# cand = {}
# for con in results_data['objects']['const_all']["geometries"]:
# 	if con["properties"]["vote_summary"]["winner"]["party"] == "Conservative" and con["properties"]["vote_summary"]["winner"]['votes'] > high_score and con["properties"]["vote_summary"]["winner"]['votes'] < 34805:
# 		high_score = con["properties"]["vote_summary"]["winner"]['votes']
# 		cand = con["properties"]["vote_summary"]["winner"]
# print cand


# jsonfile = open("ukresults_pretty.json", "w+")
# jsonfile.write(json.dumps(results_data, indent=3))
# jsonfile.close()	