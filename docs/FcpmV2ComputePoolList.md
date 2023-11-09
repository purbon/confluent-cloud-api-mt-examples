# FcpmV2ComputePoolList

A Compute Pool represents a set of compute resources that is used to run your Queries. The resources (CPUs, memory,…) provided by a Compute Pool are shared between all Queries that use it.   ## The Compute Pools Model <SchemaDefinition schemaRef=\"#/components/schemas/fcpm.v2.ComputePool\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**FcpmV2ComputePoolListMetadata**](FcpmV2ComputePoolListMetadata.md) |  | 
**data** | [**List[FcpmV2ComputePoolListDataInner]**](FcpmV2ComputePoolListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.fcpm_v2_compute_pool_list import FcpmV2ComputePoolList

# TODO update the JSON string below
json = "{}"
# create an instance of FcpmV2ComputePoolList from a JSON string
fcpm_v2_compute_pool_list_instance = FcpmV2ComputePoolList.from_json(json)
# print the JSON string representation of the object
print FcpmV2ComputePoolList.to_json()

# convert the object into a dict
fcpm_v2_compute_pool_list_dict = fcpm_v2_compute_pool_list_instance.to_dict()
# create an instance of FcpmV2ComputePoolList from a dict
fcpm_v2_compute_pool_list_form_dict = fcpm_v2_compute_pool_list.from_dict(fcpm_v2_compute_pool_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


