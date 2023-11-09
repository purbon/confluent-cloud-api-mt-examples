# FcpmV2ComputePool

A Compute Pool represents a set of compute resources that is used to run your Queries. The resources (CPUs, memory,…) provided by a Compute Pool are shared between all Queries that use it.   ## The Compute Pools Model <SchemaDefinition schemaRef=\"#/components/schemas/fcpm.v2.ComputePool\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**FcpmV2ComputePoolMetadata**](FcpmV2ComputePoolMetadata.md) |  | [optional] 
**spec** | [**FcpmV2ComputePoolSpec**](FcpmV2ComputePoolSpec.md) |  | [optional] 
**status** | [**FcpmV2ComputePoolStatus**](FcpmV2ComputePoolStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.fcpm_v2_compute_pool import FcpmV2ComputePool

# TODO update the JSON string below
json = "{}"
# create an instance of FcpmV2ComputePool from a JSON string
fcpm_v2_compute_pool_instance = FcpmV2ComputePool.from_json(json)
# print the JSON string representation of the object
print FcpmV2ComputePool.to_json()

# convert the object into a dict
fcpm_v2_compute_pool_dict = fcpm_v2_compute_pool_instance.to_dict()
# create an instance of FcpmV2ComputePool from a dict
fcpm_v2_compute_pool_form_dict = fcpm_v2_compute_pool.from_dict(fcpm_v2_compute_pool_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


