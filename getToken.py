import requests
import urllib3
import json
import sys

fqdn = sys.argv[1]


url = "https://"+ fqdn + "/identity/api/tokens"

# Get credenrtials from credentials.json
with open("credentials.json") as file:
    payload = json.load(file)

# Set header
headers = { "Accept": "application/json", "Content-Type": "application/json"}

#  disable certificate error: for dev only !
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.request("POST", url, data=json.dumps(
    payload), headers=headers, verify=False)

j = response.json()

if 'id' in j :
    f = open(".tmp/tokenID", "w")
    f.write(j["id"])
    print((j["id"]))
else:
    raise Exception("\033[1;31;40m" + json.dumps(j))