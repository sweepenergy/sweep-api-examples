import json
import os
import requests

# Define JSONWebToken to authenticate with the service. Generate API Key Here => https://app.facility-ops.com/dashboard/profile/api-keys
sweep_api_auth_token = os.getenv('SWEEP_API_TOKEN_EXAMPLE') ## AUTH TOKEN PULLED FROM ENV. You can also hard code here for testing.

def getDirectory(directory_id):
    res = requests.get("https://api.sweepapi.com/directory/{}".format(directory_id),headers = {"Authorization": "Bearer {}".format(sweep_api_auth_token)})
    return res

def generateDirectory(directory_name,parent_directory):
    payload = {
    "name" : directory_name
    }
    res = requests.post("https://api.sweepapi.com/directory/{}".format(parent_directory), json=payload ,headers = {"Authorization": "Bearer {}".format(sweep_api_auth_token)})
    return res

if __name__ == '__main__':
    print("Create A Directory Inside the Home => /")
    result = generateDirectory("Building A","home") # Creates a directory within the 'Home' User Directory Named 'Building A'
    print(result.status_code) ### on success, JSON object returned with status code 200 and id key value to the newly created directory.
    print(result.json()) ### on success, JSON object returned with status code 200 and id key value to the newly created directory.
