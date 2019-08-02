import requests
import urllib3
import json
import sys

fqdn = sys.argv[1]


# Get 
with open(".tmp/resourceID") as file:
    resourceID = file.read()

# Get Token
with open(".tmp/tokenID") as token_file:
    token = token_file.read()

url = "https://" + fqdn + "/catalog-service/api/consumer/resources/" + resourceID

# Set header
headers = { "Accept": "application/json", "Content-Type": "application/json",    "Authorization": "Bearer " + token}

#  disable certificate error: for dev only !
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.request("GET", url, headers=headers, verify=False)

j = response.json()

for element in j["operations"]:
    if element["bindingId"] == 'composition.resource.action.deployment.destroy':
        operationID = element["id"]
        f = open(".tmp/operationID", "w")
        f.write(element["id"])
        print((element["id"]))
        break