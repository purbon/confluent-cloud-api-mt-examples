# FcpmV2RegionList

`Region` objects represent cloud provider regions available when placing Flink compute pools. The API allows you to list Flink regions.   ## The Regions Model <SchemaDefinition schemaRef=\"#/components/schemas/fcpm.v2.Region\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**FcpmV2RegionListMetadata**](FcpmV2RegionListMetadata.md) |  | 
**data** | [**List[FcpmV2RegionListDataInner]**](FcpmV2RegionListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.fcpm_v2_region_list import FcpmV2RegionList

# TODO update the JSON string below
json = "{}"
# create an instance of FcpmV2RegionList from a JSON string
fcpm_v2_region_list_instance = FcpmV2RegionList.from_json(json)
# print the JSON string representation of the object
print FcpmV2RegionList.to_json()

# convert the object into a dict
fcpm_v2_region_list_dict = fcpm_v2_region_list_instance.to_dict()
# create an instance of FcpmV2RegionList from a dict
fcpm_v2_region_list_form_dict = fcpm_v2_region_list.from_dict(fcpm_v2_region_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


