# Config

Config

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | If alias is specified, then this subject is an alias for the subject named by the alias. That means that any reference to this subject will be replaced by the alias. | [optional] 
**normalize** | **bool** | If true, then schemas are automatically normalized when registered or when passed during lookups. This means that clients do not have to pass the \&quot;normalize\&quot; query parameter to have normalization occur. | [optional] 
**compatibility_level** | **str** | Compatibility Level | [optional] 
**compatibility_group** | **str** | Only schemas that belong to the same compatibility group will be checked for compatibility. | [optional] 
**default_metadata** | [**ConfigDefaultMetadata**](ConfigDefaultMetadata.md) |  | [optional] 
**override_metadata** | [**ConfigOverrideMetadata**](ConfigOverrideMetadata.md) |  | [optional] 
**default_rule_set** | [**ConfigDefaultRuleSet**](ConfigDefaultRuleSet.md) |  | [optional] 
**override_rule_set** | [**ConfigOverrideRuleSet**](ConfigOverrideRuleSet.md) |  | [optional] 

## Example

```python
from openapi_client.models.config import Config

# TODO update the JSON string below
json = "{}"
# create an instance of Config from a JSON string
config_instance = Config.from_json(json)
# print the JSON string representation of the object
print Config.to_json()

# convert the object into a dict
config_dict = config_instance.to_dict()
# create an instance of Config from a dict
config_form_dict = config.from_dict(config_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


