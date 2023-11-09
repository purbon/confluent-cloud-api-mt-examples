# ReadConnectv1ConnectorStatus200ResponseTasksInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of task. | 
**state** | **str** | The state of the task. | 
**worker_id** | **str** | The worker ID of the task. | 
**msg** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.read_connectv1_connector_status200_response_tasks_inner import ReadConnectv1ConnectorStatus200ResponseTasksInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReadConnectv1ConnectorStatus200ResponseTasksInner from a JSON string
read_connectv1_connector_status200_response_tasks_inner_instance = ReadConnectv1ConnectorStatus200ResponseTasksInner.from_json(json)
# print the JSON string representation of the object
print ReadConnectv1ConnectorStatus200ResponseTasksInner.to_json()

# convert the object into a dict
read_connectv1_connector_status200_response_tasks_inner_dict = read_connectv1_connector_status200_response_tasks_inner_instance.to_dict()
# create an instance of ReadConnectv1ConnectorStatus200ResponseTasksInner from a dict
read_connectv1_connector_status200_response_tasks_inner_form_dict = read_connectv1_connector_status200_response_tasks_inner.from_dict(read_connectv1_connector_status200_response_tasks_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


