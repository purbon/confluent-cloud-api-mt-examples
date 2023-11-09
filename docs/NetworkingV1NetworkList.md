# NetworkingV1NetworkList

`Network` represents a network (VPC) in Confluent Cloud. All Networks exist within Confluent-managed cloud provider accounts. Dedicated networks support more networking options but can only contain Dedicated clusters. Shared networks can contain any cluster type.  The API allows you to list, create, read, update, and delete your networks.   Related guide: [APIs to manage networks in Confluent Cloud](https://docs.confluent.io/cloud/current/networking/overview.html).  ## The Networks Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.Network\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `dedicated_networks_per_environment` | Number of dedicated networks per Confluent Cloud environment |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**NetworkingV1NetworkListMetadata**](NetworkingV1NetworkListMetadata.md) |  | 
**data** | [**List[NetworkingV1NetworkListDataInner]**](NetworkingV1NetworkListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.networking_v1_network_list import NetworkingV1NetworkList

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkList from a JSON string
networking_v1_network_list_instance = NetworkingV1NetworkList.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkList.to_json()

# convert the object into a dict
networking_v1_network_list_dict = networking_v1_network_list_instance.to_dict()
# create an instance of NetworkingV1NetworkList from a dict
networking_v1_network_list_form_dict = networking_v1_network_list.from_dict(networking_v1_network_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


