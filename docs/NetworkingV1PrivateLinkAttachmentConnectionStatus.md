# NetworkingV1PrivateLinkAttachmentConnectionStatus

The status of the Private Link Attachment Connection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecycle phase of the PrivateLink attachment:    PROVISIONING: PrivateLink attachment connection provisioning is in progress;    READY: PrivateLink attachment connection is ready;    FAILED: PrivateLink attachment connection is in a failed state;    DEPROVISIONING: PrivateLink attachment connection deprovisioning is in progress;  | [readonly] 
**error_code** | **str** | Error code if PrivateLink attachment connection is in a failed state. May be used for programmatic error checking. | [optional] [readonly] 
**error_message** | **str** | Displayable error message if PrivateLink attachment connection is in a failed state. | [optional] [readonly] 
**cloud** | [**NetworkingV1PrivateLinkAttachmentConnectionStatusCloud**](NetworkingV1PrivateLinkAttachmentConnectionStatusCloud.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_private_link_attachment_connection_status import NetworkingV1PrivateLinkAttachmentConnectionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAttachmentConnectionStatus from a JSON string
networking_v1_private_link_attachment_connection_status_instance = NetworkingV1PrivateLinkAttachmentConnectionStatus.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAttachmentConnectionStatus.to_json()

# convert the object into a dict
networking_v1_private_link_attachment_connection_status_dict = networking_v1_private_link_attachment_connection_status_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAttachmentConnectionStatus from a dict
networking_v1_private_link_attachment_connection_status_form_dict = networking_v1_private_link_attachment_connection_status.from_dict(networking_v1_private_link_attachment_connection_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


