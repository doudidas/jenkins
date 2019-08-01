import sys
import requests
import time
import json
import urllib3

# Get token and location from arg
token = sys.argv[1]
locationURL = sys.argv[2]

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
    time.sleep(2)

if phase == "FAILED":
    raise Exception("FAILED: " + body["requestCompletion"]["completionDetails"])
    
print(r.text)
