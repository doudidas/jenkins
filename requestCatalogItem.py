import sys
import requests
import json
import urllib3

# Get token, catalogID and businessGroupID from arg
pathToPayloadFile = sys.argv[1]
catalogID         = sys.argv[2]
businessGroupID   = sys.argv[3]

url = "https://cava-n-80-154.eng.vmware.com/catalog-service/api/consumer/entitledCatalogItems/" + catalogID + "/requests"

querystring = {
    "businessGroupId": businessGroupID,
}

# Get Token
with open(".tokenID") as token_file:
    token = token_file.read()

# Get request body from a JSON file
with open(pathToPayloadFile) as json_file:
    obj = json.load(json_file)
    payload = json.dumps(obj)


headers = {
    "Accept"       : "application/json",
    "Authorization": "Bearer " + token,
    "Content-Type" : "application/json"
}

#  disable certificate error: for dev only !
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

r = requests.request("POST", url, data=payload, headers=headers, params=querystring, verify=False)

locationURL = r.headers["Location"]

f = open(".location", "w")
f.write(locationURL)
print(locationURL)