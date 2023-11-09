# SdV1PipelineMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **object** |  | 
**resource_name** | **object** |  | [optional] 
**created_at** | **datetime** | The date and time at which this object was created. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**updated_at** | **datetime** | The date and time at which this object was last updated. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**deleted_at** | **datetime** | The date and time at which this object was (or will be) deleted. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 

## Example

```python
from openapi_client.models.sd_v1_pipeline_metadata import SdV1PipelineMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SdV1PipelineMetadata from a JSON string
sd_v1_pipeline_metadata_instance = SdV1PipelineMetadata.from_json(json)
# print the JSON string representation of the object
print SdV1PipelineMetadata.to_json()

# convert the object into a dict
sd_v1_pipeline_metadata_dict = sd_v1_pipeline_metadata_instance.to_dict()
# create an instance of SdV1PipelineMetadata from a dict
sd_v1_pipeline_metadata_form_dict = sd_v1_pipeline_metadata.from_dict(sd_v1_pipeline_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


