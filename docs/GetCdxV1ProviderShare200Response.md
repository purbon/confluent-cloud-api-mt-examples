# GetCdxV1ProviderShare200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**metadata** | [**CdxV1ProviderShareMetadata**](CdxV1ProviderShareMetadata.md) |  | [optional] 
**consumer_user_name** | **str** | Name of the consumer | [optional] [readonly] 
**consumer_organization_name** | **str** | Consumer organization name | [optional] [readonly] 
**provider_user_name** | **str** | Name or email of the provider user. Deprecated | [readonly] 
**delivery_method** | **str** | Method by which the invite will be delivered | 
**consumer_restriction** | [**CdxV1ProviderShareConsumerRestriction**](CdxV1ProviderShareConsumerRestriction.md) |  | [optional] 
**invited_at** | **datetime** | The date and time at which consumer was invited | [readonly] 
**invite_expires_at** | **datetime** | The date and time at which the invitation will expire. Only for invited shares | [readonly] 
**redeemed_at** | **datetime** | The date and time at which the invite was redeemed | [optional] [readonly] 
**provider_user** | [**CdxV1ProviderShareProviderUser**](CdxV1ProviderShareProviderUser.md) |  | 
**service_account** | **object** |  | [optional] 
**cloud_cluster** | **object** |  | 
**status** | [**CdxV1ProviderShareStatus**](CdxV1ProviderShareStatus.md) |  | 

## Example

```python
from openapi_client.models.get_cdx_v1_provider_share200_response import GetCdxV1ProviderShare200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCdxV1ProviderShare200Response from a JSON string
get_cdx_v1_provider_share200_response_instance = GetCdxV1ProviderShare200Response.from_json(json)
# print the JSON string representation of the object
print GetCdxV1ProviderShare200Response.to_json()

# convert the object into a dict
get_cdx_v1_provider_share200_response_dict = get_cdx_v1_provider_share200_response_instance.to_dict()
# create an instance of GetCdxV1ProviderShare200Response from a dict
get_cdx_v1_provider_share200_response_form_dict = get_cdx_v1_provider_share200_response.from_dict(get_cdx_v1_provider_share200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


