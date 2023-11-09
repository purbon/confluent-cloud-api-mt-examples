# RegisterSchemaRequest

Schema register request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | Version number | [optional] 
**id** | **int** | Globally unique identifier of the schema | [optional] 
**schema_type** | **str** | Schema type | [optional] 
**references** | [**List[SchemaReference]**](SchemaReference.md) | References to other schemas | [optional] 
**var_schema** | **str** | Schema definition string | [optional] 

## Example

```python
from openapi_client.models.register_schema_request import RegisterSchemaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterSchemaRequest from a JSON string
register_schema_request_instance = RegisterSchemaRequest.from_json(json)
# print the JSON string representation of the object
print RegisterSchemaRequest.to_json()

# convert the object into a dict
register_schema_request_dict = register_schema_request_instance.to_dict()
# create an instance of RegisterSchemaRequest from a dict
register_schema_request_form_dict = register_schema_request.from_dict(register_schema_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


