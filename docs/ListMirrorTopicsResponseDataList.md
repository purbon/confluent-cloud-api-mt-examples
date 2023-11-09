# ListMirrorTopicsResponseDataList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceCollectionMetadata**](ResourceCollectionMetadata.md) |  | 
**data** | [**List[ListMirrorTopicsResponseData]**](ListMirrorTopicsResponseData.md) |  | 

## Example

```python
from openapi_client.models.list_mirror_topics_response_data_list import ListMirrorTopicsResponseDataList

# TODO update the JSON string below
json = "{}"
# create an instance of ListMirrorTopicsResponseDataList from a JSON string
list_mirror_topics_response_data_list_instance = ListMirrorTopicsResponseDataList.from_json(json)
# print the JSON string representation of the object
print ListMirrorTopicsResponseDataList.to_json()

# convert the object into a dict
list_mirror_topics_response_data_list_dict = list_mirror_topics_response_data_list_instance.to_dict()
# create an instance of ListMirrorTopicsResponseDataList from a dict
list_mirror_topics_response_data_list_form_dict = list_mirror_topics_response_data_list.from_dict(list_mirror_topics_response_data_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


