# ExporterResponse

Exporter register response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the exporter | [optional] 

## Example

```python
from openapi_client.models.exporter_response import ExporterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExporterResponse from a JSON string
exporter_response_instance = ExporterResponse.from_json(json)
# print the JSON string representation of the object
print ExporterResponse.to_json()

# convert the object into a dict
exporter_response_dict = exporter_response_instance.to_dict()
# create an instance of ExporterResponse from a dict
exporter_response_form_dict = exporter_response.from_dict(exporter_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


