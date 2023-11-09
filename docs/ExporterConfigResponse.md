# ExporterConfigResponse

The map containing exporter’s configurations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_registry_url** | **str** | Config SR URL | [optional] 
**basic_auth_credentials_source** | **str** | Config SR Auth | [optional] 
**basic_auth_user_info** | **str** | Config SR User Info | [optional] 

## Example

```python
from openapi_client.models.exporter_config_response import ExporterConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExporterConfigResponse from a JSON string
exporter_config_response_instance = ExporterConfigResponse.from_json(json)
# print the JSON string representation of the object
print ExporterConfigResponse.to_json()

# convert the object into a dict
exporter_config_response_dict = exporter_config_response_instance.to_dict()
# create an instance of ExporterConfigResponse from a dict
exporter_config_response_form_dict = exporter_config_response.from_dict(exporter_config_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


