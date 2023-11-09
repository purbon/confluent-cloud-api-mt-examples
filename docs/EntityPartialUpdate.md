# EntityPartialUpdate

The updated entities.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update** | [**List[PartialUpdateParams]**](PartialUpdateParams.md) | The updated entities. | [optional] 

## Example

```python
from openapi_client.models.entity_partial_update import EntityPartialUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EntityPartialUpdate from a JSON string
entity_partial_update_instance = EntityPartialUpdate.from_json(json)
# print the JSON string representation of the object
print EntityPartialUpdate.to_json()

# convert the object into a dict
entity_partial_update_dict = entity_partial_update_instance.to_dict()
# create an instance of EntityPartialUpdate from a dict
entity_partial_update_form_dict = entity_partial_update.from_dict(entity_partial_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


