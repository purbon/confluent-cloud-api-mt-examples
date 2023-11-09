# NetworkingV1NetworkLinkServiceSpecUpdate

The desired state of the Network Link Service

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the network link service | [optional] 
**description** | **str** | The description of the network link service | [optional] 
**accept** | [**NetworkingV1NetworkLinkServiceAcceptPolicy**](NetworkingV1NetworkLinkServiceAcceptPolicy.md) |  | [optional] 
**environment** | [**GlobalObjectReference**](GlobalObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_network_link_service_spec_update import NetworkingV1NetworkLinkServiceSpecUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkLinkServiceSpecUpdate from a JSON string
networking_v1_network_link_service_spec_update_instance = NetworkingV1NetworkLinkServiceSpecUpdate.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkLinkServiceSpecUpdate.to_json()

# convert the object into a dict
networking_v1_network_link_service_spec_update_dict = networking_v1_network_link_service_spec_update_instance.to_dict()
# create an instance of NetworkingV1NetworkLinkServiceSpecUpdate from a dict
networking_v1_network_link_service_spec_update_form_dict = networking_v1_network_link_service_spec_update.from_dict(networking_v1_network_link_service_spec_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


