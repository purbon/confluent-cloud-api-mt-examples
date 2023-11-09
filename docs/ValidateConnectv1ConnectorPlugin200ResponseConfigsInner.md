# ValidateConnectv1ConnectorPlugin200ResponseConfigsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition** | [**ValidateConnectv1ConnectorPlugin200ResponseConfigsInnerDefinition**](ValidateConnectv1ConnectorPlugin200ResponseConfigsInnerDefinition.md) |  | [optional] 
**value** | [**ValidateConnectv1ConnectorPlugin200ResponseConfigsInnerValue**](ValidateConnectv1ConnectorPlugin200ResponseConfigsInnerValue.md) |  | [optional] 
**metadata** | **object** | Map of metadata details about the connector configuration, such as type of input, etc. | [optional] 

## Example

```python
from openapi_client.models.validate_connectv1_connector_plugin200_response_configs_inner import ValidateConnectv1ConnectorPlugin200ResponseConfigsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateConnectv1ConnectorPlugin200ResponseConfigsInner from a JSON string
validate_connectv1_connector_plugin200_response_configs_inner_instance = ValidateConnectv1ConnectorPlugin200ResponseConfigsInner.from_json(json)
# print the JSON string representation of the object
print ValidateConnectv1ConnectorPlugin200ResponseConfigsInner.to_json()

# convert the object into a dict
validate_connectv1_connector_plugin200_response_configs_inner_dict = validate_connectv1_connector_plugin200_response_configs_inner_instance.to_dict()
# create an instance of ValidateConnectv1ConnectorPlugin200ResponseConfigsInner from a dict
validate_connectv1_connector_plugin200_response_configs_inner_form_dict = validate_connectv1_connector_plugin200_response_configs_inner.from_dict(validate_connectv1_connector_plugin200_response_configs_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


