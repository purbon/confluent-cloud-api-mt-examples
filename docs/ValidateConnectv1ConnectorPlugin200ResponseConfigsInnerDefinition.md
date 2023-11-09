# ValidateConnectv1ConnectorPlugin200ResponseConfigsInnerDefinition

The definition for a config in the connector plugin, which includes the name, type, importance, etc.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the configuration | [optional] 
**type** | **str** | The config types | [optional] 
**required** | **bool** | Whether this configuration is required | [optional] 
**default_value** | **str** | Default value for this configuration | [optional] 
**importance** | **str** | The importance level for a configuration | [optional] 
**documentation** | **str** | The documentation for the configuration | [optional] 
**group** | **str** | The UI group to which the configuration belongs to | [optional] 
**width** | **str** | The width of a configuration value | [optional] 
**display_name** | **str** |  | [optional] 
**dependents** | **List[str]** | Other configurations on which this configuration is dependent | [optional] 
**order** | **int** | The order of configuration in specified group | [optional] 
**alias** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.validate_connectv1_connector_plugin200_response_configs_inner_definition import ValidateConnectv1ConnectorPlugin200ResponseConfigsInnerDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateConnectv1ConnectorPlugin200ResponseConfigsInnerDefinition from a JSON string
validate_connectv1_connector_plugin200_response_configs_inner_definition_instance = ValidateConnectv1ConnectorPlugin200ResponseConfigsInnerDefinition.from_json(json)
# print the JSON string representation of the object
print ValidateConnectv1ConnectorPlugin200ResponseConfigsInnerDefinition.to_json()

# convert the object into a dict
validate_connectv1_connector_plugin200_response_configs_inner_definition_dict = validate_connectv1_connector_plugin200_response_configs_inner_definition_instance.to_dict()
# create an instance of ValidateConnectv1ConnectorPlugin200ResponseConfigsInnerDefinition from a dict
validate_connectv1_connector_plugin200_response_configs_inner_definition_form_dict = validate_connectv1_connector_plugin200_response_configs_inner_definition.from_dict(validate_connectv1_connector_plugin200_response_configs_inner_definition_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


