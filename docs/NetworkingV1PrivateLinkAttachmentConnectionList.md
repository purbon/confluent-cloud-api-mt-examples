# NetworkingV1PrivateLinkAttachmentConnectionList

PrivateLink attachment connection objects represent connections established to a cloud region in order to access resources that belong to a Confluent Cloud Environment. The API allows you to list, create, read update and delete your PrivateLink attachment connections.   ## The Private Link Attachment Connections Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.PrivateLinkAttachmentConnection\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**NetworkingV1PrivateLinkAttachmentConnectionListMetadata**](NetworkingV1PrivateLinkAttachmentConnectionListMetadata.md) |  | 
**data** | [**List[NetworkingV1PrivateLinkAttachmentConnectionListDataInner]**](NetworkingV1PrivateLinkAttachmentConnectionListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.networking_v1_private_link_attachment_connection_list import NetworkingV1PrivateLinkAttachmentConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAttachmentConnectionList from a JSON string
networking_v1_private_link_attachment_connection_list_instance = NetworkingV1PrivateLinkAttachmentConnectionList.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAttachmentConnectionList.to_json()

# convert the object into a dict
networking_v1_private_link_attachment_connection_list_dict = networking_v1_private_link_attachment_connection_list_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAttachmentConnectionList from a dict
networking_v1_private_link_attachment_connection_list_form_dict = networking_v1_private_link_attachment_connection_list.from_dict(networking_v1_private_link_attachment_connection_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


