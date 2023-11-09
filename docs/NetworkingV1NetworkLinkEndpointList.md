# NetworkingV1NetworkLinkEndpointList

A Network Link Enpoint is associated with a Private Link Confluent Cloud Network at the origin and a Network Link Service (associated with another Private Link Confluent Cloud Network) at the target. It enables connectivity between the origin network and the target network. It can only be associated with a Private Link network.   Related guide: [Network Linking Overview](https://docs.confluent.io/cloud/current/networking/network-linking.html).  ## The Network Link Endpoints Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.NetworkLinkEndpoint\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `network_link_endpoints_per_network` | Number of network link endpoints per network |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**NetworkingV1NetworkLinkEndpointListMetadata**](NetworkingV1NetworkLinkEndpointListMetadata.md) |  | 
**data** | [**List[NetworkingV1NetworkLinkEndpointListDataInner]**](NetworkingV1NetworkLinkEndpointListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.networking_v1_network_link_endpoint_list import NetworkingV1NetworkLinkEndpointList

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkLinkEndpointList from a JSON string
networking_v1_network_link_endpoint_list_instance = NetworkingV1NetworkLinkEndpointList.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkLinkEndpointList.to_json()

# convert the object into a dict
networking_v1_network_link_endpoint_list_dict = networking_v1_network_link_endpoint_list_instance.to_dict()
# create an instance of NetworkingV1NetworkLinkEndpointList from a dict
networking_v1_network_link_endpoint_list_form_dict = networking_v1_network_link_endpoint_list.from_dict(networking_v1_network_link_endpoint_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


