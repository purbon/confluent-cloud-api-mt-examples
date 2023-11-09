# SchemaReference

Schema reference

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Reference name | [optional] 
**subject** | **str** | Name of the referenced subject | [optional] 
**version** | **int** | Version number of the referenced subject | [optional] 

## Example

```python
from openapi_client.models.schema_reference import SchemaReference

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaReference from a JSON string
schema_reference_instance = SchemaReference.from_json(json)
# print the JSON string representation of the object
print SchemaReference.to_json()

# convert the object into a dict
schema_reference_dict = schema_reference_instance.to_dict()
# create an instance of SchemaReference from a dict
schema_reference_form_dict = schema_reference.from_dict(schema_reference_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


