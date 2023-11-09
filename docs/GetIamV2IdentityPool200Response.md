# GetIamV2IdentityPool200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**metadata** | [**IamV2IdentityPoolMetadata**](IamV2IdentityPoolMetadata.md) |  | [optional] 
**display_name** | **str** | The name of the &#x60;IdentityPool&#x60;. | 
**description** | **str** | A description of how this &#x60;IdentityPool&#x60; is used | 
**identity_claim** | **str** | The JSON Web Token (JWT) claim to extract the authenticating identity to Confluent resources from (see [Registered Claim Names](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1) for more details). This appears in the audit log records, showing, for example, that \&quot;identity Z used identity pool X to access topic A\&quot;. | 
**filter** | **str** | A filter expression in [Supported Common Expression Language (CEL)](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/identity-pools.html#supported-common-expression-language-cel-filters) that specifies which identities can authenticate using your identity pool (see [Set identity pool filters](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/identity-pools.html#set-identity-pool-filters) for more details). | 
**principal** | **str** | Represents the federated identity associated with this pool. | [readonly] 
**state** | **str** | The current state of the identity pool | [readonly] 

## Example

```python
from openapi_client.models.get_iam_v2_identity_pool200_response import GetIamV2IdentityPool200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIamV2IdentityPool200Response from a JSON string
get_iam_v2_identity_pool200_response_instance = GetIamV2IdentityPool200Response.from_json(json)
# print the JSON string representation of the object
print GetIamV2IdentityPool200Response.to_json()

# convert the object into a dict
get_iam_v2_identity_pool200_response_dict = get_iam_v2_identity_pool200_response_instance.to_dict()
# create an instance of GetIamV2IdentityPool200Response from a dict
get_iam_v2_identity_pool200_response_form_dict = get_iam_v2_identity_pool200_response.from_dict(get_iam_v2_identity_pool200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


