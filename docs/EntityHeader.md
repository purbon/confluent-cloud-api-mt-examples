# EntityHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** | The type name | [optional] 
**attributes** | **Dict[str, object]** | The attributes | [optional] 
**guid** | **str** | The internal guid | [optional] 
**status** | **str** | The status | [optional] 
**display_text** | **str** | The display text | [optional] 
**classification_names** | **List[str]** | The classification (tag) names | [optional] 
**classifications** | [**List[Classification]**](Classification.md) | The classifications (tags) | [optional] 
**meaning_names** | **List[str]** | The meaning names | [optional] 
**meanings** | [**List[TermAssignmentHeader]**](TermAssignmentHeader.md) | The meanings | [optional] 
**is_incomplete** | **bool** | Whether is incomplete | [optional] 
**labels** | **List[str]** | The labels | [optional] 

## Example

```python
from openapi_client.models.entity_header import EntityHeader

# TODO update the JSON string below
json = "{}"
# create an instance of EntityHeader from a JSON string
entity_header_instance = EntityHeader.from_json(json)
# print the JSON string representation of the object
print EntityHeader.to_json()

# convert the object into a dict
entity_header_dict = entity_header_instance.to_dict()
# create an instance of EntityHeader from a dict
entity_header_form_dict = entity_header.from_dict(entity_header_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


