# NetworkingV1AzurePrivateLinkAttachmentConnection

Represents a connection between an Azure PrivateLink service and a PrivateEndpoint.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | PrivateLinkAttachmentConnection kind. | 
**private_endpoint_resource_id** | **str** | Resource Id of the PrivateEndpoint that is connected to the PrivateLink service.  | 

## Example

```python
from openapi_client.models.networking_v1_azure_private_link_attachment_connection import NetworkingV1AzurePrivateLinkAttachmentConnection

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1AzurePrivateLinkAttachmentConnection from a JSON string
networking_v1_azure_private_link_attachment_connection_instance = NetworkingV1AzurePrivateLinkAttachmentConnection.from_json(json)
# print the JSON string representation of the object
print NetworkingV1AzurePrivateLinkAttachmentConnection.to_json()

# convert the object into a dict
networking_v1_azure_private_link_attachment_connection_dict = networking_v1_azure_private_link_attachment_connection_instance.to_dict()
# create an instance of NetworkingV1AzurePrivateLinkAttachmentConnection from a dict
networking_v1_azure_private_link_attachment_connection_form_dict = networking_v1_azure_private_link_attachment_connection.from_dict(networking_v1_azure_private_link_attachment_connection_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


