# Entity

The entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** | The type name | [optional] 
**attributes** | **object** | The type attributes | [optional] 
**guid** | **str** | The internal guid | [optional] 
**home_id** | **str** | The home id | [optional] 
**is_proxy** | **bool** | Whether is a proxy | [optional] 
**is_incomplete** | **bool** | Whether is incomplete | [optional] 
**provenance_type** | **int** | The provenance type | [optional] 
**status** | **str** | The status | [optional] 
**created_by** | **str** | The creator | [optional] 
**updated_by** | **str** | The updater | [optional] 
**create_time** | **int** | The create time | [optional] 
**update_time** | **int** | The update time | [optional] 
**version** | **int** | The version | [optional] 
**relationship_attributes** | **object** | The relationship attributes | [optional] 
**classifications** | [**List[Classification]**](Classification.md) | The classifications (tags) | [optional] 
**meanings** | [**List[TermAssignmentHeader]**](TermAssignmentHeader.md) | The meanings | [optional] 
**custom_attributes** | **Dict[str, str]** | The custom attributes | [optional] 
**business_attributes** | **Dict[str, object]** | The business attributes | [optional] 
**labels** | **List[str]** | The labels | [optional] 
**proxy** | **bool** | Whether is a proxy | [optional] 

## Example

```python
from openapi_client.models.entity import Entity

# TODO update the JSON string below
json = "{}"
# create an instance of Entity from a JSON string
entity_instance = Entity.from_json(json)
# print the JSON string representation of the object
print Entity.to_json()

# convert the object into a dict
entity_dict = entity_instance.to_dict()
# create an instance of Entity from a dict
entity_form_dict = entity.from_dict(entity_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


