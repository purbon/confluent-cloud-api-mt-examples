# NetworkingV1PeeringList

Add or remove VPC/VNet peering connections between your VPC/VNet and Confluent Cloud.  Related guide: [Peering Connections Overview](https://docs.confluent.io/cloud/current/networking/peering/overview.html).  ## The Peerings Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.Peering\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `peerings_per_network` | Number of peerings per network |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**NetworkingV1PeeringListMetadata**](NetworkingV1PeeringListMetadata.md) |  | 
**data** | [**List[NetworkingV1PeeringListDataInner]**](NetworkingV1PeeringListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.networking_v1_peering_list import NetworkingV1PeeringList

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PeeringList from a JSON string
networking_v1_peering_list_instance = NetworkingV1PeeringList.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PeeringList.to_json()

# convert the object into a dict
networking_v1_peering_list_dict = networking_v1_peering_list_instance.to_dict()
# create an instance of NetworkingV1PeeringList from a dict
networking_v1_peering_list_form_dict = networking_v1_peering_list.from_dict(networking_v1_peering_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


