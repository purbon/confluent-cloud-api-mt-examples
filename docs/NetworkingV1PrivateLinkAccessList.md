# NetworkingV1PrivateLinkAccessList

Add or remove access to PrivateLink endpoints by AWS account, Azure subscription and GCP project ID.  Related guide: [Private Links Overview](https://docs.confluent.io/cloud/current/networking/private-links/index.html).  ## The Private Link Accesses Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.PrivateLinkAccess\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `private_link_accounts_per_network` | Number of AWS accounts per network | | `private_link_subscriptions_per_network` | Number of Azure subscriptions per network | | `private_service_connect_projects_per_network` | Number of GCP projects per network |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**NetworkingV1PrivateLinkAccessListMetadata**](NetworkingV1PrivateLinkAccessListMetadata.md) |  | 
**data** | [**List[NetworkingV1PrivateLinkAccessListDataInner]**](NetworkingV1PrivateLinkAccessListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.networking_v1_private_link_access_list import NetworkingV1PrivateLinkAccessList

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAccessList from a JSON string
networking_v1_private_link_access_list_instance = NetworkingV1PrivateLinkAccessList.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAccessList.to_json()

# convert the object into a dict
networking_v1_private_link_access_list_dict = networking_v1_private_link_access_list_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAccessList from a dict
networking_v1_private_link_access_list_form_dict = networking_v1_private_link_access_list.from_dict(networking_v1_private_link_access_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


