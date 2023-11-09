# PartialUpdateParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** | The type name | [optional] 
**attributes** | **object** | The attributes | [optional] 
**guid** | **str** | The internal guid | [optional] 
**status** | **str** | The status | [optional] 
**classification_names** | **List[str]** | The classification (tag) names | [optional] 
**classifications** | [**List[ClassificationHeader]**](ClassificationHeader.md) | The classifications (tags) | [optional] 
**is_incomplete** | **bool** | Whether is incomplete | [optional] 

## Example

```python
from openapi_client.models.partial_update_params import PartialUpdateParams

# TODO update the JSON string below
json = "{}"
# create an instance of PartialUpdateParams from a JSON string
partial_update_params_instance = PartialUpdateParams.from_json(json)
# print the JSON string representation of the object
print PartialUpdateParams.to_json()

# convert the object into a dict
partial_update_params_dict = partial_update_params_instance.to_dict()
# create an instance of PartialUpdateParams from a dict
partial_update_params_form_dict = partial_update_params.from_dict(partial_update_params_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


