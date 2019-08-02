import sys
import requests
import json
import urllib3

# Get token, catalogID and businessGroupID from arg
fqdn              = sys.argv[1]
pathToPayloadFile = sys.argv[2]

# Get request body from a JSON file
with open(pathToPayloadFile) as json_file:
    obj = json.load(json_file)
    businessGroupID = obj["businessGroupId"]
    catalogID = obj["catalogItemId"]
    payload = json.dumps(obj)



url = "https://" + fqdn + "/catalog-service/api/consumer/entitledCatalogItems/" + catalogID + "/requests"

querystring = {
    "businessGroupId": businessGroupID,
}

# Get Token
with open(".tmp/tokenID") as token_file:
    token = token_file.read()




headers = {
    "Accept"       : "application/json",
    "Authorization": "Bearer " + token,
    "Content-Type" : "application/json"
}

#  disable certificate error: for dev only !
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

r = requests.request("POST", url, data=payload, headers=headers, params=querystring, verify=False)

if "location" in r.headers:
    locationURL = r.headers["Location"]
    f = open(".tmp/location", "w")
    f.write(locationURL)
    print(locationURL)
else:
    body = r.json()
    raise Exception(json.dumps(body))
