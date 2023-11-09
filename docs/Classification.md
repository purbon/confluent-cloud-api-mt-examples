# Classification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** | The tag name | [optional] 
**attributes** | **Dict[str, object]** | The tag attributes | [optional] 
**entity_guid** | **str** | The internal entity guid | [optional] 
**entity_status** | **str** | The entity status | [optional] 
**propagate** | **bool** | Whether to propagate the tag | [optional] 
**validity_periods** | [**List[TimeBoundary]**](TimeBoundary.md) | The validity periods | [optional] 
**remove_propagations_on_entity_delete** | **bool** | Whether to remove propagations on entity delete | [optional] 

## Example

```python
from openapi_client.models.classification import Classification

# TODO update the JSON string below
json = "{}"
# create an instance of Classification from a JSON string
classification_instance = Classification.from_json(json)
# print the JSON string representation of the object
print Classification.to_json()

# convert the object into a dict
classification_dict = classification_instance.to_dict()
# create an instance of Classification from a dict
classification_form_dict = classification.from_dict(classification_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


