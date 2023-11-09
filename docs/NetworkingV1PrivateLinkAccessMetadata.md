# NetworkingV1PrivateLinkAccessMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **object** |  | 
**resource_name** | **object** |  | [optional] 
**created_at** | **datetime** | The date and time at which this object was created. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**updated_at** | **datetime** | The date and time at which this object was last updated. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**deleted_at** | **datetime** | The date and time at which this object was (or will be) deleted. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 

## Example

```python
from openapi_client.models.networking_v1_private_link_access_metadata import NetworkingV1PrivateLinkAccessMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAccessMetadata from a JSON string
networking_v1_private_link_access_metadata_instance = NetworkingV1PrivateLinkAccessMetadata.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAccessMetadata.to_json()

# convert the object into a dict
networking_v1_private_link_access_metadata_dict = networking_v1_private_link_access_metadata_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAccessMetadata from a dict
networking_v1_private_link_access_metadata_form_dict = networking_v1_private_link_access_metadata.from_dict(networking_v1_private_link_access_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


