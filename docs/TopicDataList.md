# TopicDataList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceCollectionMetadata**](ResourceCollectionMetadata.md) |  | 
**data** | [**List[TopicData]**](TopicData.md) |  | 

## Example

```python
from openapi_client.models.topic_data_list import TopicDataList

# TODO update the JSON string below
json = "{}"
# create an instance of TopicDataList from a JSON string
topic_data_list_instance = TopicDataList.from_json(json)
# print the JSON string representation of the object
print TopicDataList.to_json()

# convert the object into a dict
topic_data_list_dict = topic_data_list_instance.to_dict()
# create an instance of TopicDataList from a dict
topic_data_list_form_dict = topic_data_list.from_dict(topic_data_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


