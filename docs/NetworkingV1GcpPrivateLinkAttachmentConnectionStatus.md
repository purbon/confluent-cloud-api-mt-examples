# NetworkingV1GcpPrivateLinkAttachmentConnectionStatus

Status of a GCP PrivateLink attachment connection for a zone.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | PrivateLinkAttachmentConnectionStatus kind. | 
**zone** | **str** | Zone associated with the GCP PrivateLink attachment connection. | [readonly] 
**private_service_connect_service_attachment** | **str** | GCP Private Service Connect ServiceAttachment for the zone. | [readonly] 
**private_service_connect_connection_id** | **str** | Id of the Private Service connection. | [readonly] 

## Example

```python
from openapi_client.models.networking_v1_gcp_private_link_attachment_connection_status import NetworkingV1GcpPrivateLinkAttachmentConnectionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1GcpPrivateLinkAttachmentConnectionStatus from a JSON string
networking_v1_gcp_private_link_attachment_connection_status_instance = NetworkingV1GcpPrivateLinkAttachmentConnectionStatus.from_json(json)
# print the JSON string representation of the object
print NetworkingV1GcpPrivateLinkAttachmentConnectionStatus.to_json()

# convert the object into a dict
networking_v1_gcp_private_link_attachment_connection_status_dict = networking_v1_gcp_private_link_attachment_connection_status_instance.to_dict()
# create an instance of NetworkingV1GcpPrivateLinkAttachmentConnectionStatus from a dict
networking_v1_gcp_private_link_attachment_connection_status_form_dict = networking_v1_gcp_private_link_attachment_connection_status.from_dict(networking_v1_gcp_private_link_attachment_connection_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


