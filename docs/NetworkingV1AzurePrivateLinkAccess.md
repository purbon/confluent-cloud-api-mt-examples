# NetworkingV1AzurePrivateLinkAccess

Azure PrivateLink access configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | PrivateLink kind type. | 
**subscription** | **str** | The Azure subscription ID for the account containing the VNets you want to connect from using Azure Private Link. You can find your Azure subscription ID in the subscription section of your [Microsoft Azure Portal](https://portal.azure.com/#blade/Microsoft_Azure_Billing/SubscriptionsBlade). Must be a valid **32 character UUID string**.  | 

## Example

```python
from openapi_client.models.networking_v1_azure_private_link_access import NetworkingV1AzurePrivateLinkAccess

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1AzurePrivateLinkAccess from a JSON string
networking_v1_azure_private_link_access_instance = NetworkingV1AzurePrivateLinkAccess.from_json(json)
# print the JSON string representation of the object
print NetworkingV1AzurePrivateLinkAccess.to_json()

# convert the object into a dict
networking_v1_azure_private_link_access_dict = networking_v1_azure_private_link_access_instance.to_dict()
# create an instance of NetworkingV1AzurePrivateLinkAccess from a dict
networking_v1_azure_private_link_access_form_dict = networking_v1_azure_private_link_access.from_dict(networking_v1_azure_private_link_access_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


