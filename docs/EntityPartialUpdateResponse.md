# EntityPartialUpdateResponse

The type name

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mutated_entities** | [**EntityPartialUpdate**](EntityPartialUpdate.md) |  | [optional] 

## Example

```python
from openapi_client.models.entity_partial_update_response import EntityPartialUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntityPartialUpdateResponse from a JSON string
entity_partial_update_response_instance = EntityPartialUpdateResponse.from_json(json)
# print the JSON string representation of the object
print EntityPartialUpdateResponse.to_json()

# convert the object into a dict
entity_partial_update_response_dict = entity_partial_update_response_instance.to_dict()
# create an instance of EntityPartialUpdateResponse from a dict
entity_partial_update_response_form_dict = entity_partial_update_response.from_dict(entity_partial_update_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


