# ReadConnectv1ConnectorStatus200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the connector. | 
**type** | **str** | Type of connector, sink or source. | 
**connector** | [**ReadConnectv1ConnectorStatus200ResponseConnector**](ReadConnectv1ConnectorStatus200ResponseConnector.md) |  | 
**tasks** | [**List[ReadConnectv1ConnectorStatus200ResponseTasksInner]**](ReadConnectv1ConnectorStatus200ResponseTasksInner.md) | The map containing the task status. | [optional] 

## Example

```python
from openapi_client.models.read_connectv1_connector_status200_response import ReadConnectv1ConnectorStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ReadConnectv1ConnectorStatus200Response from a JSON string
read_connectv1_connector_status200_response_instance = ReadConnectv1ConnectorStatus200Response.from_json(json)
# print the JSON string representation of the object
print ReadConnectv1ConnectorStatus200Response.to_json()

# convert the object into a dict
read_connectv1_connector_status200_response_dict = read_connectv1_connector_status200_response_instance.to_dict()
# create an instance of ReadConnectv1ConnectorStatus200Response from a dict
read_connectv1_connector_status200_response_form_dict = read_connectv1_connector_status200_response.from_dict(read_connectv1_connector_status200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


