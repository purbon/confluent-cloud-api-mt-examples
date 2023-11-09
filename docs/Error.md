# Error

Describes a particular error encountered while performing an operation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for this particular occurrence of the problem. | [optional] 
**status** | **str** | The HTTP status code applicable to this problem, expressed as a string value. | [optional] 
**code** | **str** | An application-specific error code, expressed as a string value. | [optional] 
**title** | **str** | A short, human-readable summary of the problem. It **SHOULD NOT** change from occurrence to occurrence of the problem, except for purposes of localization. | [optional] 
**detail** | **str** | A human-readable explanation specific to this occurrence of the problem. | [optional] 
**source** | [**ErrorSource**](ErrorSource.md) |  | [optional] 
**error_code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print Error.to_json()

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_form_dict = error.from_dict(error_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


