# ConfigUpdateRequest

Config update request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | If alias is specified, then this subject is an alias for the subject named by the alias. That means that any reference to this subject will be replaced by the alias. | [optional] 
**normalize** | **bool** | If true, then schemas are automatically normalized when registered or when passed during lookups. This means that clients do not have to pass the \&quot;normalize\&quot; query parameter to have normalization occur. | [optional] 
**compatibility** | **str** | Compatibility Level | [optional] 
**compatibility_group** | **str** | Only schemas that belong to the same compatibility group will be checked for compatibility. | [optional] 
**default_metadata** | [**ConfigDefaultMetadata**](ConfigDefaultMetadata.md) |  | [optional] 
**override_metadata** | [**ConfigOverrideMetadata**](ConfigOverrideMetadata.md) |  | [optional] 
**default_rule_set** | [**ConfigDefaultRuleSet**](ConfigDefaultRuleSet.md) |  | [optional] 
**override_rule_set** | [**ConfigOverrideRuleSet**](ConfigOverrideRuleSet.md) |  | [optional] 

## Example

```python
from openapi_client.models.config_update_request import ConfigUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigUpdateRequest from a JSON string
config_update_request_instance = ConfigUpdateRequest.from_json(json)
# print the JSON string representation of the object
print ConfigUpdateRequest.to_json()

# convert the object into a dict
config_update_request_dict = config_update_request_instance.to_dict()
# create an instance of ConfigUpdateRequest from a dict
config_update_request_form_dict = config_update_request.from_dict(config_update_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


