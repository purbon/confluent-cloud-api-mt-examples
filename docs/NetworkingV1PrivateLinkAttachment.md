# NetworkingV1PrivateLinkAttachment

PrivateLink attachment objects represent reservations to establish PrivateLink connections to a cloud region in order to access resources that belong to a Confluent Cloud Environment. The API allows you to list, create, read update and delete your PrivateLink attachments.   ## The Private Link Attachments Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.PrivateLinkAttachment\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `private_link_attachments_per_environment` | Number of PrivateLink Attachments per environment |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**NetworkingV1PrivateLinkAttachmentMetadata**](NetworkingV1PrivateLinkAttachmentMetadata.md) |  | [optional] 
**spec** | [**NetworkingV1PrivateLinkAttachmentSpec**](NetworkingV1PrivateLinkAttachmentSpec.md) |  | [optional] 
**status** | [**NetworkingV1PrivateLinkAttachmentStatus**](NetworkingV1PrivateLinkAttachmentStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_private_link_attachment import NetworkingV1PrivateLinkAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAttachment from a JSON string
networking_v1_private_link_attachment_instance = NetworkingV1PrivateLinkAttachment.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAttachment.to_json()

# convert the object into a dict
networking_v1_private_link_attachment_dict = networking_v1_private_link_attachment_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAttachment from a dict
networking_v1_private_link_attachment_form_dict = networking_v1_private_link_attachment.from_dict(networking_v1_private_link_attachment_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


