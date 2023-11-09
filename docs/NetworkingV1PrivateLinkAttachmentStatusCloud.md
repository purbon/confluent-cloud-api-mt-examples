# NetworkingV1PrivateLinkAttachmentStatusCloud

The cloud specific status of the PrivateLink attachment. These will be populated when the PrivateLink attachment reaches the WAITING_FOR_CONNECTIONS state.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | PrivateLinkAttachmentStatus kind. | [readonly] 
**vpc_endpoint_service** | [**NetworkingV1AwsPrivateLinkAttachmentStatusVpcEndpointService**](NetworkingV1AwsPrivateLinkAttachmentStatusVpcEndpointService.md) |  | 
**private_link_services** | [**List[NetworkingV1AzurePrivateLinkService]**](NetworkingV1AzurePrivateLinkService.md) | Array of Azure PrivateLink services that can be used to connect PrivateEndpoints for each availability zone.  | [readonly] 
**service_attachments** | [**List[NetworkingV1GcpPscServiceAttachment]**](NetworkingV1GcpPscServiceAttachment.md) | Array of GCP PSC Service attachments that can be used to connect PSC Endpoints for each zone.  | [readonly] 

## Example

```python
from openapi_client.models.networking_v1_private_link_attachment_status_cloud import NetworkingV1PrivateLinkAttachmentStatusCloud

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAttachmentStatusCloud from a JSON string
networking_v1_private_link_attachment_status_cloud_instance = NetworkingV1PrivateLinkAttachmentStatusCloud.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAttachmentStatusCloud.to_json()

# convert the object into a dict
networking_v1_private_link_attachment_status_cloud_dict = networking_v1_private_link_attachment_status_cloud_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAttachmentStatusCloud from a dict
networking_v1_private_link_attachment_status_cloud_form_dict = networking_v1_private_link_attachment_status_cloud.from_dict(networking_v1_private_link_attachment_status_cloud_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


