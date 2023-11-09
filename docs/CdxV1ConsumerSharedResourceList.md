# CdxV1ConsumerSharedResourceList

`ConsumerSharedResource` object contains details of the data stream (topic, schema registry subjects, sharing metadata) that you received through Stream Sharing.   ## The Consumer Shared Resources Model <SchemaDefinition schemaRef=\"#/components/schemas/cdx.v1.ConsumerSharedResource\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**CdxV1ConsumerSharedResourceListMetadata**](CdxV1ConsumerSharedResourceListMetadata.md) |  | 
**data** | [**List[CdxV1ConsumerSharedResourceListDataInner]**](CdxV1ConsumerSharedResourceListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.cdx_v1_consumer_shared_resource_list import CdxV1ConsumerSharedResourceList

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1ConsumerSharedResourceList from a JSON string
cdx_v1_consumer_shared_resource_list_instance = CdxV1ConsumerSharedResourceList.from_json(json)
# print the JSON string representation of the object
print CdxV1ConsumerSharedResourceList.to_json()

# convert the object into a dict
cdx_v1_consumer_shared_resource_list_dict = cdx_v1_consumer_shared_resource_list_instance.to_dict()
# create an instance of CdxV1ConsumerSharedResourceList from a dict
cdx_v1_consumer_shared_resource_list_form_dict = cdx_v1_consumer_shared_resource_list.from_dict(cdx_v1_consumer_shared_resource_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


