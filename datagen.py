import json

program = "jfll" #frc, ftc, fll, jfll

input_source = "raw_"+ program +"_dataset.json"
output_source = program + "_teams.json"

with open(input_source) as data_file:
	data = data_file.read()

data = json.loads(data)

i = 0
collection = {"teams":[]}
for tinfo in data['hits']['hits']:
	if len(str(tinfo["_source"]["team_number_yearly"])) > 5:
		pass
	else:
		thash = {}
		thash["program"] = tinfo["_source"]["program_code_display"]
		thash["number"] = tinfo["_source"]["team_number_yearly"]
		if "team_nickname" in tinfo["_source"]:
			thash["name"] = tinfo["_source"]["team_nickname"]
		else:
			thash["name"] = ""
		if "team_web_url" in tinfo["_source"].keys():
			thash["website"] = tinfo["_source"]["team_web_url"]
		else:
			thash["website"] = ""
		if "team_motto" in tinfo["_source"].keys():
			thash["motto"] = tinfo["_source"]["team_motto"]
		else:
			thash["motto"] = ""
		thash["rookieyear"] = tinfo["_source"]["team_rookieyear"]
		if "team_city" in tinfo["_source"].keys():
			thash["city"] = tinfo["_source"]["team_city"]
		else:
			thash["city"] = ""
		thash["state_or_providence"] = tinfo["_source"]["team_stateprov"]
		thash["country"] = tinfo["_source"]["team_country"]
		collection["teams"].append(thash)
	print("got it %s", i)
	i+=1

with open(output_source,'w') as teams_data:
	teams_data.write(json.dumps(collection))
