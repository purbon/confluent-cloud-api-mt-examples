# NetworkingV1NetworkLinkServiceStatus

The status of the Network Link Service

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecycle phase of the network link service:  READY:  network link service is ready;  | [readonly] 
**error_code** | **str** | Error code if network link service is in a failed state. May be used for programmatic error checking.  | [optional] [readonly] 
**error_message** | **str** | Displayable error message if network link service is in a failed state | [optional] [readonly] 

## Example

```python
from openapi_client.models.networking_v1_network_link_service_status import NetworkingV1NetworkLinkServiceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkLinkServiceStatus from a JSON string
networking_v1_network_link_service_status_instance = NetworkingV1NetworkLinkServiceStatus.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkLinkServiceStatus.to_json()

# convert the object into a dict
networking_v1_network_link_service_status_dict = networking_v1_network_link_service_status_instance.to_dict()
# create an instance of NetworkingV1NetworkLinkServiceStatus from a dict
networking_v1_network_link_service_status_form_dict = networking_v1_network_link_service_status.from_dict(networking_v1_network_link_service_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


