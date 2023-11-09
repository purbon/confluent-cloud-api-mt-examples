# IamV2IdentityProviderUpdate

`IdentityProvider` objects represent external OAuth/OpenID Connect providers within Confluent Cloud.  The API allows you to list, create, read, update, and delete your Identity Provider.   Related guide: [OAuth for Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/overview.html).  ## The Identity Providers Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.IdentityProvider\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `identity_providers_per_org` | Number of Identity Providers per organization | | `public_keys_per_provider` | Number of public keys saved per Identity Provider |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**IamV2IdentityProviderMetadata**](IamV2IdentityProviderMetadata.md) |  | [optional] 
**display_name** | **str** | The name of the Provider. | [optional] 
**description** | **str** | A description for your provider | [optional] 
**state** | **str** | The current state of the provider | [optional] [readonly] 
**keys** | [**List[IamV2JwksObject]**](IamV2JwksObject.md) | The JWKS provided by the Provider. We only express the &#x60;kid&#x60; and &#x60;alg&#x60; for each key set | [optional] [readonly] 

## Example

```python
from openapi_client.models.iam_v2_identity_provider_update import IamV2IdentityProviderUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2IdentityProviderUpdate from a JSON string
iam_v2_identity_provider_update_instance = IamV2IdentityProviderUpdate.from_json(json)
# print the JSON string representation of the object
print IamV2IdentityProviderUpdate.to_json()

# convert the object into a dict
iam_v2_identity_provider_update_dict = iam_v2_identity_provider_update_instance.to_dict()
# create an instance of IamV2IdentityProviderUpdate from a dict
iam_v2_identity_provider_update_form_dict = iam_v2_identity_provider_update.from_dict(iam_v2_identity_provider_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


