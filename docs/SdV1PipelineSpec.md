# SdV1PipelineSpec

The desired state of the Pipeline

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the pipeline. | [optional] 
**description** | **str** | The description of the pipeline. | [optional] 
**retained_topic_names** | **List[str]** | A list of Kafka topic names from the activated pipeline to be retained when this pipeline is deactivated.  | [optional] 
**activated** | **bool** | The desired state of the pipeline. | [optional] [default to False]
**activation_privilege** | **bool** | Whether the pipeline has privileges to be activated. | [optional] [default to False]
**source_code** | [**SdV1SourceCodeObject**](SdV1SourceCodeObject.md) |  | [optional] 
**secrets** | **Dict[str, str]** | A map of secrets used in the pipeline source code. | [optional] 
**environment** | [**ObjectReference**](ObjectReference.md) |  | [optional] 
**kafka_cluster** | [**ObjectReference**](ObjectReference.md) |  | [optional] 
**ksql_cluster** | [**ObjectReference**](ObjectReference.md) |  | [optional] 
**stream_governance_cluster** | [**ObjectReference**](ObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.sd_v1_pipeline_spec import SdV1PipelineSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SdV1PipelineSpec from a JSON string
sd_v1_pipeline_spec_instance = SdV1PipelineSpec.from_json(json)
# print the JSON string representation of the object
print SdV1PipelineSpec.to_json()

# convert the object into a dict
sd_v1_pipeline_spec_dict = sd_v1_pipeline_spec_instance.to_dict()
# create an instance of SdV1PipelineSpec from a dict
sd_v1_pipeline_spec_form_dict = sd_v1_pipeline_spec.from_dict(sd_v1_pipeline_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


