# TagResponse


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
**error** | [**ErrorMessage**](ErrorMessage.md) |  | [optional] 

## Example

```python
from openapi_client.models.tag_response import TagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TagResponse from a JSON string
tag_response_instance = TagResponse.from_json(json)
# print the JSON string representation of the object
print TagResponse.to_json()

# convert the object into a dict
tag_response_dict = tag_response_instance.to_dict()
# create an instance of TagResponse from a dict
tag_response_form_dict = tag_response.from_dict(tag_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


