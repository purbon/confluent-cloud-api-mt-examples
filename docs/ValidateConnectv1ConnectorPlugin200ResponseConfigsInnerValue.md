# ValidateConnectv1ConnectorPlugin200ResponseConfigsInnerValue

The current value for a config, which includes the name, value, recommended values, etc.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the configuration | [optional] 
**value** | **str** | The value for the configuration | [optional] 
**recommended_values** | **List[str]** | The list of valid values for the configuration | [optional] 
**errors** | **List[str]** | Errors, if any, in the configuration value | [optional] 
**visible** | **bool** | The visibility of the configuration. Based on the values of other configuration fields, this visibility boolean value points out if the current field should be visible or not. | [optional] 

## Example

```python
from openapi_client.models.validate_connectv1_connector_plugin200_response_configs_inner_value import ValidateConnectv1ConnectorPlugin200ResponseConfigsInnerValue

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateConnectv1ConnectorPlugin200ResponseConfigsInnerValue from a JSON string
validate_connectv1_connector_plugin200_response_configs_inner_value_instance = ValidateConnectv1ConnectorPlugin200ResponseConfigsInnerValue.from_json(json)
# print the JSON string representation of the object
print ValidateConnectv1ConnectorPlugin200ResponseConfigsInnerValue.to_json()

# convert the object into a dict
validate_connectv1_connector_plugin200_response_configs_inner_value_dict = validate_connectv1_connector_plugin200_response_configs_inner_value_instance.to_dict()
# create an instance of ValidateConnectv1ConnectorPlugin200ResponseConfigsInnerValue from a dict
validate_connectv1_connector_plugin200_response_configs_inner_value_form_dict = validate_connectv1_connector_plugin200_response_configs_inner_value.from_dict(validate_connectv1_connector_plugin200_response_configs_inner_value_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


