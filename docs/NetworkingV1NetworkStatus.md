# NetworkingV1NetworkStatus

The status of the Network

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecyle phase of the network:  PROVISIONING:  network provisioning is in progress;  READY:  network is ready;  FAILED: provisioning failed;  DEPROVISIONING: network deprovisioning is in progress;  | [readonly] 
**supported_connection_types** | **List[str]** | The connection types this network supports. | [readonly] 
**active_connection_types** | **List[str]** | The connection types requested for use with the network. | [readonly] 
**error_code** | **str** | Error code if network is in a failed state. May be used for programmatic error checking. | [optional] [readonly] 
**error_message** | **str** | Displayable error message if network is in a failed state | [optional] [readonly] 
**dns_domain** | **str** | The root DNS domain for the network if applicable. Present on networks that support PrivateLink. | [optional] [readonly] 
**zonal_subdomains** | **Dict[str, str]** | The DNS subdomain for each zone. Present on networks that support PrivateLink. Keys are zones and values are DNS domains.  | [optional] [readonly] 
**cloud** | [**NetworkingV1NetworkStatusCloud**](NetworkingV1NetworkStatusCloud.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_network_status import NetworkingV1NetworkStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkStatus from a JSON string
networking_v1_network_status_instance = NetworkingV1NetworkStatus.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkStatus.to_json()

# convert the object into a dict
networking_v1_network_status_dict = networking_v1_network_status_instance.to_dict()
# create an instance of NetworkingV1NetworkStatus from a dict
networking_v1_network_status_form_dict = networking_v1_network_status.from_dict(networking_v1_network_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


