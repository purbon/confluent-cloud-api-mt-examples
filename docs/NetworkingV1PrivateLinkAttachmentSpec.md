# NetworkingV1PrivateLinkAttachmentSpec

The desired state of the Private Link Attachment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the PrivateLink attachment. | [optional] 
**cloud** | **str** | The cloud service provider that hosts the resources to access with the PrivateLink attachment.  | [optional] 
**region** | **str** | The cloud service provider region where the resources to be accessed using the PrivateLink attachment are located.  | [optional] 
**environment** | [**ObjectReference**](ObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_private_link_attachment_spec import NetworkingV1PrivateLinkAttachmentSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAttachmentSpec from a JSON string
networking_v1_private_link_attachment_spec_instance = NetworkingV1PrivateLinkAttachmentSpec.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAttachmentSpec.to_json()

# convert the object into a dict
networking_v1_private_link_attachment_spec_dict = networking_v1_private_link_attachment_spec_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAttachmentSpec from a dict
networking_v1_private_link_attachment_spec_form_dict = networking_v1_private_link_attachment_spec.from_dict(networking_v1_private_link_attachment_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


