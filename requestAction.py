import sys
import requests
import json
import urllib3

# Get user arguments
fqdn              = sys.argv[1]
resourceID        = sys.argv[2]
pathToPayloadFile = sys.argv[3]
token             = sys.argv[4]

# Get request body from a JSON file
with open(pathToPayloadFile) as json_file:
    obj = json.load(json_file)
    obj["resourceId"] = resourceID
    payload = json.dumps(obj)

# Set URL
url = "https://" + fqdn + "/catalog-service/api/consumer/resources/" + \
    resourceID + "/actions/" + obj["actionId"] + "/requests"

# Set Header
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
}

#  Disable certificate error: for dev only !
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Send request
r = requests.request("POST", url, data=payload, headers=headers, verify=False)

body = r.json()

if "id" in body:
    print(body["id"])
else:
    raise Exception(json.dumps(body))
