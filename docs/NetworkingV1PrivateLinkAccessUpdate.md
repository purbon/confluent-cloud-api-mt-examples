# NetworkingV1PrivateLinkAccessUpdate

Add or remove access to PrivateLink endpoints by AWS account, Azure subscription and GCP project ID.  Related guide: [Private Links Overview](https://docs.confluent.io/cloud/current/networking/private-links/index.html).  ## The Private Link Accesses Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.PrivateLinkAccess\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `private_link_accounts_per_network` | Number of AWS accounts per network | | `private_link_subscriptions_per_network` | Number of Azure subscriptions per network | | `private_service_connect_projects_per_network` | Number of GCP projects per network |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**NetworkingV1PrivateLinkAccessMetadata**](NetworkingV1PrivateLinkAccessMetadata.md) |  | [optional] 
**spec** | [**NetworkingV1PrivateLinkAccessSpecUpdate**](NetworkingV1PrivateLinkAccessSpecUpdate.md) |  | [optional] 
**status** | [**NetworkingV1PrivateLinkAccessStatus**](NetworkingV1PrivateLinkAccessStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_private_link_access_update import NetworkingV1PrivateLinkAccessUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAccessUpdate from a JSON string
networking_v1_private_link_access_update_instance = NetworkingV1PrivateLinkAccessUpdate.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAccessUpdate.to_json()

# convert the object into a dict
networking_v1_private_link_access_update_dict = networking_v1_private_link_access_update_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAccessUpdate from a dict
networking_v1_private_link_access_update_form_dict = networking_v1_private_link_access_update.from_dict(networking_v1_private_link_access_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


