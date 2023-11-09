# ClassificationHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** | The tag name | [optional] 
**entity_guid** | **str** | The internal entity guid | [optional] 
**entity_status** | **str** | The entity status | [optional] 
**propagate** | **bool** | Whether to propagate the tag | [optional] 
**remove_propagations_on_entity_delete** | **bool** | Whether to remove propagations on entity delete | [optional] 

## Example

```python
from openapi_client.models.classification_header import ClassificationHeader

# TODO update the JSON string below
json = "{}"
# create an instance of ClassificationHeader from a JSON string
classification_header_instance = ClassificationHeader.from_json(json)
# print the JSON string representation of the object
print ClassificationHeader.to_json()

# convert the object into a dict
classification_header_dict = classification_header_instance.to_dict()
# create an instance of ClassificationHeader from a dict
classification_header_form_dict = classification_header.from_dict(classification_header_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


