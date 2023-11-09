# NetworkingV1NetworkLinkServiceAssociationSpec

The desired state of the Network Link Service Association

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the network link endpoint | [optional] [readonly] 
**description** | **str** | The description of the network link endpoint | [optional] [readonly] 
**network_link_endpoint** | **str** | ID of the Network link endpoint. | [optional] [readonly] 
**network_link_service** | [**EnvScopedObjectReference**](EnvScopedObjectReference.md) |  | [optional] 
**environment** | [**GlobalObjectReference**](GlobalObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_network_link_service_association_spec import NetworkingV1NetworkLinkServiceAssociationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkLinkServiceAssociationSpec from a JSON string
networking_v1_network_link_service_association_spec_instance = NetworkingV1NetworkLinkServiceAssociationSpec.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkLinkServiceAssociationSpec.to_json()

# convert the object into a dict
networking_v1_network_link_service_association_spec_dict = networking_v1_network_link_service_association_spec_instance.to_dict()
# create an instance of NetworkingV1NetworkLinkServiceAssociationSpec from a dict
networking_v1_network_link_service_association_spec_form_dict = networking_v1_network_link_service_association_spec.from_dict(networking_v1_network_link_service_association_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


