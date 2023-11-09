# ByokV1AzureKey

The Azure BYOK details. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The Application ID created for this key-environment combination.  | [optional] [readonly] 
**key_id** | **str** | The unique Key Object Identifier URL without version of an Azure Key Vault key.  | 
**key_vault_id** | **str** | Key Vault ID containing the key  | 
**kind** | **str** | BYOK kind type.  | 
**tenant_id** | **str** | Tenant ID (uuid) hosting the Key Vault containing the key  | 

## Example

```python
from openapi_client.models.byok_v1_azure_key import ByokV1AzureKey

# TODO update the JSON string below
json = "{}"
# create an instance of ByokV1AzureKey from a JSON string
byok_v1_azure_key_instance = ByokV1AzureKey.from_json(json)
# print the JSON string representation of the object
print ByokV1AzureKey.to_json()

# convert the object into a dict
byok_v1_azure_key_dict = byok_v1_azure_key_instance.to_dict()
# create an instance of ByokV1AzureKey from a dict
byok_v1_azure_key_form_dict = byok_v1_azure_key.from_dict(byok_v1_azure_key_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


