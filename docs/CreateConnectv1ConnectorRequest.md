# CreateConnectv1ConnectorRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the connector to create. | [optional] 
**config** | [**CreateConnectv1ConnectorRequestConfig**](CreateConnectv1ConnectorRequestConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_connectv1_connector_request import CreateConnectv1ConnectorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectv1ConnectorRequest from a JSON string
create_connectv1_connector_request_instance = CreateConnectv1ConnectorRequest.from_json(json)
# print the JSON string representation of the object
print CreateConnectv1ConnectorRequest.to_json()

# convert the object into a dict
create_connectv1_connector_request_dict = create_connectv1_connector_request_instance.to_dict()
# create an instance of CreateConnectv1ConnectorRequest from a dict
create_connectv1_connector_request_form_dict = create_connectv1_connector_request.from_dict(create_connectv1_connector_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


