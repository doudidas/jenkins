import requests
import urllib3
import json

url = "https://us08-1-vralb.oc.vmware.com/identity/api/tokens"

payload = {
    "username": "etopin@vvmware.com",
    "password": "KpmgSYf45..#ET",
    "tenant": "Cava"
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

if hasattr(j, "id"):
    print(j["id"])
else:
    raise Exception("FAILED: " + json.dumps(j))
