# ValidateConnectv1ConnectorPlugin200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The class name of the connector plugin. | [optional] 
**groups** | **List[str]** | The list of groups used in configuration definitions. | [optional] 
**error_count** | **int** | The total number of errors encountered during configuration validation. | [optional] 
**configs** | [**List[ValidateConnectv1ConnectorPlugin200ResponseConfigsInner]**](ValidateConnectv1ConnectorPlugin200ResponseConfigsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.validate_connectv1_connector_plugin200_response import ValidateConnectv1ConnectorPlugin200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateConnectv1ConnectorPlugin200Response from a JSON string
validate_connectv1_connector_plugin200_response_instance = ValidateConnectv1ConnectorPlugin200Response.from_json(json)
# print the JSON string representation of the object
print ValidateConnectv1ConnectorPlugin200Response.to_json()

# convert the object into a dict
validate_connectv1_connector_plugin200_response_dict = validate_connectv1_connector_plugin200_response_instance.to_dict()
# create an instance of ValidateConnectv1ConnectorPlugin200Response from a dict
validate_connectv1_connector_plugin200_response_form_dict = validate_connectv1_connector_plugin200_response.from_dict(validate_connectv1_connector_plugin200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


