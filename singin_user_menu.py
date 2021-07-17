import json

full_name = input("What is your name? ")
email = input("Whats your email address ")
school_id =(input("Enter your school ID "))


    
filename = 'sing_user.json'
with open(filename, 'w') as f_obj:
    #diccionario que contiene todo
    user = {
        "full name":full_name,
        "Email address":email,
        "School Id": school_id
        }

    json.dump(user,f_obj, indent=4) #especificamos 4 espacios como la indentacion
    

