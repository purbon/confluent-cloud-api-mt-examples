# CompatibilityCheckResponse

Compatibility check response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_compatible** | **bool** | Whether the compared schemas are compatible | [optional] 
**messages** | **List[str]** | Error messages | [optional] 

## Example

```python
from openapi_client.models.compatibility_check_response import CompatibilityCheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompatibilityCheckResponse from a JSON string
compatibility_check_response_instance = CompatibilityCheckResponse.from_json(json)
# print the JSON string representation of the object
print CompatibilityCheckResponse.to_json()

# convert the object into a dict
compatibility_check_response_dict = compatibility_check_response_instance.to_dict()
# create an instance of CompatibilityCheckResponse from a dict
compatibility_check_response_form_dict = compatibility_check_response.from_dict(compatibility_check_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


