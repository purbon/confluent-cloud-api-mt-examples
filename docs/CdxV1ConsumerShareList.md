# CdxV1ConsumerShareList

`ConsumerShare` object respresents the share that you received through Stream Sharing.   Related guide: [Consumer Stream Shares in Confluent Cloud](https://docs.confluent.io/cloud/current/stream-sharing/consume-shared-data.html).  ## The Consumer Shares Model <SchemaDefinition schemaRef=\"#/components/schemas/cdx.v1.ConsumerShare\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**CdxV1ConsumerShareListMetadata**](CdxV1ConsumerShareListMetadata.md) |  | 
**data** | [**List[CdxV1ConsumerShareListDataInner]**](CdxV1ConsumerShareListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.cdx_v1_consumer_share_list import CdxV1ConsumerShareList

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1ConsumerShareList from a JSON string
cdx_v1_consumer_share_list_instance = CdxV1ConsumerShareList.from_json(json)
# print the JSON string representation of the object
print CdxV1ConsumerShareList.to_json()

# convert the object into a dict
cdx_v1_consumer_share_list_dict = cdx_v1_consumer_share_list_instance.to_dict()
# create an instance of CdxV1ConsumerShareList from a dict
cdx_v1_consumer_share_list_form_dict = cdx_v1_consumer_share_list.from_dict(cdx_v1_consumer_share_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


