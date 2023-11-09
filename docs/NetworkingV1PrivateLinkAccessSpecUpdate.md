# NetworkingV1PrivateLinkAccessSpecUpdate

The desired state of the Private Link Access

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the PrivateLink access | [optional] 
**environment** | [**ObjectReference**](ObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_private_link_access_spec_update import NetworkingV1PrivateLinkAccessSpecUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAccessSpecUpdate from a JSON string
networking_v1_private_link_access_spec_update_instance = NetworkingV1PrivateLinkAccessSpecUpdate.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAccessSpecUpdate.to_json()

# convert the object into a dict
networking_v1_private_link_access_spec_update_dict = networking_v1_private_link_access_spec_update_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAccessSpecUpdate from a dict
networking_v1_private_link_access_spec_update_form_dict = networking_v1_private_link_access_spec_update.from_dict(networking_v1_private_link_access_spec_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


