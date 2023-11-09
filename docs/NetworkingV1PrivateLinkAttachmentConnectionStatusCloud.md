# NetworkingV1PrivateLinkAttachmentConnectionStatusCloud

The cloud specific status of the PrivateLink attachment connection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | PrivateLinkAttachmentConnectionStatus kind. | 
**vpc_endpoint_service_name** | **str** | Id of the VPC Endpoint service used for PrivateLink. | [readonly] 
**vpc_endpoint_id** | **str** | Id of the VPC Endpoint (if any) that is connected to the VPC Endpoint service. | [readonly] 
**zone** | **str** | Zone associated with the GCP PrivateLink attachment connection. | [readonly] 
**private_link_service_alias** | **str** | Azure PrivateLink service alias for the availability zone. | [readonly] 
**private_link_service_resource_id** | **str** | Azure PrivateLink service resource id for the availability zone. | [readonly] 
**private_endpoint_resource_id** | **str** | Resource Id of the PrivateEndpoint (if any) that is connected to the PrivateLink service for this availability zone.  | [readonly] 
**private_service_connect_service_attachment** | **str** | GCP Private Service Connect ServiceAttachment for the zone. | [readonly] 
**private_service_connect_connection_id** | **str** | Id of the Private Service connection. | [readonly] 

## Example

```python
from openapi_client.models.networking_v1_private_link_attachment_connection_status_cloud import NetworkingV1PrivateLinkAttachmentConnectionStatusCloud

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAttachmentConnectionStatusCloud from a JSON string
networking_v1_private_link_attachment_connection_status_cloud_instance = NetworkingV1PrivateLinkAttachmentConnectionStatusCloud.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAttachmentConnectionStatusCloud.to_json()

# convert the object into a dict
networking_v1_private_link_attachment_connection_status_cloud_dict = networking_v1_private_link_attachment_connection_status_cloud_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAttachmentConnectionStatusCloud from a dict
networking_v1_private_link_attachment_connection_status_cloud_form_dict = networking_v1_private_link_attachment_connection_status_cloud.from_dict(networking_v1_private_link_attachment_connection_status_cloud_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


