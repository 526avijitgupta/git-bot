import subprocess

def get_user_details(username, url):
    response = subprocess.check_output(('curl', '-u', username, url))
    response = response.split('\n')
    return response
