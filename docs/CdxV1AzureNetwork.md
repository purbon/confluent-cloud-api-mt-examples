# CdxV1AzureNetwork

The Azure network details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Network kind type. | 
**private_link_service_aliases** | **Dict[str, str]** | The mapping of zones to PrivateLink Service Aliases if available.  Keys are zones and values are [Azure PrivateLink Service Aliases](https://docs.microsoft.com/en-us/azure/private-link/private-link-service-overview#share-your-service)  | [optional] [readonly] 

## Example

```python
from openapi_client.models.cdx_v1_azure_network import CdxV1AzureNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1AzureNetwork from a JSON string
cdx_v1_azure_network_instance = CdxV1AzureNetwork.from_json(json)
# print the JSON string representation of the object
print CdxV1AzureNetwork.to_json()

# convert the object into a dict
cdx_v1_azure_network_dict = cdx_v1_azure_network_instance.to_dict()
# create an instance of CdxV1AzureNetwork from a dict
cdx_v1_azure_network_form_dict = cdx_v1_azure_network.from_dict(cdx_v1_azure_network_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


