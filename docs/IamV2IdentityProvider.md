# IamV2IdentityProvider

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
**issuer** | **str** | A publicly reachable issuer URI for the Identity Provider. The unique issuer URI string represents the entity for issuing tokens. | [optional] 
**jwks_uri** | **str** | A publicly reachable JSON Web Key Set (JWKS) URI for the Identity Provider. A JSON Web Key Set (JWKS) provides a set of keys containing the public keys used to verify any JSON Web Token (JWT) issued by your OAuth 2.0 identity provider. | [optional] 
**keys** | [**List[IamV2JwksObject]**](IamV2JwksObject.md) | The JWKS provided by the Provider. We only express the &#x60;kid&#x60; and &#x60;alg&#x60; for each key set | [optional] [readonly] 

## Example

```python
from openapi_client.models.iam_v2_identity_provider import IamV2IdentityProvider

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2IdentityProvider from a JSON string
iam_v2_identity_provider_instance = IamV2IdentityProvider.from_json(json)
# print the JSON string representation of the object
print IamV2IdentityProvider.to_json()

# convert the object into a dict
iam_v2_identity_provider_dict = iam_v2_identity_provider_instance.to_dict()
# create an instance of IamV2IdentityProvider from a dict
iam_v2_identity_provider_form_dict = iam_v2_identity_provider.from_dict(iam_v2_identity_provider_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


