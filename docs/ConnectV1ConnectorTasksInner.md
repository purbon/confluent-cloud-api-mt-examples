# ConnectV1ConnectorTasksInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector** | **str** | The name of the connector the task belongs to | 
**task** | **int** | Task ID within the connector | 

## Example

```python
from openapi_client.models.connect_v1_connector_tasks_inner import ConnectV1ConnectorTasksInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1ConnectorTasksInner from a JSON string
connect_v1_connector_tasks_inner_instance = ConnectV1ConnectorTasksInner.from_json(json)
# print the JSON string representation of the object
print ConnectV1ConnectorTasksInner.to_json()

# convert the object into a dict
connect_v1_connector_tasks_inner_dict = connect_v1_connector_tasks_inner_instance.to_dict()
# create an instance of ConnectV1ConnectorTasksInner from a dict
connect_v1_connector_tasks_inner_form_dict = connect_v1_connector_tasks_inner.from_dict(connect_v1_connector_tasks_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


