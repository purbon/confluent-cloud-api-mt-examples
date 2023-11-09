# NetworkingV1NetworkLinkEndpointSpec

The desired state of the Network Link Endpoint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the network link endpoint | [optional] 
**description** | **str** | The description of the network link endpoint | [optional] 
**environment** | [**GlobalObjectReference**](GlobalObjectReference.md) |  | [optional] 
**network** | [**EnvScopedObjectReference**](EnvScopedObjectReference.md) |  | [optional] 
**network_link_service** | [**EnvScopedObjectReference**](EnvScopedObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_network_link_endpoint_spec import NetworkingV1NetworkLinkEndpointSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkLinkEndpointSpec from a JSON string
networking_v1_network_link_endpoint_spec_instance = NetworkingV1NetworkLinkEndpointSpec.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkLinkEndpointSpec.to_json()

# convert the object into a dict
networking_v1_network_link_endpoint_spec_dict = networking_v1_network_link_endpoint_spec_instance.to_dict()
# create an instance of NetworkingV1NetworkLinkEndpointSpec from a dict
networking_v1_network_link_endpoint_spec_form_dict = networking_v1_network_link_endpoint_spec.from_dict(networking_v1_network_link_endpoint_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


