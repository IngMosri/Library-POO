import json
filename = 'sing_user.json'
with open(filename, 'w') as f_obj:
    #diccionario que contiene todo
    user = {
        "full name":full_name,
        "Email address":email,
        "School Id": school_id
        }

    json.dump(user,f_obj, indent=4) #especificamos 4 espacios como la indentacion
    

