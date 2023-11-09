# CreateSdV1PipelineRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**SdV1PipelineMetadata**](SdV1PipelineMetadata.md) |  | [optional] 
**spec** | [**CreateSdV1PipelineRequestAllOfSpec**](CreateSdV1PipelineRequestAllOfSpec.md) |  | 
**status** | [**SdV1PipelineStatus**](SdV1PipelineStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_sd_v1_pipeline_request import CreateSdV1PipelineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSdV1PipelineRequest from a JSON string
create_sd_v1_pipeline_request_instance = CreateSdV1PipelineRequest.from_json(json)
# print the JSON string representation of the object
print CreateSdV1PipelineRequest.to_json()

# convert the object into a dict
create_sd_v1_pipeline_request_dict = create_sd_v1_pipeline_request_instance.to_dict()
# create an instance of CreateSdV1PipelineRequest from a dict
create_sd_v1_pipeline_request_form_dict = create_sd_v1_pipeline_request.from_dict(create_sd_v1_pipeline_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


