# SchemaString

Schema definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_type** | **str** | Schema type | [optional] 
**var_schema** | **str** | Schema string identified by the ID | [optional] 
**references** | [**List[SchemaReference]**](SchemaReference.md) | References to other schemas | [optional] 
**max_id** | **int** | Maximum ID | [optional] 

## Example

```python
from openapi_client.models.schema_string import SchemaString

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaString from a JSON string
schema_string_instance = SchemaString.from_json(json)
# print the JSON string representation of the object
print SchemaString.to_json()

# convert the object into a dict
schema_string_dict = schema_string_instance.to_dict()
# create an instance of SchemaString from a dict
schema_string_form_dict = schema_string.from_dict(schema_string_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


