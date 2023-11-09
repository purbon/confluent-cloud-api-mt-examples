# NetworkingV1PeeringSpecCloud

The cloud-specific peering details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Peering kind type. | 
**account** | **str** | The AWS account ID | 
**vpc** | **str** | The VPC ID you are peering with Confluent Cloud network. | 
**routes** | **List[str]** | The [CIDR blocks](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) of the VPC you are peering with Confluent Cloud network. This is used by Confluent Cloud network to route traffic back to your network. The CIDR block must be a private range and cannot overlap with the Confluent Cloud CIDR block.  | 
**customer_region** | **str** | The region of the VNet you are peering with Confluent Cloud network. | 
**project** | **str** | The Google Cloud project ID associated with the VPC that you are peering with Confluent Cloud network.  | 
**vpc_network** | **str** | The name of the VPC that you are peering with Confluent Cloud network. | 
**import_custom_routes** | **bool** | Enable customer route import. For more information, see [Importing custom routes](https://cloud.google.com/vpc/docs/vpc-peering#importing-exporting-routes).  | [optional] [default to False]
**tenant** | **str** | The Azure Tenant ID in which your Azure Subscription exists. Represents an organization in Azure Active Directory. You can find your Azure Tenant ID in the Azure Portal under [Azure Active Directory](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/Overview). Must be a valid **32 character UUID string**.  | 
**vnet** | **str** | The resource ID of the VNet that you are peering with Confluent Cloud. You can find the name of your Azure VNet in the [Azure Portal on the Overview tab of your Azure Virtual Network](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Network%2FvirtualNetworks). | 

## Example

```python
from openapi_client.models.networking_v1_peering_spec_cloud import NetworkingV1PeeringSpecCloud

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PeeringSpecCloud from a JSON string
networking_v1_peering_spec_cloud_instance = NetworkingV1PeeringSpecCloud.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PeeringSpecCloud.to_json()

# convert the object into a dict
networking_v1_peering_spec_cloud_dict = networking_v1_peering_spec_cloud_instance.to_dict()
# create an instance of NetworkingV1PeeringSpecCloud from a dict
networking_v1_peering_spec_cloud_form_dict = networking_v1_peering_spec_cloud.from_dict(networking_v1_peering_spec_cloud_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


