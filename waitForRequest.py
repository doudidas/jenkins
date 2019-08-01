import sys
import requests
import time
import json
import urllib3


# Get Token
with open(".tokenID") as file:
    token = file.read()
# Get location URL
with open(".location") as file:
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
    print("\033[1;33;40m")
    print(phase)
    print("\033[1;37;40m")
    time.sleep(5)

if phase == "FAILED":
    raise Exception("\033[1;31;40m" + body["requestCompletion"]["completionDetails"])
    
print(r.text)
