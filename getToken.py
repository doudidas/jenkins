import requests
import urllib3
import json
import sys

# Get user arguments
fqdn = sys.argv[1]

# Set URL
url = "https://" + fqdn + "/identity/api/tokens"

# Get credentials from credentials.json
with open("credentials.json") as file:
    payload = json.load(file)

# Set header
headers = {"Accept": "application/json", "Content-Type": "application/json"}

#  disable certificate error: for dev only !
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Send request
response = requests.request("POST", url, data=json.dumps(
    payload), headers=headers, verify=False)

j = response.json()

if 'id' in j:
    print((j["id"]))
else:
    raise Exception(json.dumps(j, indent=3))
