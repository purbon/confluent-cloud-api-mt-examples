# SearchResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_parameters** | [**SearchParams**](SearchParams.md) |  | [optional] 
**types** | **List[str]** | The types | [optional] 
**entities** | [**List[EntityHeader]**](EntityHeader.md) | The entities | [optional] 
**referred_entities** | [**Dict[str, EntityHeader]**](EntityHeader.md) | The referred entities | [optional] 

## Example

```python
from openapi_client.models.search_result import SearchResult

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResult from a JSON string
search_result_instance = SearchResult.from_json(json)
# print the JSON string representation of the object
print SearchResult.to_json()

# convert the object into a dict
search_result_dict = search_result_instance.to_dict()
# create an instance of SearchResult from a dict
search_result_form_dict = search_result.from_dict(search_result_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


