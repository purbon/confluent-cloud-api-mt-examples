# AttributeDef


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name | [optional] 
**type_name** | **str** | The type name | [optional] 
**is_optional** | **bool** | Whether is optional | [optional] 
**cardinality** | **str** | The cardinality | [optional] 
**values_min_count** | **int** | The values min count | [optional] 
**values_max_count** | **int** | The values max count | [optional] 
**is_unique** | **bool** | Whether is unique | [optional] 
**is_indexable** | **bool** | Whether is indexable | [optional] 
**include_in_notification** | **bool** | Whether to include in notifications | [optional] 
**default_value** | **str** | The default value | [optional] 
**description** | **str** | The description | [optional] 
**search_weight** | **int** | The search weight | [optional] 
**index_type** | **str** | The index type | [optional] 
**constraints** | [**List[ConstraintDef]**](ConstraintDef.md) | The constraints | [optional] 
**options** | **Dict[str, str]** | The options | [optional] 
**display_name** | **str** | The display name | [optional] 

## Example

```python
from openapi_client.models.attribute_def import AttributeDef

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeDef from a JSON string
attribute_def_instance = AttributeDef.from_json(json)
# print the JSON string representation of the object
print AttributeDef.to_json()

# convert the object into a dict
attribute_def_dict = attribute_def_instance.to_dict()
# create an instance of AttributeDef from a dict
attribute_def_form_dict = attribute_def.from_dict(attribute_def_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


