# CdxV1ProviderShare

`ProviderShare` object respresents the share that you have created through Stream Sharing.   Related guide: [Provider Stream Shares in Confluent Cloud](https://docs.confluent.io/cloud/current/stream-sharing/produce-shared-data.html#stream-shares).  ## The Provider Shares Model <SchemaDefinition schemaRef=\"#/components/schemas/cdx.v1.ProviderShare\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**CdxV1ProviderShareMetadata**](CdxV1ProviderShareMetadata.md) |  | [optional] 
**consumer_user_name** | **str** | Name of the consumer | [optional] [readonly] 
**consumer_organization_name** | **str** | Consumer organization name | [optional] [readonly] 
**provider_user_name** | **str** | Name or email of the provider user. Deprecated | [optional] [readonly] 
**delivery_method** | **str** | Method by which the invite will be delivered | [optional] 
**consumer_restriction** | [**CdxV1ProviderShareConsumerRestriction**](CdxV1ProviderShareConsumerRestriction.md) |  | [optional] 
**invited_at** | **datetime** | The date and time at which consumer was invited | [optional] [readonly] 
**invite_expires_at** | **datetime** | The date and time at which the invitation will expire. Only for invited shares | [optional] [readonly] 
**redeemed_at** | **datetime** | The date and time at which the invite was redeemed | [optional] [readonly] 
**provider_user** | [**CdxV1ProviderShareProviderUser**](CdxV1ProviderShareProviderUser.md) |  | [optional] 
**service_account** | [**GlobalObjectReference**](GlobalObjectReference.md) |  | [optional] 
**cloud_cluster** | [**EnvScopedObjectReference**](EnvScopedObjectReference.md) |  | [optional] 
**status** | [**CdxV1ProviderShareStatus**](CdxV1ProviderShareStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.cdx_v1_provider_share import CdxV1ProviderShare

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1ProviderShare from a JSON string
cdx_v1_provider_share_instance = CdxV1ProviderShare.from_json(json)
# print the JSON string representation of the object
print CdxV1ProviderShare.to_json()

# convert the object into a dict
cdx_v1_provider_share_dict = cdx_v1_provider_share_instance.to_dict()
# create an instance of CdxV1ProviderShare from a dict
cdx_v1_provider_share_form_dict = cdx_v1_provider_share.from_dict(cdx_v1_provider_share_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


