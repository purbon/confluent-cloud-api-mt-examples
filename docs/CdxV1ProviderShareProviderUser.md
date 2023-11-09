# CdxV1ProviderShareProviderUser

The provider user/inviter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the referred resource | 
**related** | **str** | API URL for accessing or modifying the referred object | [readonly] 
**resource_name** | **str** | CRN reference to the referred resource | [readonly] 

## Example

```python
from openapi_client.models.cdx_v1_provider_share_provider_user import CdxV1ProviderShareProviderUser

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1ProviderShareProviderUser from a JSON string
cdx_v1_provider_share_provider_user_instance = CdxV1ProviderShareProviderUser.from_json(json)
# print the JSON string representation of the object
print CdxV1ProviderShareProviderUser.to_json()

# convert the object into a dict
cdx_v1_provider_share_provider_user_dict = cdx_v1_provider_share_provider_user_instance.to_dict()
# create an instance of CdxV1ProviderShareProviderUser from a dict
cdx_v1_provider_share_provider_user_form_dict = cdx_v1_provider_share_provider_user.from_dict(cdx_v1_provider_share_provider_user_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


