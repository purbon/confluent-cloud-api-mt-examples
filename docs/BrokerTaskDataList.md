# BrokerTaskDataList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceCollectionMetadata**](ResourceCollectionMetadata.md) |  | 
**data** | [**List[BrokerTaskData]**](BrokerTaskData.md) |  | 

## Example

```python
from openapi_client.models.broker_task_data_list import BrokerTaskDataList

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerTaskDataList from a JSON string
broker_task_data_list_instance = BrokerTaskDataList.from_json(json)
# print the JSON string representation of the object
print BrokerTaskDataList.to_json()

# convert the object into a dict
broker_task_data_list_dict = broker_task_data_list_instance.to_dict()
# create an instance of BrokerTaskDataList from a dict
broker_task_data_list_form_dict = broker_task_data_list.from_dict(broker_task_data_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


