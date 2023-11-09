# NetworkingV1AzurePrivateLinkService

Azure Private Link Service for an availability zone with reserved capacity to connect a Private Endpoint. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone** | **str** | Availability zone associated with the Azure PrivateLink service. | [readonly] 
**private_link_service_alias** | **str** | Azure PrivateLink service alias for the availability zone. | [readonly] 
**private_link_service_resource_id** | **str** | Azure PrivateLink service resource id for the availability zone. | [readonly] 

## Example

```python
from openapi_client.models.networking_v1_azure_private_link_service import NetworkingV1AzurePrivateLinkService

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1AzurePrivateLinkService from a JSON string
networking_v1_azure_private_link_service_instance = NetworkingV1AzurePrivateLinkService.from_json(json)
# print the JSON string representation of the object
print NetworkingV1AzurePrivateLinkService.to_json()

# convert the object into a dict
networking_v1_azure_private_link_service_dict = networking_v1_azure_private_link_service_instance.to_dict()
# create an instance of NetworkingV1AzurePrivateLinkService from a dict
networking_v1_azure_private_link_service_form_dict = networking_v1_azure_private_link_service.from_dict(networking_v1_azure_private_link_service_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


