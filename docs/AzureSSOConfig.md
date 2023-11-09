# AzureSSOConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**tenant_id** | **str** | The Azure AD tenant ID | 

## Example

```python
from openapi_client.models.azure_sso_config import AzureSSOConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSSOConfig from a JSON string
azure_sso_config_instance = AzureSSOConfig.from_json(json)
# print the JSON string representation of the object
print AzureSSOConfig.to_json()

# convert the object into a dict
azure_sso_config_dict = azure_sso_config_instance.to_dict()
# create an instance of AzureSSOConfig from a dict
azure_sso_config_form_dict = azure_sso_config.from_dict(azure_sso_config_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


