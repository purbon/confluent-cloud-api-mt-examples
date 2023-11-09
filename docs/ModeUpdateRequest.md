# ModeUpdateRequest

Mode update request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** | Schema Registry operating mode | [optional] 

## Example

```python
from openapi_client.models.mode_update_request import ModeUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModeUpdateRequest from a JSON string
mode_update_request_instance = ModeUpdateRequest.from_json(json)
# print the JSON string representation of the object
print ModeUpdateRequest.to_json()

# convert the object into a dict
mode_update_request_dict = mode_update_request_instance.to_dict()
# create an instance of ModeUpdateRequest from a dict
mode_update_request_form_dict = mode_update_request.from_dict(mode_update_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


