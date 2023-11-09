# NetworkingV1GcpPrivateLinkAttachmentStatus

GCP PrivateLink attachment represents reserved capacity in zonal GCP PSC Service attachments.  A PSC Endpoint can be connected to the Service attachment corresponding to each zone. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | PrivateLinkAttachmentStatus kind. | [readonly] 
**service_attachments** | [**List[NetworkingV1GcpPscServiceAttachment]**](NetworkingV1GcpPscServiceAttachment.md) | Array of GCP PSC Service attachments that can be used to connect PSC Endpoints for each zone.  | [readonly] 

## Example

```python
from openapi_client.models.networking_v1_gcp_private_link_attachment_status import NetworkingV1GcpPrivateLinkAttachmentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1GcpPrivateLinkAttachmentStatus from a JSON string
networking_v1_gcp_private_link_attachment_status_instance = NetworkingV1GcpPrivateLinkAttachmentStatus.from_json(json)
# print the JSON string representation of the object
print NetworkingV1GcpPrivateLinkAttachmentStatus.to_json()

# convert the object into a dict
networking_v1_gcp_private_link_attachment_status_dict = networking_v1_gcp_private_link_attachment_status_instance.to_dict()
# create an instance of NetworkingV1GcpPrivateLinkAttachmentStatus from a dict
networking_v1_gcp_private_link_attachment_status_form_dict = networking_v1_gcp_private_link_attachment_status.from_dict(networking_v1_gcp_private_link_attachment_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


