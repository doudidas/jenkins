import requests
import urllib3
import json
import sys

# Get user arguments
fqdn = sys.argv[1]

# Get previous requestID from cache
with open(".tmp/requestID") as file:
    requestID = file.read()

# Get Token from cache
with open(".tmp/tokenID") as token_file:
    token = token_file.read()

# Set url
url = "https://" + fqdn + "/composition-service/api/deploymentresources/requests/" + requestID

# Set header
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token
}

#  disable certificate error: for dev only !
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Send Request
response = requests.request("GET", url, headers=headers, verify=False)

j = response.json()

if 'cafeResourceId' in j:
    # Save resourceID into cache
    f = open(".tmp/resourceID", "w")
    f.write(j["cafeResourceId"])
    print((j["cafeResourceId"]))
else:
    raise Exception(json.dumps(j, indent=3))
