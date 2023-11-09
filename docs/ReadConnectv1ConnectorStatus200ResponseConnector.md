# ReadConnectv1ConnectorStatus200ResponseConnector

The map containing connector status.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the connector. | 
**worker_id** | **str** | The worker ID of the connector. | 
**trace** | **str** | The exception name in case of error. | [optional] 

## Example

```python
from openapi_client.models.read_connectv1_connector_status200_response_connector import ReadConnectv1ConnectorStatus200ResponseConnector

# TODO update the JSON string below
json = "{}"
# create an instance of ReadConnectv1ConnectorStatus200ResponseConnector from a JSON string
read_connectv1_connector_status200_response_connector_instance = ReadConnectv1ConnectorStatus200ResponseConnector.from_json(json)
# print the JSON string representation of the object
print ReadConnectv1ConnectorStatus200ResponseConnector.to_json()

# convert the object into a dict
read_connectv1_connector_status200_response_connector_dict = read_connectv1_connector_status200_response_connector_instance.to_dict()
# create an instance of ReadConnectv1ConnectorStatus200ResponseConnector from a dict
read_connectv1_connector_status200_response_connector_form_dict = read_connectv1_connector_status200_response_connector.from_dict(read_connectv1_connector_status200_response_connector_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


