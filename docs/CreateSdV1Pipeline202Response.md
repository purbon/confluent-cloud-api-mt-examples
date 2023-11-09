# CreateSdV1Pipeline202Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**SdV1PipelineMetadata**](SdV1PipelineMetadata.md) |  | [optional] 
**spec** | [**ListSdV1Pipelines200ResponseAllOfDataInnerSpec**](ListSdV1Pipelines200ResponseAllOfDataInnerSpec.md) |  | 
**status** | [**SdV1PipelineStatus**](SdV1PipelineStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_sd_v1_pipeline202_response import CreateSdV1Pipeline202Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSdV1Pipeline202Response from a JSON string
create_sd_v1_pipeline202_response_instance = CreateSdV1Pipeline202Response.from_json(json)
# print the JSON string representation of the object
print CreateSdV1Pipeline202Response.to_json()

# convert the object into a dict
create_sd_v1_pipeline202_response_dict = create_sd_v1_pipeline202_response_instance.to_dict()
# create an instance of CreateSdV1Pipeline202Response from a dict
create_sd_v1_pipeline202_response_form_dict = create_sd_v1_pipeline202_response.from_dict(create_sd_v1_pipeline202_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


