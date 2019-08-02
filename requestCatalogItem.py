import sys
import requests
import json
import urllib3

# Get user arguments
fqdn              = sys.argv[1]
pathToPayloadFile = sys.argv[2]

# Get Token from cache
with open(".tmp/tokenID") as token_file:
    token = token_file.read()

# Get request body from a JSON file
with open(pathToPayloadFile) as json_file:
    obj = json.load(json_file)
    payload = json.dumps(obj)


# Set URL
url = "https://" + fqdn + "/catalog-service/api/consumer/entitledCatalogItems/" + obj["catalogItemId"] + "/requests"

# Add Query 
querystring = {
    "businessGroupId": obj["businessGroupId"],
}

# Set Header
headers = {
    "Accept"       : "application/json",
    "Authorization": "Bearer " + token,
    "Content-Type" : "application/json"
}

#  disable certificate error: for dev only !
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Send request
r = requests.request("POST", url, data=payload, headers=headers, params=querystring, verify=False)

if "location" in r.headers:
    # Save location url into cache
    locationURL = r.headers["Location"]
    f = open(".tmp/location", "w")
    f.write(locationURL)
    print(locationURL)
else:
    body = r.json()
    raise Exception(json.dumps(body))
