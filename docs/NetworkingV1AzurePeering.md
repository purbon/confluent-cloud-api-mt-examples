# NetworkingV1AzurePeering

Azure VNet Peering.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Peering kind type. | 
**tenant** | **str** | The Azure Tenant ID in which your Azure Subscription exists. Represents an organization in Azure Active Directory. You can find your Azure Tenant ID in the Azure Portal under [Azure Active Directory](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview). Must be a valid **32 character UUID string**.  | 
**vnet** | **str** | The resource ID of the VNet that you are peering with Confluent Cloud. You can find the name of your Azure VNet in the [Azure Portal on the Overview tab of your Azure Virtual Network](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Network%2FvirtualNetworks). | 
**customer_region** | **str** | The region of the VNet you are peering with Confluent Cloud network. | 

## Example

```python
from openapi_client.models.networking_v1_azure_peering import NetworkingV1AzurePeering

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1AzurePeering from a JSON string
networking_v1_azure_peering_instance = NetworkingV1AzurePeering.from_json(json)
# print the JSON string representation of the object
print NetworkingV1AzurePeering.to_json()

# convert the object into a dict
networking_v1_azure_peering_dict = networking_v1_azure_peering_instance.to_dict()
# create an instance of NetworkingV1AzurePeering from a dict
networking_v1_azure_peering_form_dict = networking_v1_azure_peering.from_dict(networking_v1_azure_peering_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


