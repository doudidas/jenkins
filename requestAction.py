import sys
import requests
import json
import urllib3

# Get user arguments
fqdn              = sys.argv[1]
pathToPayloadFile = sys.argv[2]

# Get resourceID from cache 
with open(".tmp/resourceID") as file:
    resourceID = file.read()

# Get Token from cache
with open(".tmp/tokenID") as file:
    token = file.read()

# Get request body from a JSON file
with open(pathToPayloadFile) as json_file:
    obj = json.load(json_file)
    obj["resourceId"] = resourceID
    payload = json.dumps(obj)

# Set URL
url = "https://" + fqdn + "/catalog-service/api/consumer/resources/" + resourceID + "/actions/" + obj["actionId"] + "/requests"

# Set Header
headers = {
    "Accept"       : "application/json",
    "Authorization": "Bearer " + token,
    "Content-Type" : "application/json"
}

#  Disable certificate error: for dev only !
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Send request
r = requests.request("POST", url, data=payload, headers=headers, verify=False)

if "location" in r.headers:
    # Save header into cache
    locationURL = r.headers["Location"]
    f = open(".tmp/location", "w")
    f.write(locationURL)
    print(locationURL)
else:
    body = r.json()
    raise Exception(json.dumps(body))
