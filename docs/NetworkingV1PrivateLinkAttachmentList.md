# NetworkingV1PrivateLinkAttachmentList

PrivateLink attachment objects represent reservations to establish PrivateLink connections to a cloud region in order to access resources that belong to a Confluent Cloud Environment. The API allows you to list, create, read update and delete your PrivateLink attachments.   ## The Private Link Attachments Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.PrivateLinkAttachment\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `private_link_attachments_per_environment` | Number of PrivateLink Attachments per environment |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**NetworkingV1PrivateLinkAttachmentListMetadata**](NetworkingV1PrivateLinkAttachmentListMetadata.md) |  | 
**data** | [**List[NetworkingV1PrivateLinkAttachmentListDataInner]**](NetworkingV1PrivateLinkAttachmentListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.networking_v1_private_link_attachment_list import NetworkingV1PrivateLinkAttachmentList

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAttachmentList from a JSON string
networking_v1_private_link_attachment_list_instance = NetworkingV1PrivateLinkAttachmentList.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAttachmentList.to_json()

# convert the object into a dict
networking_v1_private_link_attachment_list_dict = networking_v1_private_link_attachment_list_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAttachmentList from a dict
networking_v1_private_link_attachment_list_form_dict = networking_v1_private_link_attachment_list.from_dict(networking_v1_private_link_attachment_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


