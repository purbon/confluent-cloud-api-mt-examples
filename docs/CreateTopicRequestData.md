# CreateTopicRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic_name** | **str** |  | 
**partitions_count** | **int** |  | [optional] 
**replication_factor** | **int** |  | [optional] 
**configs** | [**List[CreateTopicRequestDataConfigsInner]**](CreateTopicRequestDataConfigsInner.md) |  | [optional] 
**validate_only** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.create_topic_request_data import CreateTopicRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTopicRequestData from a JSON string
create_topic_request_data_instance = CreateTopicRequestData.from_json(json)
# print the JSON string representation of the object
print CreateTopicRequestData.to_json()

# convert the object into a dict
create_topic_request_data_dict = create_topic_request_data_instance.to_dict()
# create an instance of CreateTopicRequestData from a dict
create_topic_request_data_form_dict = create_topic_request_data.from_dict(create_topic_request_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


