# ModelSchema

Schema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Name of the subject | [optional] 
**version** | **int** | Version number | [optional] 
**id** | **int** | Globally unique identifier of the schema | [optional] 
**schema_type** | **str** | Schema type | [optional] 
**references** | [**List[SchemaReference]**](SchemaReference.md) | References to other schemas | [optional] 
**var_schema** | **str** | Schema definition string | [optional] 

## Example

```python
from openapi_client.models.model_schema import ModelSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSchema from a JSON string
model_schema_instance = ModelSchema.from_json(json)
# print the JSON string representation of the object
print ModelSchema.to_json()

# convert the object into a dict
model_schema_dict = model_schema_instance.to_dict()
# create an instance of ModelSchema from a dict
model_schema_form_dict = model_schema.from_dict(model_schema_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


