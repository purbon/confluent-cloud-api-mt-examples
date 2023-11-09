# SdV1PipelineListMetadata


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
from openapi_client.models.sd_v1_pipeline_list_metadata import SdV1PipelineListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SdV1PipelineListMetadata from a JSON string
sd_v1_pipeline_list_metadata_instance = SdV1PipelineListMetadata.from_json(json)
# print the JSON string representation of the object
print SdV1PipelineListMetadata.to_json()

# convert the object into a dict
sd_v1_pipeline_list_metadata_dict = sd_v1_pipeline_list_metadata_instance.to_dict()
# create an instance of SdV1PipelineListMetadata from a dict
sd_v1_pipeline_list_metadata_form_dict = sd_v1_pipeline_list_metadata.from_dict(sd_v1_pipeline_list_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


