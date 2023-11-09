# ListSdV1Pipelines200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**SdV1PipelineListMetadata**](SdV1PipelineListMetadata.md) |  | 
**data** | [**List[ListSdV1Pipelines200ResponseAllOfDataInner]**](ListSdV1Pipelines200ResponseAllOfDataInner.md) |  | 

## Example

```python
from openapi_client.models.list_sd_v1_pipelines200_response import ListSdV1Pipelines200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSdV1Pipelines200Response from a JSON string
list_sd_v1_pipelines200_response_instance = ListSdV1Pipelines200Response.from_json(json)
# print the JSON string representation of the object
print ListSdV1Pipelines200Response.to_json()

# convert the object into a dict
list_sd_v1_pipelines200_response_dict = list_sd_v1_pipelines200_response_instance.to_dict()
# create an instance of ListSdV1Pipelines200Response from a dict
list_sd_v1_pipelines200_response_form_dict = list_sd_v1_pipelines200_response.from_dict(list_sd_v1_pipelines200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


