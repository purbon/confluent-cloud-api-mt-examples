# EntityWithExtInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referred_entities** | [**Dict[str, Entity]**](Entity.md) | The referred entities | [optional] 
**entity** | [**Entity**](Entity.md) |  | [optional] 

## Example

```python
from openapi_client.models.entity_with_ext_info import EntityWithExtInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EntityWithExtInfo from a JSON string
entity_with_ext_info_instance = EntityWithExtInfo.from_json(json)
# print the JSON string representation of the object
print EntityWithExtInfo.to_json()

# convert the object into a dict
entity_with_ext_info_dict = entity_with_ext_info_instance.to_dict()
# create an instance of EntityWithExtInfo from a dict
entity_with_ext_info_form_dict = entity_with_ext_info.from_dict(entity_with_ext_info_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


