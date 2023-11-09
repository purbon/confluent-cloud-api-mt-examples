# RegisterSchemaResponse

Schema register response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Globally unique identifier of the schema | [optional] 

## Example

```python
from openapi_client.models.register_schema_response import RegisterSchemaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterSchemaResponse from a JSON string
register_schema_response_instance = RegisterSchemaResponse.from_json(json)
# print the JSON string representation of the object
print RegisterSchemaResponse.to_json()

# convert the object into a dict
register_schema_response_dict = register_schema_response_instance.to_dict()
# create an instance of RegisterSchemaResponse from a dict
register_schema_response_form_dict = register_schema_response.from_dict(register_schema_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


