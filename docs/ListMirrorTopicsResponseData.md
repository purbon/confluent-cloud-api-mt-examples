# ListMirrorTopicsResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**link_name** | **str** |  | 
**mirror_topic_name** | **str** |  | 
**source_topic_name** | **str** |  | 
**num_partitions** | **int** |  | 
**mirror_lags** | [**List[MirrorLag]**](MirrorLag.md) |  | 
**mirror_status** | [**MirrorTopicStatus**](MirrorTopicStatus.md) |  | 
**state_time_ms** | **int** |  | 

## Example

```python
from openapi_client.models.list_mirror_topics_response_data import ListMirrorTopicsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListMirrorTopicsResponseData from a JSON string
list_mirror_topics_response_data_instance = ListMirrorTopicsResponseData.from_json(json)
# print the JSON string representation of the object
print ListMirrorTopicsResponseData.to_json()

# convert the object into a dict
list_mirror_topics_response_data_dict = list_mirror_topics_response_data_instance.to_dict()
# create an instance of ListMirrorTopicsResponseData from a dict
list_mirror_topics_response_data_form_dict = list_mirror_topics_response_data.from_dict(list_mirror_topics_response_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


