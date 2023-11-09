# FcpmV2RegionListDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**metadata** | [**FcpmV2RegionMetadata**](FcpmV2RegionMetadata.md) |  | 
**display_name** | **str** | The display name. | [readonly] 
**cloud** | **str** | The cloud service provider that hosts the region. | [readonly] 
**region_name** | **str** | The region name. | [readonly] 
**http_endpoint** | **str** | The regional API endpoint for flink compute pools. | [optional] [readonly] 

## Example

```python
from openapi_client.models.fcpm_v2_region_list_data_inner import FcpmV2RegionListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of FcpmV2RegionListDataInner from a JSON string
fcpm_v2_region_list_data_inner_instance = FcpmV2RegionListDataInner.from_json(json)
# print the JSON string representation of the object
print FcpmV2RegionListDataInner.to_json()

# convert the object into a dict
fcpm_v2_region_list_data_inner_dict = fcpm_v2_region_list_data_inner_instance.to_dict()
# create an instance of FcpmV2RegionListDataInner from a dict
fcpm_v2_region_list_data_inner_form_dict = fcpm_v2_region_list_data_inner.from_dict(fcpm_v2_region_list_data_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


