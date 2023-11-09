# IamV2IdentityProviderList

`IdentityProvider` objects represent external OAuth/OpenID Connect providers within Confluent Cloud.  The API allows you to list, create, read, update, and delete your Identity Provider.   Related guide: [OAuth for Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/overview.html).  ## The Identity Providers Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.IdentityProvider\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `identity_providers_per_org` | Number of Identity Providers per organization | | `public_keys_per_provider` | Number of public keys saved per Identity Provider |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**IamV2IdentityProviderListMetadata**](IamV2IdentityProviderListMetadata.md) |  | 
**data** | [**List[IamV2IdentityProviderListDataInner]**](IamV2IdentityProviderListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.iam_v2_identity_provider_list import IamV2IdentityProviderList

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2IdentityProviderList from a JSON string
iam_v2_identity_provider_list_instance = IamV2IdentityProviderList.from_json(json)
# print the JSON string representation of the object
print IamV2IdentityProviderList.to_json()

# convert the object into a dict
iam_v2_identity_provider_list_dict = iam_v2_identity_provider_list_instance.to_dict()
# create an instance of IamV2IdentityProviderList from a dict
iam_v2_identity_provider_list_form_dict = iam_v2_identity_provider_list.from_dict(iam_v2_identity_provider_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


