# CreateIamV2IdentityProviderRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**IamV2IdentityProviderMetadata**](IamV2IdentityProviderMetadata.md) |  | [optional] 
**display_name** | **str** | The name of the Provider. | 
**description** | **str** | A description for your provider | 
**state** | **str** | The current state of the provider | [optional] [readonly] 
**issuer** | **str** | A publicly reachable issuer URI for the Identity Provider. The unique issuer URI string represents the entity for issuing tokens. | 
**jwks_uri** | **str** | A publicly reachable JSON Web Key Set (JWKS) URI for the Identity Provider. A JSON Web Key Set (JWKS) provides a set of keys containing the public keys used to verify any JSON Web Token (JWT) issued by your OAuth 2.0 identity provider. | 
**keys** | [**List[IamV2JwksObject]**](IamV2JwksObject.md) | The JWKS provided by the Provider. We only express the &#x60;kid&#x60; and &#x60;alg&#x60; for each key set | [optional] [readonly] 

## Example

```python
from openapi_client.models.create_iam_v2_identity_provider_request import CreateIamV2IdentityProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIamV2IdentityProviderRequest from a JSON string
create_iam_v2_identity_provider_request_instance = CreateIamV2IdentityProviderRequest.from_json(json)
# print the JSON string representation of the object
print CreateIamV2IdentityProviderRequest.to_json()

# convert the object into a dict
create_iam_v2_identity_provider_request_dict = create_iam_v2_identity_provider_request_instance.to_dict()
# create an instance of CreateIamV2IdentityProviderRequest from a dict
create_iam_v2_identity_provider_request_form_dict = create_iam_v2_identity_provider_request.from_dict(create_iam_v2_identity_provider_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


