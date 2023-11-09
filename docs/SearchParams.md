# SearchParams

Search paramas to filter results

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_deleted** | **bool** | Whether to include deleted | [optional] 
**limit** | **int** | The limit | [optional] 
**offset** | **int** | The offset | [optional] 

## Example

```python
from openapi_client.models.search_params import SearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of SearchParams from a JSON string
search_params_instance = SearchParams.from_json(json)
# print the JSON string representation of the object
print SearchParams.to_json()

# convert the object into a dict
search_params_dict = search_params_instance.to_dict()
# create an instance of SearchParams from a dict
search_params_form_dict = search_params.from_dict(search_params_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


