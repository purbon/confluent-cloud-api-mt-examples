# TagDef


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The category | [optional] 
**guid** | **str** | The internal guid | [optional] 
**created_by** | **str** | The creator | [optional] 
**updated_by** | **str** | The updater | [optional] 
**create_time** | **int** | The create time | [optional] 
**update_time** | **int** | The update time | [optional] 
**version** | **int** | The version | [optional] 
**name** | **str** | The name | [optional] 
**description** | **str** | The description | [optional] 
**type_version** | **str** | The type version | [optional] 
**service_type** | **str** | The service type | [optional] 
**options** | **Dict[str, str]** | The options | [optional] 
**attribute_defs** | [**List[AttributeDef]**](AttributeDef.md) | The attribute definitions | [optional] 
**super_types** | **List[str]** | The supertypes | [optional] 
**entity_types** | **List[str]** | The entity types | [optional] 
**sub_types** | **List[str]** | The subtypes | [optional] 

## Example

```python
from openapi_client.models.tag_def import TagDef

# TODO update the JSON string below
json = "{}"
# create an instance of TagDef from a JSON string
tag_def_instance = TagDef.from_json(json)
# print the JSON string representation of the object
print TagDef.to_json()

# convert the object into a dict
tag_def_dict = tag_def_instance.to_dict()
# create an instance of TagDef from a dict
tag_def_form_dict = tag_def.from_dict(tag_def_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


