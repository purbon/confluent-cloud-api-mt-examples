# NetworkingV1AzurePrivateLinkAttachmentConnectionStatus

Status of an Azure PrivateLink attachment connection for an availability zone.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | PrivateLinkAttachmentConnectionStatus kind. | 
**zone** | **str** | Availability zone associated with the Azure PrivateLink service. | [readonly] 
**private_link_service_alias** | **str** | Azure PrivateLink service alias for the availability zone. | [readonly] 
**private_link_service_resource_id** | **str** | Azure PrivateLink service resource id for the availability zone. | [readonly] 
**private_endpoint_resource_id** | **str** | Resource Id of the PrivateEndpoint (if any) that is connected to the PrivateLink service for this availability zone.  | [readonly] 

## Example

```python
from openapi_client.models.networking_v1_azure_private_link_attachment_connection_status import NetworkingV1AzurePrivateLinkAttachmentConnectionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1AzurePrivateLinkAttachmentConnectionStatus from a JSON string
networking_v1_azure_private_link_attachment_connection_status_instance = NetworkingV1AzurePrivateLinkAttachmentConnectionStatus.from_json(json)
# print the JSON string representation of the object
print NetworkingV1AzurePrivateLinkAttachmentConnectionStatus.to_json()

# convert the object into a dict
networking_v1_azure_private_link_attachment_connection_status_dict = networking_v1_azure_private_link_attachment_connection_status_instance.to_dict()
# create an instance of NetworkingV1AzurePrivateLinkAttachmentConnectionStatus from a dict
networking_v1_azure_private_link_attachment_connection_status_form_dict = networking_v1_azure_private_link_attachment_connection_status.from_dict(networking_v1_azure_private_link_attachment_connection_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


