# NetworkingV1PrivateLinkAccessSpec

The desired state of the Private Link Access

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the PrivateLink access | [optional] 
**cloud** | [**NetworkingV1PrivateLinkAccessSpecCloud**](NetworkingV1PrivateLinkAccessSpecCloud.md) |  | [optional] 
**environment** | [**ObjectReference**](ObjectReference.md) |  | [optional] 
**network** | [**ObjectReference**](ObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_private_link_access_spec import NetworkingV1PrivateLinkAccessSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAccessSpec from a JSON string
networking_v1_private_link_access_spec_instance = NetworkingV1PrivateLinkAccessSpec.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAccessSpec.to_json()

# convert the object into a dict
networking_v1_private_link_access_spec_dict = networking_v1_private_link_access_spec_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAccessSpec from a dict
networking_v1_private_link_access_spec_form_dict = networking_v1_private_link_access_spec.from_dict(networking_v1_private_link_access_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


