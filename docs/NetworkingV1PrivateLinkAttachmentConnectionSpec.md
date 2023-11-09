# NetworkingV1PrivateLinkAttachmentConnectionSpec

The desired state of the Private Link Attachment Connection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the PrivateLink attachment connection. | [optional] 
**cloud** | [**NetworkingV1PrivateLinkAttachmentConnectionSpecCloud**](NetworkingV1PrivateLinkAttachmentConnectionSpecCloud.md) |  | [optional] 
**environment** | [**ObjectReference**](ObjectReference.md) |  | [optional] 
**private_link_attachment** | [**ObjectReference**](ObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_private_link_attachment_connection_spec import NetworkingV1PrivateLinkAttachmentConnectionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAttachmentConnectionSpec from a JSON string
networking_v1_private_link_attachment_connection_spec_instance = NetworkingV1PrivateLinkAttachmentConnectionSpec.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAttachmentConnectionSpec.to_json()

# convert the object into a dict
networking_v1_private_link_attachment_connection_spec_dict = networking_v1_private_link_attachment_connection_spec_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAttachmentConnectionSpec from a dict
networking_v1_private_link_attachment_connection_spec_form_dict = networking_v1_private_link_attachment_connection_spec.from_dict(networking_v1_private_link_attachment_connection_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


