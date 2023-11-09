# FcpmV2ComputePoolSpec

The desired state of the Compute Pool

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the Flink compute pool. | [optional] 
**cloud** | **str** | The cloud service provider that runs the compute pool. | [optional] 
**http_endpoint** | **str** | The API endpoint of the Flink compute pool. | [optional] [readonly] 
**region** | **str** | Flink compute pools in the region provided will be able to use this identity pool | [optional] 
**max_cfu** | **int** | Maximum number of Confluent Flink Units (CFUs) that the Flink compute pool should auto-scale to.  | [optional] 
**environment** | [**GlobalObjectReference**](GlobalObjectReference.md) |  | [optional] 
**network** | [**EnvScopedObjectReference**](EnvScopedObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.fcpm_v2_compute_pool_spec import FcpmV2ComputePoolSpec

# TODO update the JSON string below
json = "{}"
# create an instance of FcpmV2ComputePoolSpec from a JSON string
fcpm_v2_compute_pool_spec_instance = FcpmV2ComputePoolSpec.from_json(json)
# print the JSON string representation of the object
print FcpmV2ComputePoolSpec.to_json()

# convert the object into a dict
fcpm_v2_compute_pool_spec_dict = fcpm_v2_compute_pool_spec_instance.to_dict()
# create an instance of FcpmV2ComputePoolSpec from a dict
fcpm_v2_compute_pool_spec_form_dict = fcpm_v2_compute_pool_spec.from_dict(fcpm_v2_compute_pool_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


