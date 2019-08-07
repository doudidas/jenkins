import sys
import requests
import time
import json
import urllib3


# Get user arguments
fqdn      = sys.argv[2]
requestID = sys.argv[3]
token     = sys.argv[1]


locationURL = "https://" + fqdn + "/catalog-service/api/consumer/requests/" + requestID

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
    time.sleep(5)
if phase == "FAILED":
    raise Exception(body["requestCompletion"]["completionDetails"])

requestID = body["id"]
print(requestID)
