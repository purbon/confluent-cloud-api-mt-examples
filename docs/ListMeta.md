# ListMeta

ListMeta describes metadata that resource collections may have

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** | A link to the first page of results. If a response does not contain a first link, then direct navigation to the first page is not supported. | [optional] 
**last** | **str** | A link to the last page of results. If a response does not contain a last link, then direct navigation to the last page is not supported. | [optional] 
**prev** | **str** | A link to the previous page of results. If a response does not contain a prev link, then either there is no previous data or backwards traversal through the result set is not supported. | [optional] 
**next** | **str** | A link to the next page of results. If a response does not contain a next link, then there is no more data available. | [optional] 
**total_size** | **int** | Number of records in the full result set. This response may be paginated and have a smaller number of records. | [optional] 

## Example

```python
from openapi_client.models.list_meta import ListMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ListMeta from a JSON string
list_meta_instance = ListMeta.from_json(json)
# print the JSON string representation of the object
print ListMeta.to_json()

# convert the object into a dict
list_meta_dict = list_meta_instance.to_dict()
# create an instance of ListMeta from a dict
list_meta_form_dict = list_meta.from_dict(list_meta_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


