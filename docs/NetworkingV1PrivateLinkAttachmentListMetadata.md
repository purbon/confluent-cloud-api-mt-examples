# NetworkingV1PrivateLinkAttachmentListMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **object** |  | [optional] 
**last** | **object** |  | [optional] 
**prev** | **object** |  | [optional] 
**next** | **object** |  | [optional] 
**total_size** | **int** | Number of records in the full result set. This response may be paginated and have a smaller number of records. | [optional] 

## Example

```python
from openapi_client.models.networking_v1_private_link_attachment_list_metadata import NetworkingV1PrivateLinkAttachmentListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAttachmentListMetadata from a JSON string
networking_v1_private_link_attachment_list_metadata_instance = NetworkingV1PrivateLinkAttachmentListMetadata.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAttachmentListMetadata.to_json()

# convert the object into a dict
networking_v1_private_link_attachment_list_metadata_dict = networking_v1_private_link_attachment_list_metadata_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAttachmentListMetadata from a dict
networking_v1_private_link_attachment_list_metadata_form_dict = networking_v1_private_link_attachment_list_metadata.from_dict(networking_v1_private_link_attachment_list_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


