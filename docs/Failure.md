# Failure

Provides information about problems encountered while performing an operation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[Error]**](Error.md) | List of errors which caused this operation to fail | 

## Example

```python
from openapi_client.models.failure import Failure

# TODO update the JSON string below
json = "{}"
# create an instance of Failure from a JSON string
failure_instance = Failure.from_json(json)
# print the JSON string representation of the object
print Failure.to_json()

# convert the object into a dict
failure_dict = failure_instance.to_dict()
# create an instance of Failure from a dict
failure_form_dict = failure.from_dict(failure_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


