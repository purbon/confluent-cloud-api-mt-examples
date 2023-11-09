# ExporterStatusResponse

Exporter status get request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of exporter. | [optional] 
**state** | **str** | State of the exporter. Could be STARTING, RUNNING or PAUSED | [optional] 
**offset** | **int** | Offset of the exporter | [optional] 
**ts** | **int** | Timestamp of the exporter | [optional] 
**trace** | **str** | Error trace of the exporter | [optional] 

## Example

```python
from openapi_client.models.exporter_status_response import ExporterStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExporterStatusResponse from a JSON string
exporter_status_response_instance = ExporterStatusResponse.from_json(json)
# print the JSON string representation of the object
print ExporterStatusResponse.to_json()

# convert the object into a dict
exporter_status_response_dict = exporter_status_response_instance.to_dict()
# create an instance of ExporterStatusResponse from a dict
exporter_status_response_form_dict = exporter_status_response.from_dict(exporter_status_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


