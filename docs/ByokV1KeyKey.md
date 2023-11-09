# ByokV1KeyKey

The cloud-specific key details.  For AWS please provide the corresponding `key_arn`. For Azure please provide the corresponding `key_id`. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_arn** | **str** | The Amazon Resource Name (ARN) of an AWS KMS key.  | 
**roles** | **List[str]** | The Amazon Resource Names (ARNs) of IAM Roles created for this key-environment combination.  | [optional] [readonly] 
**kind** | **str** | BYOK kind type.  | 
**application_id** | **str** | The Application ID created for this key-environment combination.  | [optional] [readonly] 
**key_id** | **str** | The unique Key Object Identifier URL without version of an Azure Key Vault key.  | 
**key_vault_id** | **str** | Key Vault ID containing the key  | 
**tenant_id** | **str** | Tenant ID (uuid) hosting the Key Vault containing the key  | 

## Example

```python
from openapi_client.models.byok_v1_key_key import ByokV1KeyKey

# TODO update the JSON string below
json = "{}"
# create an instance of ByokV1KeyKey from a JSON string
byok_v1_key_key_instance = ByokV1KeyKey.from_json(json)
# print the JSON string representation of the object
print ByokV1KeyKey.to_json()

# convert the object into a dict
byok_v1_key_key_dict = byok_v1_key_key_instance.to_dict()
# create an instance of ByokV1KeyKey from a dict
byok_v1_key_key_form_dict = byok_v1_key_key.from_dict(byok_v1_key_key_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


