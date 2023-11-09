# ConfigSynonymData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | [optional] 
**source** | **str** |  | 

## Example

```python
from openapi_client.models.config_synonym_data import ConfigSynonymData

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSynonymData from a JSON string
config_synonym_data_instance = ConfigSynonymData.from_json(json)
# print the JSON string representation of the object
print ConfigSynonymData.to_json()

# convert the object into a dict
config_synonym_data_dict = config_synonym_data_instance.to_dict()
# create an instance of ConfigSynonymData from a dict
config_synonym_data_form_dict = config_synonym_data.from_dict(config_synonym_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


