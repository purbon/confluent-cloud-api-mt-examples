# NetworkingV1PrivateLinkAttachmentConnectionUpdate

PrivateLink attachment connection objects represent connections established to a cloud region in order to access resources that belong to a Confluent Cloud Environment. The API allows you to list, create, read update and delete your PrivateLink attachment connections.   ## The Private Link Attachment Connections Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.PrivateLinkAttachmentConnection\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**NetworkingV1PrivateLinkAttachmentConnectionMetadata**](NetworkingV1PrivateLinkAttachmentConnectionMetadata.md) |  | [optional] 
**spec** | [**NetworkingV1PrivateLinkAttachmentConnectionSpecUpdate**](NetworkingV1PrivateLinkAttachmentConnectionSpecUpdate.md) |  | [optional] 
**status** | [**NetworkingV1PrivateLinkAttachmentConnectionStatus**](NetworkingV1PrivateLinkAttachmentConnectionStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_private_link_attachment_connection_update import NetworkingV1PrivateLinkAttachmentConnectionUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAttachmentConnectionUpdate from a JSON string
networking_v1_private_link_attachment_connection_update_instance = NetworkingV1PrivateLinkAttachmentConnectionUpdate.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAttachmentConnectionUpdate.to_json()

# convert the object into a dict
networking_v1_private_link_attachment_connection_update_dict = networking_v1_private_link_attachment_connection_update_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAttachmentConnectionUpdate from a dict
networking_v1_private_link_attachment_connection_update_form_dict = networking_v1_private_link_attachment_connection_update.from_dict(networking_v1_private_link_attachment_connection_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


