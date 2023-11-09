# NetworkingV1NetworkStatusCloud

The cloud-specific network details. These will be populated when the network reaches the READY state.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Network kind type. | 
**vpc** | **str** | The Confluent Cloud VPC ID. | [readonly] 
**account** | **str** | The AWS account ID associated with the Confluent Cloud VPC. | [readonly] 
**private_link_endpoint_service** | **str** | The endpoint service of the Confluent Cloud VPC. (used for PrivateLink) if available. | [optional] [readonly] 
**project** | **str** | The GCP Project ID associated with the Confluent Cloud VPC. | [readonly] 
**vpc_network** | **str** | The network name of the Confluent Cloud VPC. | [readonly] 
**private_service_connect_service_attachments** | **Dict[str, str]** | The mapping of zones to Private Service Connect Service Attachments if available. Keys are zones and values are [GCP Private Service Connect Service Attachment](https://cloud.google.com/vpc/docs/configure-private-service-connect-producer#api_7)  | [optional] [readonly] 
**vnet** | **str** | The resource ID of the Confluent Cloud VNet. | [readonly] 
**subscription** | **str** | The Azure Subscription ID associated with the Confluent Cloud VPC. | [readonly] 
**private_link_service_aliases** | **Dict[str, str]** | The mapping of zones to Private Link Service Aliases if available. Keys are zones and values are [Azure Private Link Service Aliases](https://docs.microsoft.com/en-us/azure/private-link/private-link-service-overview#share-your-service).  | [optional] [readonly] 
**private_link_service_resource_ids** | **Dict[str, str]** | The mapping of zones to Private Link Service Resource IDs if available. Keys are zones and values are [Azure Private Link Service Resource IDs](https://docs.microsoft.com/en-us/azure/private-link/private-link-service-overview#share-your-service).  | [optional] [readonly] 

## Example

```python
from openapi_client.models.networking_v1_network_status_cloud import NetworkingV1NetworkStatusCloud

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkStatusCloud from a JSON string
networking_v1_network_status_cloud_instance = NetworkingV1NetworkStatusCloud.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkStatusCloud.to_json()

# convert the object into a dict
networking_v1_network_status_cloud_dict = networking_v1_network_status_cloud_instance.to_dict()
# create an instance of NetworkingV1NetworkStatusCloud from a dict
networking_v1_network_status_cloud_form_dict = networking_v1_network_status_cloud.from_dict(networking_v1_network_status_cloud_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


