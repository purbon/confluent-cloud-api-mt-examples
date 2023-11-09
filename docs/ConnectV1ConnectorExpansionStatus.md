# ConnectV1ConnectorExpansionStatus

Status of the connector and its tasks.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the connector. | 
**type** | **str** | Type of connector, sink or source. | 
**connector** | [**ConnectV1ConnectorExpansionStatusConnector**](ConnectV1ConnectorExpansionStatusConnector.md) |  | 
**tasks** | [**List[ReadConnectv1ConnectorStatus200ResponseTasksInner]**](ReadConnectv1ConnectorStatus200ResponseTasksInner.md) | A map containing the task status. | [optional] 

## Example

```python
from openapi_client.models.connect_v1_connector_expansion_status import ConnectV1ConnectorExpansionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1ConnectorExpansionStatus from a JSON string
connect_v1_connector_expansion_status_instance = ConnectV1ConnectorExpansionStatus.from_json(json)
# print the JSON string representation of the object
print ConnectV1ConnectorExpansionStatus.to_json()

# convert the object into a dict
connect_v1_connector_expansion_status_dict = connect_v1_connector_expansion_status_instance.to_dict()
# create an instance of ConnectV1ConnectorExpansionStatus from a dict
connect_v1_connector_expansion_status_form_dict = connect_v1_connector_expansion_status.from_dict(connect_v1_connector_expansion_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


