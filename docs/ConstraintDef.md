# ConstraintDef


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type | [optional] 
**params** | **Dict[str, object]** | The params | [optional] 

## Example

```python
from openapi_client.models.constraint_def import ConstraintDef

# TODO update the JSON string below
json = "{}"
# create an instance of ConstraintDef from a JSON string
constraint_def_instance = ConstraintDef.from_json(json)
# print the JSON string representation of the object
print ConstraintDef.to_json()

# convert the object into a dict
constraint_def_dict = constraint_def_instance.to_dict()
# create an instance of ConstraintDef from a dict
constraint_def_form_dict = constraint_def.from_dict(constraint_def_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


