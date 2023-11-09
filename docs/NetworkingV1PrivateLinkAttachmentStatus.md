# NetworkingV1PrivateLinkAttachmentStatus

The status of the Private Link Attachment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecycle phase of the PrivateLink attachment:    PROVISIONING: PrivateLink attachment provisioning is in progress;    WAITING_FOR_CONNECTIONS: PrivateLink attachment is waiting for connections;    READY: PrivateLink attachment is ready;    FAILED: PrivateLink attachment is in a failed state;    EXPIRED: PrivateLink attachment has timed out waiting for connections, can only be deleted;    DEPROVISIONING: PrivateLink attachment deprovisioning is in progress;  | [readonly] 
**error_code** | **str** | Error code if PrivateLink attachment is in a failed state. May be used for programmatic error checking. | [optional] [readonly] 
**error_message** | **str** | Displayable error message if PrivateLink attachment is in a failed state. | [optional] [readonly] 
**dns_domain** | **str** | The root DNS domain for the PrivateLink attachment. | [optional] [readonly] 
**cloud** | [**NetworkingV1PrivateLinkAttachmentStatusCloud**](NetworkingV1PrivateLinkAttachmentStatusCloud.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_private_link_attachment_status import NetworkingV1PrivateLinkAttachmentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAttachmentStatus from a JSON string
networking_v1_private_link_attachment_status_instance = NetworkingV1PrivateLinkAttachmentStatus.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAttachmentStatus.to_json()

# convert the object into a dict
networking_v1_private_link_attachment_status_dict = networking_v1_private_link_attachment_status_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAttachmentStatus from a dict
networking_v1_private_link_attachment_status_form_dict = networking_v1_private_link_attachment_status.from_dict(networking_v1_private_link_attachment_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


