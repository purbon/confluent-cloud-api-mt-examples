# FcpmV2ComputePoolListMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **object** |  | [optional] 
**last** | **object** |  | [optional] 
**prev** | **object** |  | [optional] 
**next** | **object** |  | [optional] 
**total_size** | **int** | Number of records in the full result set. This response may be paginated and have a smaller number of records. | [optional] 

## Example

```python
from openapi_client.models.fcpm_v2_compute_pool_list_metadata import FcpmV2ComputePoolListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FcpmV2ComputePoolListMetadata from a JSON string
fcpm_v2_compute_pool_list_metadata_instance = FcpmV2ComputePoolListMetadata.from_json(json)
# print the JSON string representation of the object
print FcpmV2ComputePoolListMetadata.to_json()

# convert the object into a dict
fcpm_v2_compute_pool_list_metadata_dict = fcpm_v2_compute_pool_list_metadata_instance.to_dict()
# create an instance of FcpmV2ComputePoolListMetadata from a dict
fcpm_v2_compute_pool_list_metadata_form_dict = fcpm_v2_compute_pool_list_metadata.from_dict(fcpm_v2_compute_pool_list_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


