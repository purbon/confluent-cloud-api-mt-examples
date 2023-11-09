# NetworkingV1NetworkLinkServiceUpdate

Network Link Service is associated with a Private Link Confluent Cloud Network. It enables connectivity from other Private Link Confluent Cloud Networks based on the configured accept policies.   Related guide: [Network Linking Overview](https://docs.confluent.io/cloud/current/networking/network-linking.html).  ## The Network Link Services Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.NetworkLinkService\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `network_link_service_per_network` | Number of network link services per network |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**NetworkingV1NetworkLinkServiceMetadata**](NetworkingV1NetworkLinkServiceMetadata.md) |  | [optional] 
**spec** | [**NetworkingV1NetworkLinkServiceSpecUpdate**](NetworkingV1NetworkLinkServiceSpecUpdate.md) |  | [optional] 
**status** | [**NetworkingV1NetworkLinkServiceStatus**](NetworkingV1NetworkLinkServiceStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_network_link_service_update import NetworkingV1NetworkLinkServiceUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkLinkServiceUpdate from a JSON string
networking_v1_network_link_service_update_instance = NetworkingV1NetworkLinkServiceUpdate.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkLinkServiceUpdate.to_json()

# convert the object into a dict
networking_v1_network_link_service_update_dict = networking_v1_network_link_service_update_instance.to_dict()
# create an instance of NetworkingV1NetworkLinkServiceUpdate from a dict
networking_v1_network_link_service_update_form_dict = networking_v1_network_link_service_update.from_dict(networking_v1_network_link_service_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


