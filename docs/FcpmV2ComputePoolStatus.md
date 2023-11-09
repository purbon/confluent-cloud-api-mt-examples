# FcpmV2ComputePoolStatus

The status of the Compute Pool

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | Status of the Flink compute pool. | [readonly] 
**current_cfu** | **int** | The number of Confluent Flink Units (CFUs) currently allocated to this Flink compute pool. | [readonly] 

## Example

```python
from openapi_client.models.fcpm_v2_compute_pool_status import FcpmV2ComputePoolStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FcpmV2ComputePoolStatus from a JSON string
fcpm_v2_compute_pool_status_instance = FcpmV2ComputePoolStatus.from_json(json)
# print the JSON string representation of the object
print FcpmV2ComputePoolStatus.to_json()

# convert the object into a dict
fcpm_v2_compute_pool_status_dict = fcpm_v2_compute_pool_status_instance.to_dict()
# create an instance of FcpmV2ComputePoolStatus from a dict
fcpm_v2_compute_pool_status_form_dict = fcpm_v2_compute_pool_status.from_dict(fcpm_v2_compute_pool_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


