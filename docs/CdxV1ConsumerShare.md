# CdxV1ConsumerShare

`ConsumerShare` object respresents the share that you received through Stream Sharing.   Related guide: [Consumer Stream Shares in Confluent Cloud](https://docs.confluent.io/cloud/current/stream-sharing/consume-shared-data.html).  ## The Consumer Shares Model <SchemaDefinition schemaRef=\"#/components/schemas/cdx.v1.ConsumerShare\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**CdxV1ConsumerShareMetadata**](CdxV1ConsumerShareMetadata.md) |  | [optional] 
**provider_organization_name** | **str** | Provider organization name | [optional] [readonly] 
**provider_user_name** | **str** | Name or email of the provider user | [optional] [readonly] 
**invite_expires_at** | **datetime** | The date and time at which the invitation will expire. Only for invited shares | [optional] [readonly] 
**consumer_organization_name** | **str** | Consumer organization name. Deprecated | [optional] [readonly] 
**consumer_user_name** | **str** | Name of the consumer. Deprecated | [optional] [readonly] 
**consumer_user** | [**CdxV1ConsumerShareConsumerUser**](CdxV1ConsumerShareConsumerUser.md) |  | [optional] 
**status** | [**CdxV1ConsumerShareStatus**](CdxV1ConsumerShareStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.cdx_v1_consumer_share import CdxV1ConsumerShare

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1ConsumerShare from a JSON string
cdx_v1_consumer_share_instance = CdxV1ConsumerShare.from_json(json)
# print the JSON string representation of the object
print CdxV1ConsumerShare.to_json()

# convert the object into a dict
cdx_v1_consumer_share_dict = cdx_v1_consumer_share_instance.to_dict()
# create an instance of CdxV1ConsumerShare from a dict
cdx_v1_consumer_share_form_dict = cdx_v1_consumer_share.from_dict(cdx_v1_consumer_share_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


