import sys
import requests
import json
import urllib3

# Get user arguments
fqdn              = sys.argv[1]
pathToPayloadFile = sys.argv[2]
token             = sys.argv[3]

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

body = r.json()

if "id" in body:
    print(body["id"].strip())
else:
    raise Exception(json.dumps(body))