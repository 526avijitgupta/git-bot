from REST import *

username=raw_input("enter the username")
l=get_user_details(username)
print [x for x in l]
