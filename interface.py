from REST import *
BASE_URL="https://api.github.com"
username=raw_input("enter the username")
details=get_user_details(username,BASE_URL)
print [x for x in details]
repo=raw_input()
collab=get_user_details(username,BASE_URL+"/repos/"+username+"/"+repo+"/collaborators")
print [x for x in collab]
