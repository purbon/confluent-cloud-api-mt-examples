# NetworkingV1NetworkLinkEndpointSpecUpdate

The desired state of the Network Link Endpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the network link endpoint | [optional] 
**description** | **str** | The description of the network link endpoint | [optional] 
**environment** | [**GlobalObjectReference**](GlobalObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_network_link_endpoint_spec_update import NetworkingV1NetworkLinkEndpointSpecUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkLinkEndpointSpecUpdate from a JSON string
networking_v1_network_link_endpoint_spec_update_instance = NetworkingV1NetworkLinkEndpointSpecUpdate.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkLinkEndpointSpecUpdate.to_json()

# convert the object into a dict
networking_v1_network_link_endpoint_spec_update_dict = networking_v1_network_link_endpoint_spec_update_instance.to_dict()
# create an instance of NetworkingV1NetworkLinkEndpointSpecUpdate from a dict
networking_v1_network_link_endpoint_spec_update_form_dict = networking_v1_network_link_endpoint_spec_update.from_dict(networking_v1_network_link_endpoint_spec_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


