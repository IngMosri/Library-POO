import json



# Opening JSON file
f = open('sing_user.json',)

# returns JSON object as
# a dictionary
sing_user = json.load(f)

# Iterating through the json
# list
for i in sing_user['full_name']:
	print(i)

# Closing file
f.close()
