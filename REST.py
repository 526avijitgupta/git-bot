import subprocess

BASE_URL = "https://api.github.com"

def get_user_details(username):
    response = subprocess.check_output(('curl', '-u', username, BASE_URL))
    response = response.split('\n')
    return response
