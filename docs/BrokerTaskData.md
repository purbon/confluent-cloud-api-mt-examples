# BrokerTaskData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**broker_id** | **int** |  | 
**task_type** | [**BrokerTaskType**](BrokerTaskType.md) |  | 
**task_status** | **str** |  | 
**shutdown_scheduled** | **bool** |  | [optional] 
**sub_task_statuses** | **Dict[str, str]** |  | 
**created_at** | **datetime** | The date and time at which this task was created. | [readonly] 
**updated_at** | **datetime** | The date and time at which this task was last updated. | [readonly] 
**error_code** | **int** |  | [optional] 
**error_message** | **str** |  | [optional] 
**broker** | [**Relationship**](Relationship.md) |  | 

## Example

```python
from openapi_client.models.broker_task_data import BrokerTaskData

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerTaskData from a JSON string
broker_task_data_instance = BrokerTaskData.from_json(json)
# print the JSON string representation of the object
print BrokerTaskData.to_json()

# convert the object into a dict
broker_task_data_dict = broker_task_data_instance.to_dict()
# create an instance of BrokerTaskData from a dict
broker_task_data_form_dict = broker_task_data.from_dict(broker_task_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


