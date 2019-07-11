import sys
import requests
import time

# Convert json to Python syntax
null = None
false = False
true = True

# Get token from arg
token = sys.argv[1]

url = "https://cava-n-80-154.eng.vmware.com/catalog-service/api/consumer/entitledCatalogItems/8b0c1cca-2678-470d-ab27-05f7c8a9fc21/requests"

querystring = {
    "businessGroupId": "b3a2dc51-5267-410c-87f3-ddfefc1645a7",
    "requestedFor": "api-user@vsphere.local"
}

payload = """{
    "type": "com.vmware.vcac.catalog.domain.request.CatalogItemProvisioningRequest",
    "catalogItemId": "8b0c1cca-2678-470d-ab27-05f7c8a9fc21",
    "requestedFor": "etopin@vsphere.local",
    "businessGroupId": "b3a2dc51-5267-410c-87f3-ddfefc1645a7",
    "description": null,
    "reasons": null,
    "data": {
        "_leaseDays": 1,
        "_number_of_instances": 1,
        "centos": {
            "componentTypeId": "com.vmware.csp.component.cafe.composition",
            "componentId": null,
            "classId": "Blueprint.Component.Declaration",
            "typeFilter": "Centos*centos",
            "data": {
                "_cluster": 1,
                "_hasChildren": false,
                "cpu": 1,
                "datacenter_location": null,
                "description": null,
                "disks": [
                    {
                        "componentTypeId": "com.vmware.csp.iaas.blueprint.service",
                        "componentId": null,
                        "classId": "Infrastructure.Compute.Machine.MachineDisk",
                        "typeFilter": null,
                        "data": {
                            "capacity": 1,
                            "custom_properties": null,
                            "id": 1561394194720,
                            "initial_location": "",
                            "is_clone": true,
                            "label": "Hard disk 1",
                            "storage_reservation_policy": "",
                            "userCreated": false,
                            "volumeId": 0
                        }
                    },
                    {
                        "componentTypeId": "com.vmware.csp.iaas.blueprint.service",
                        "componentId": null,
                        "classId": "Infrastructure.Compute.Machine.MachineDisk",
                        "typeFilter": null,
                        "data": {
                            "capacity": 10,
                            "id": 1561394057515,
                            "initial_location": "",
                            "is_clone": false,
                            "label": "",
                            "storage_reservation_policy": "",
                            "userCreated": true,
                            "volumeId": 1
                        }
                    }
                ],
                "display_location": false,
                "guest_customization_specification": null,
                "machine_prefix": null,
                "max_network_adapters": -1,
                "max_per_user": 0,
                "max_volumes": 60,
                "memory": 128,
                "nics": [
                    {
                        "componentTypeId": "com.vmware.csp.iaas.blueprint.service",
                        "componentId": null,
                        "classId": "Infrastructure.Compute.Machine.Nic",
                        "typeFilter": null,
                        "data": {
                            "address": "",
                            "assignment_type": "DHCP",
                            "id": 0,
                            "load_balancing": "",
                            "network": null,
                            "network_profile": null
                        }
                    }
                ],
                "os_arch": "x86_64",
                "os_distribution": null,
                "os_type": "Linux",
                "os_version": null,
                "ovfAuthNeeded": false,
                "ovf_proxy_endpoint": null,
                "ovf_url": null,
                "ovf_url_pwd": null,
                "ovf_url_username": null,
                "ovf_use_proxy": false,
                "property_groups": null,
                "reservation_policy": null,
                "security_groups": [],
                "security_tags": [],
                "snapshot_name": null,
                "source_machine_external_snapshot": null,
                "source_machine_vmsnapshot": null,
                "storage": 11
            }
        }
    }
}
"""

headers = {
    'Accept': "application/json",
    'Authorization': "Bearer " + token,
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.15.0",
    'Host': "cava-n-80-154.eng.vmware.com",
    'accept-encoding': "gzip, deflate",
    'content-length': "4125",
    'Connection': "keep-alive"
    }

r = requests.request("POST", url, data=payload, headers=headers, params=querystring, verify=False)

locationURL = r.headers['Location']

executionStatus = ""
while executionStatus != "STOPPED":
    r = requests.request("GET", locationURL, headers=headers, verify=False)
    body = r.json()
    executionStatus = body['executionStatus']
    phase = body["phase"]
    print(phase)
    time.sleep(2)

if phase == "FAILED":
    raise Exception('FAILED: ' + body['requestCompletion']['completionDetails'])

print(r.text)