# NetworkingV1Peering

Add or remove VPC/VNet peering connections between your VPC/VNet and Confluent Cloud.  Related guide: [Peering Connections Overview](https://docs.confluent.io/cloud/current/networking/peering/overview.html).  ## The Peerings Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.Peering\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `peerings_per_network` | Number of peerings per network |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**NetworkingV1PeeringMetadata**](NetworkingV1PeeringMetadata.md) |  | [optional] 
**spec** | [**NetworkingV1PeeringSpec**](NetworkingV1PeeringSpec.md) |  | [optional] 
**status** | [**NetworkingV1PeeringStatus**](NetworkingV1PeeringStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_peering import NetworkingV1Peering

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1Peering from a JSON string
networking_v1_peering_instance = NetworkingV1Peering.from_json(json)
# print the JSON string representation of the object
print NetworkingV1Peering.to_json()

# convert the object into a dict
networking_v1_peering_dict = networking_v1_peering_instance.to_dict()
# create an instance of NetworkingV1Peering from a dict
networking_v1_peering_form_dict = networking_v1_peering.from_dict(networking_v1_peering_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


