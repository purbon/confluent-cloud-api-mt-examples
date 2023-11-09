# NetworkingV1Network

`Network` represents a network (VPC) in Confluent Cloud. All Networks exist within Confluent-managed cloud provider accounts. Dedicated networks support more networking options but can only contain Dedicated clusters. Shared networks can contain any cluster type.  The API allows you to list, create, read, update, and delete your networks.   Related guide: [APIs to manage networks in Confluent Cloud](https://docs.confluent.io/cloud/current/networking/overview.html).  ## The Networks Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.Network\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `dedicated_networks_per_environment` | Number of dedicated networks per Confluent Cloud environment |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**NetworkingV1NetworkMetadata**](NetworkingV1NetworkMetadata.md) |  | [optional] 
**spec** | [**NetworkingV1NetworkSpec**](NetworkingV1NetworkSpec.md) |  | [optional] 
**status** | [**NetworkingV1NetworkStatus**](NetworkingV1NetworkStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_network import NetworkingV1Network

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1Network from a JSON string
networking_v1_network_instance = NetworkingV1Network.from_json(json)
# print the JSON string representation of the object
print NetworkingV1Network.to_json()

# convert the object into a dict
networking_v1_network_dict = networking_v1_network_instance.to_dict()
# create an instance of NetworkingV1Network from a dict
networking_v1_network_form_dict = networking_v1_network.from_dict(networking_v1_network_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


