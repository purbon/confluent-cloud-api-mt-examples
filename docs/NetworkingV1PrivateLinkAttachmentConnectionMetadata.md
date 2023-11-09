# NetworkingV1PrivateLinkAttachmentConnectionMetadata


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
from openapi_client.models.networking_v1_private_link_attachment_connection_metadata import NetworkingV1PrivateLinkAttachmentConnectionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAttachmentConnectionMetadata from a JSON string
networking_v1_private_link_attachment_connection_metadata_instance = NetworkingV1PrivateLinkAttachmentConnectionMetadata.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAttachmentConnectionMetadata.to_json()

# convert the object into a dict
networking_v1_private_link_attachment_connection_metadata_dict = networking_v1_private_link_attachment_connection_metadata_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAttachmentConnectionMetadata from a dict
networking_v1_private_link_attachment_connection_metadata_form_dict = networking_v1_private_link_attachment_connection_metadata.from_dict(networking_v1_private_link_attachment_connection_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


