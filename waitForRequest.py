import sys
import requests
import time
import json
import urllib3


# Get Token
with open(".tmp/tokenID") as file:
    token = file.read()
# Get location URL
with open(".tmp/location") as file:
    locationURL = file.read()

headers = {
    "Accept"       : "application/json",
    "Authorization": "Bearer " + token,
    "Content-Type" : "application/json"
}

#  disable certificate error: for dev only !
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

executionStatus = ""
while executionStatus != "STOPPED":
    r = requests.request("GET", locationURL, headers=headers, verify=False)
    body = r.json()
    executionStatus = body["executionStatus"]
    phase = body["phase"]
    print(phase)
    time.sleep(5)

if phase == "FAILED":
    raise Exception(body["requestCompletion"]["completionDetails"])

f = open(".tmp/requestID", "w")
requestID = body["id"]
f.write(requestID)
output = json.dumps(body, indent=3)
print(output)
