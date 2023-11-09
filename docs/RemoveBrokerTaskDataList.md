# RemoveBrokerTaskDataList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceCollectionMetadata**](ResourceCollectionMetadata.md) |  | 
**data** | [**List[RemoveBrokerTaskData]**](RemoveBrokerTaskData.md) |  | 

## Example

```python
from openapi_client.models.remove_broker_task_data_list import RemoveBrokerTaskDataList

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveBrokerTaskDataList from a JSON string
remove_broker_task_data_list_instance = RemoveBrokerTaskDataList.from_json(json)
# print the JSON string representation of the object
print RemoveBrokerTaskDataList.to_json()

# convert the object into a dict
remove_broker_task_data_list_dict = remove_broker_task_data_list_instance.to_dict()
# create an instance of RemoveBrokerTaskDataList from a dict
remove_broker_task_data_list_form_dict = remove_broker_task_data_list.from_dict(remove_broker_task_data_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


