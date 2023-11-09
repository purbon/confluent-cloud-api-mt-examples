# SdV1PipelineStatus

The status of the Pipeline

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The current state of the pipeline.:   DRAFT:  the pipeline is a draft and not activated yet;   ACTIVATING:  the pipeline activation is in progress;   DEACTIVATING:  the pipeline deactivation is in progress;   ACTIVE:  the pipeline is actived and running;   FAILED:  the pipeline activation or deactivation failed;   DELETED:  the pipeline is deleted  | [optional] [readonly] 
**topic_count** | **int** | The number of Kafka topics defined in the pipeline. | [optional] [readonly] 
**connector_count** | **int** | The number of connectors defined in the pipeline. | [optional] [readonly] 
**query_count** | **int** | The number of KSQL queries defined in the pipeline. | [optional] [readonly] 

## Example

```python
from openapi_client.models.sd_v1_pipeline_status import SdV1PipelineStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SdV1PipelineStatus from a JSON string
sd_v1_pipeline_status_instance = SdV1PipelineStatus.from_json(json)
# print the JSON string representation of the object
print SdV1PipelineStatus.to_json()

# convert the object into a dict
sd_v1_pipeline_status_dict = sd_v1_pipeline_status_instance.to_dict()
# create an instance of SdV1PipelineStatus from a dict
sd_v1_pipeline_status_form_dict = sd_v1_pipeline_status.from_dict(sd_v1_pipeline_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


