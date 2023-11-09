# RegisterExporterRequest

Exporter register request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**references** | [**List[ExporterReference]**](ExporterReference.md) | References to other schemas | [optional] 

## Example

```python
from openapi_client.models.register_exporter_request import RegisterExporterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterExporterRequest from a JSON string
register_exporter_request_instance = RegisterExporterRequest.from_json(json)
# print the JSON string representation of the object
print RegisterExporterRequest.to_json()

# convert the object into a dict
register_exporter_request_dict = register_exporter_request_instance.to_dict()
# create an instance of RegisterExporterRequest from a dict
register_exporter_request_form_dict = register_exporter_request.from_dict(register_exporter_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


