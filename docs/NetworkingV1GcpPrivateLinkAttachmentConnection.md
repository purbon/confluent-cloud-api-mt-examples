# NetworkingV1GcpPrivateLinkAttachmentConnection

Represents a connection between a GCP PSC Service Attachment and a PSC Endpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | PrivateLinkAttachmentConnection kind. | 
**private_service_connect_connection_id** | **str** | Id of the Private Service connection. | [readonly] 

## Example

```python
from openapi_client.models.networking_v1_gcp_private_link_attachment_connection import NetworkingV1GcpPrivateLinkAttachmentConnection

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1GcpPrivateLinkAttachmentConnection from a JSON string
networking_v1_gcp_private_link_attachment_connection_instance = NetworkingV1GcpPrivateLinkAttachmentConnection.from_json(json)
# print the JSON string representation of the object
print NetworkingV1GcpPrivateLinkAttachmentConnection.to_json()

# convert the object into a dict
networking_v1_gcp_private_link_attachment_connection_dict = networking_v1_gcp_private_link_attachment_connection_instance.to_dict()
# create an instance of NetworkingV1GcpPrivateLinkAttachmentConnection from a dict
networking_v1_gcp_private_link_attachment_connection_form_dict = networking_v1_gcp_private_link_attachment_connection.from_dict(networking_v1_gcp_private_link_attachment_connection_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


