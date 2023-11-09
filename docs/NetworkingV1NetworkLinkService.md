# NetworkingV1NetworkLinkService

Network Link Service is associated with a Private Link Confluent Cloud Network. It enables connectivity from other Private Link Confluent Cloud Networks based on the configured accept policies.   Related guide: [Network Linking Overview](https://docs.confluent.io/cloud/current/networking/network-linking.html).  ## The Network Link Services Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.NetworkLinkService\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `network_link_service_per_network` | Number of network link services per network |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**NetworkingV1NetworkLinkServiceMetadata**](NetworkingV1NetworkLinkServiceMetadata.md) |  | [optional] 
**spec** | [**NetworkingV1NetworkLinkServiceSpec**](NetworkingV1NetworkLinkServiceSpec.md) |  | [optional] 
**status** | [**NetworkingV1NetworkLinkServiceStatus**](NetworkingV1NetworkLinkServiceStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_network_link_service import NetworkingV1NetworkLinkService

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkLinkService from a JSON string
networking_v1_network_link_service_instance = NetworkingV1NetworkLinkService.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkLinkService.to_json()

# convert the object into a dict
networking_v1_network_link_service_dict = networking_v1_network_link_service_instance.to_dict()
# create an instance of NetworkingV1NetworkLinkService from a dict
networking_v1_network_link_service_form_dict = networking_v1_network_link_service.from_dict(networking_v1_network_link_service_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


