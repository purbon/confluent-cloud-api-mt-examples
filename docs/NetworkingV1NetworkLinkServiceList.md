# NetworkingV1NetworkLinkServiceList

Network Link Service is associated with a Private Link Confluent Cloud Network. It enables connectivity from other Private Link Confluent Cloud Networks based on the configured accept policies.   Related guide: [Network Linking Overview](https://docs.confluent.io/cloud/current/networking/network-linking.html).  ## The Network Link Services Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.NetworkLinkService\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `network_link_service_per_network` | Number of network link services per network |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**NetworkingV1NetworkLinkServiceListMetadata**](NetworkingV1NetworkLinkServiceListMetadata.md) |  | 
**data** | [**List[NetworkingV1NetworkLinkServiceListDataInner]**](NetworkingV1NetworkLinkServiceListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.networking_v1_network_link_service_list import NetworkingV1NetworkLinkServiceList

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkLinkServiceList from a JSON string
networking_v1_network_link_service_list_instance = NetworkingV1NetworkLinkServiceList.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkLinkServiceList.to_json()

# convert the object into a dict
networking_v1_network_link_service_list_dict = networking_v1_network_link_service_list_instance.to_dict()
# create an instance of NetworkingV1NetworkLinkServiceList from a dict
networking_v1_network_link_service_list_form_dict = networking_v1_network_link_service_list.from_dict(networking_v1_network_link_service_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


