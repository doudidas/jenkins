import requests
import urllib3
import json
import sys

# Get user arguments
fqdn      = sys.argv[1]
requestID = sys.argv[2]
token     = sys.argv[3]

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
    print((j["cafeResourceId"]))
else:
    raise Exception(json.dumps(j, indent=3))
