# Tag


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** | The tag name | [optional] 
**attributes** | **object** | The tag attributes | [optional] 
**entity_guid** | **str** | The internal entity guid | [optional] 
**entity_status** | **str** | The entity status | [optional] 
**propagate** | **bool** | Whether to propagate the tag | [optional] 
**validity_periods** | [**List[TimeBoundary]**](TimeBoundary.md) | The validity periods | [optional] 
**remove_propagations_on_entity_delete** | **bool** | Whether to remove propagations on entity delete | [optional] 
**entity_type** | **str** | The entity type | [optional] 
**entity_name** | **str** | The qualified name of the entity | [optional] 

## Example

```python
from openapi_client.models.tag import Tag

# TODO update the JSON string below
json = "{}"
# create an instance of Tag from a JSON string
tag_instance = Tag.from_json(json)
# print the JSON string representation of the object
print Tag.to_json()

# convert the object into a dict
tag_dict = tag_instance.to_dict()
# create an instance of Tag from a dict
tag_form_dict = tag.from_dict(tag_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


