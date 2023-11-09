# ConnectV1ConnectorErrorError

Connector Error with error code and message.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Error code for the type of error | [optional] 
**message** | **str** | Human readable error message | [optional] 

## Example

```python
from openapi_client.models.connect_v1_connector_error_error import ConnectV1ConnectorErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1ConnectorErrorError from a JSON string
connect_v1_connector_error_error_instance = ConnectV1ConnectorErrorError.from_json(json)
# print the JSON string representation of the object
print ConnectV1ConnectorErrorError.to_json()

# convert the object into a dict
connect_v1_connector_error_error_dict = connect_v1_connector_error_error_instance.to_dict()
# create an instance of ConnectV1ConnectorErrorError from a dict
connect_v1_connector_error_error_form_dict = connect_v1_connector_error_error.from_dict(connect_v1_connector_error_error_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


