# TermAssignmentHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term_guid** | **str** | The term guid | [optional] 
**relation_guid** | **str** | The relation guid | [optional] 
**description** | **str** | The description | [optional] 
**display_text** | **str** | The display text | [optional] 
**expression** | **str** | The expression | [optional] 
**created_by** | **str** | The creator | [optional] 
**steward** | **str** | The steward | [optional] 
**source** | **str** | The source | [optional] 
**confidence** | **int** | The confidence | [optional] 
**status** | **str** | The status | [optional] 

## Example

```python
from openapi_client.models.term_assignment_header import TermAssignmentHeader

# TODO update the JSON string below
json = "{}"
# create an instance of TermAssignmentHeader from a JSON string
term_assignment_header_instance = TermAssignmentHeader.from_json(json)
# print the JSON string representation of the object
print TermAssignmentHeader.to_json()

# convert the object into a dict
term_assignment_header_dict = term_assignment_header_instance.to_dict()
# create an instance of TermAssignmentHeader from a dict
term_assignment_header_form_dict = term_assignment_header.from_dict(term_assignment_header_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


