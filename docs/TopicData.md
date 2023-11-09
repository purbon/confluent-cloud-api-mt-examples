# TopicData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**topic_name** | **str** |  | 
**is_internal** | **bool** |  | 
**replication_factor** | **int** |  | 
**partitions_count** | **int** |  | 
**partitions** | [**Relationship**](Relationship.md) |  | 
**configs** | [**Relationship**](Relationship.md) |  | 
**partition_reassignments** | [**Relationship**](Relationship.md) |  | 
**authorized_operations** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.topic_data import TopicData

# TODO update the JSON string below
json = "{}"
# create an instance of TopicData from a JSON string
topic_data_instance = TopicData.from_json(json)
# print the JSON string representation of the object
print TopicData.to_json()

# convert the object into a dict
topic_data_dict = topic_data_instance.to_dict()
# create an instance of TopicData from a dict
topic_data_form_dict = topic_data.from_dict(topic_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


