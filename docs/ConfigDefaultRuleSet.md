# ConfigDefaultRuleSet

Default value for the ruleSet to be used during schema registration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | **object** | The metadata properties and their new values | [optional] 

## Example

```python
from openapi_client.models.config_default_rule_set import ConfigDefaultRuleSet

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigDefaultRuleSet from a JSON string
config_default_rule_set_instance = ConfigDefaultRuleSet.from_json(json)
# print the JSON string representation of the object
print ConfigDefaultRuleSet.to_json()

# convert the object into a dict
config_default_rule_set_dict = config_default_rule_set_instance.to_dict()
# create an instance of ConfigDefaultRuleSet from a dict
config_default_rule_set_form_dict = config_default_rule_set.from_dict(config_default_rule_set_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


