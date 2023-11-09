# CreateMirrorTopicRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_topic_name** | **str** |  | 
**mirror_topic_name** | **str** |  | [optional] 
**replication_factor** | **int** |  | [optional] 
**configs** | [**List[ConfigData]**](ConfigData.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_mirror_topic_request_data import CreateMirrorTopicRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMirrorTopicRequestData from a JSON string
create_mirror_topic_request_data_instance = CreateMirrorTopicRequestData.from_json(json)
# print the JSON string representation of the object
print CreateMirrorTopicRequestData.to_json()

# convert the object into a dict
create_mirror_topic_request_data_dict = create_mirror_topic_request_data_instance.to_dict()
# create an instance of CreateMirrorTopicRequestData from a dict
create_mirror_topic_request_data_form_dict = create_mirror_topic_request_data.from_dict(create_mirror_topic_request_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


