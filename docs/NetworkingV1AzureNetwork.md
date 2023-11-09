# NetworkingV1AzureNetwork

The Azure network details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Network kind type. | 
**vnet** | **str** | The resource ID of the Confluent Cloud VNet. | [readonly] 
**subscription** | **str** | The Azure Subscription ID associated with the Confluent Cloud VPC. | [readonly] 
**private_link_service_aliases** | **Dict[str, str]** | The mapping of zones to Private Link Service Aliases if available. Keys are zones and values are [Azure Private Link Service Aliases](https://docs.microsoft.com/en-us/azure/private-link/private-link-service-overview#share-your-service).  | [optional] [readonly] 
**private_link_service_resource_ids** | **Dict[str, str]** | The mapping of zones to Private Link Service Resource IDs if available. Keys are zones and values are [Azure Private Link Service Resource IDs](https://docs.microsoft.com/en-us/azure/private-link/private-link-service-overview#share-your-service).  | [optional] [readonly] 

## Example

```python
from openapi_client.models.networking_v1_azure_network import NetworkingV1AzureNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1AzureNetwork from a JSON string
networking_v1_azure_network_instance = NetworkingV1AzureNetwork.from_json(json)
# print the JSON string representation of the object
print NetworkingV1AzureNetwork.to_json()

# convert the object into a dict
networking_v1_azure_network_dict = networking_v1_azure_network_instance.to_dict()
# create an instance of NetworkingV1AzureNetwork from a dict
networking_v1_azure_network_form_dict = networking_v1_azure_network.from_dict(networking_v1_azure_network_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


