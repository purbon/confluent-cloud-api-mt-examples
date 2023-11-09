# RemoveBrokerTaskData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**broker_id** | **int** |  | 
**shutdown_scheduled** | **bool** |  | 
**broker_replica_exclusion_status** | **str** |  | 
**partition_reassignment_status** | **str** |  | 
**broker_shutdown_status** | **str** |  | 
**error_code** | **int** |  | [optional] 
**error_message** | **str** |  | [optional] 
**broker** | [**Relationship**](Relationship.md) |  | 

## Example

```python
from openapi_client.models.remove_broker_task_data import RemoveBrokerTaskData

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveBrokerTaskData from a JSON string
remove_broker_task_data_instance = RemoveBrokerTaskData.from_json(json)
# print the JSON string representation of the object
print RemoveBrokerTaskData.to_json()

# convert the object into a dict
remove_broker_task_data_dict = remove_broker_task_data_instance.to_dict()
# create an instance of RemoveBrokerTaskData from a dict
remove_broker_task_data_form_dict = remove_broker_task_data.from_dict(remove_broker_task_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


