# ConnectV1ConnectorExpansionStatusConnector

A map containing connector status.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the connector. | 
**worker_id** | **str** | The worker ID of the connector. | 
**trace** | **str** | Exception message in case of an error. | [optional] 

## Example

```python
from openapi_client.models.connect_v1_connector_expansion_status_connector import ConnectV1ConnectorExpansionStatusConnector

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1ConnectorExpansionStatusConnector from a JSON string
connect_v1_connector_expansion_status_connector_instance = ConnectV1ConnectorExpansionStatusConnector.from_json(json)
# print the JSON string representation of the object
print ConnectV1ConnectorExpansionStatusConnector.to_json()

# convert the object into a dict
connect_v1_connector_expansion_status_connector_dict = connect_v1_connector_expansion_status_connector_instance.to_dict()
# create an instance of ConnectV1ConnectorExpansionStatusConnector from a dict
connect_v1_connector_expansion_status_connector_form_dict = connect_v1_connector_expansion_status_connector.from_dict(connect_v1_connector_expansion_status_connector_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


