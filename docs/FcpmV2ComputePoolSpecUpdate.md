# FcpmV2ComputePoolSpecUpdate

The desired state of the Compute Pool

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the Flink compute pool. | [optional] 
**max_cfu** | **int** | Maximum number of Confluent Flink Units (CFUs) that the Flink compute pool should auto-scale to.  | [optional] 
**environment** | [**GlobalObjectReference**](GlobalObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.fcpm_v2_compute_pool_spec_update import FcpmV2ComputePoolSpecUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of FcpmV2ComputePoolSpecUpdate from a JSON string
fcpm_v2_compute_pool_spec_update_instance = FcpmV2ComputePoolSpecUpdate.from_json(json)
# print the JSON string representation of the object
print FcpmV2ComputePoolSpecUpdate.to_json()

# convert the object into a dict
fcpm_v2_compute_pool_spec_update_dict = fcpm_v2_compute_pool_spec_update_instance.to_dict()
# create an instance of FcpmV2ComputePoolSpecUpdate from a dict
fcpm_v2_compute_pool_spec_update_form_dict = fcpm_v2_compute_pool_spec_update.from_dict(fcpm_v2_compute_pool_spec_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


