# NetworkingV1AzurePrivateLinkAttachmentStatus

Azure PrivateLink attachment represents reserved capacity in zonal PrivateLink services.  A Private Endpoint can be connected to the PLS corresponding to each zone. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | PrivateLinkAttachmentStatus kind. | [readonly] 
**private_link_services** | [**List[NetworkingV1AzurePrivateLinkService]**](NetworkingV1AzurePrivateLinkService.md) | Array of Azure PrivateLink services that can be used to connect PrivateEndpoints for each availability zone.  | [readonly] 

## Example

```python
from openapi_client.models.networking_v1_azure_private_link_attachment_status import NetworkingV1AzurePrivateLinkAttachmentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1AzurePrivateLinkAttachmentStatus from a JSON string
networking_v1_azure_private_link_attachment_status_instance = NetworkingV1AzurePrivateLinkAttachmentStatus.from_json(json)
# print the JSON string representation of the object
print NetworkingV1AzurePrivateLinkAttachmentStatus.to_json()

# convert the object into a dict
networking_v1_azure_private_link_attachment_status_dict = networking_v1_azure_private_link_attachment_status_instance.to_dict()
# create an instance of NetworkingV1AzurePrivateLinkAttachmentStatus from a dict
networking_v1_azure_private_link_attachment_status_form_dict = networking_v1_azure_private_link_attachment_status.from_dict(networking_v1_azure_private_link_attachment_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


