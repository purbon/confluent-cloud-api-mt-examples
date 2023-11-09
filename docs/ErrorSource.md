# ErrorSource

If this error was caused by a particular part of the API request, the source will point to the query string parameter or request body property that caused it.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pointer** | **str** | A JSON Pointer [RFC6901] to the associated entity in the request document [e.g. \&quot;/spec\&quot; for a spec object, or \&quot;/spec/title\&quot; for a specific field]. | [optional] 
**parameter** | **str** | A string indicating which query parameter caused the error. | [optional] 

## Example

```python
from openapi_client.models.error_source import ErrorSource

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorSource from a JSON string
error_source_instance = ErrorSource.from_json(json)
# print the JSON string representation of the object
print ErrorSource.to_json()

# convert the object into a dict
error_source_dict = error_source_instance.to_dict()
# create an instance of ErrorSource from a dict
error_source_form_dict = error_source.from_dict(error_source_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


