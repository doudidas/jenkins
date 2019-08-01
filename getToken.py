import requests
import urllib3
import json

url = "https://cava-n-80-154.eng.vmware.com/identity/api/tokens"

payload = {
    "username": "etopin@vsphere.local",
    "password": "VMware1!",
    "tenant": "vsphere.local"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

#  disable certificate error: for dev only !
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.request("POST", url, data=json.dumps(
    payload), headers=headers, verify=False)

j = response.json()

if 'id' in j :
    f = open(".tokenID", "w")
    f.write(j["id"])
    print((j["id"]))
else:
    raise Exception("FAILED: " + json.dumps(j))