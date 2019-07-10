import requests

url = "https://cava-n-80-154.eng.vmware.com/identity/api/tokens"

payload = "{\"username\":\"etopin@vsphere.local\",\"password\":\"VMware1!\",\"tenant\":\"vsphere.local\"}"
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)
j = response.json()
print(j["id"])