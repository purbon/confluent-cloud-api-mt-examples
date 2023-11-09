# IamV2IdentityPoolList

`IdentityPool` objects represent groups of identities tied to a given a `IdentityProvider` that authorizes them to Confluent Cloud resources.  It provides a mapping functionality of your `Identity Provider` user to a Confluent identity pool that is then used to provide access to Confluent Resources.   Related guide: [Use identity pools with your OAuth provider](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/identity-pools.html).  ## The Identity Pools Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.IdentityPool\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `identity_pools_per_provider` | Number of Identity Pools per Identity Provider |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**IamV2IdentityPoolListMetadata**](IamV2IdentityPoolListMetadata.md) |  | 
**data** | [**List[IamV2IdentityPoolListDataInner]**](IamV2IdentityPoolListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.iam_v2_identity_pool_list import IamV2IdentityPoolList

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2IdentityPoolList from a JSON string
iam_v2_identity_pool_list_instance = IamV2IdentityPoolList.from_json(json)
# print the JSON string representation of the object
print IamV2IdentityPoolList.to_json()

# convert the object into a dict
iam_v2_identity_pool_list_dict = iam_v2_identity_pool_list_instance.to_dict()
# create an instance of IamV2IdentityPoolList from a dict
iam_v2_identity_pool_list_form_dict = iam_v2_identity_pool_list.from_dict(iam_v2_identity_pool_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


