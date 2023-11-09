# AbstractConfigData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**name** | **str** |  | 
**value** | **str** |  | [optional] 
**is_default** | **bool** |  | 
**is_read_only** | **bool** |  | 
**is_sensitive** | **bool** |  | 
**source** | **str** |  | 
**synonyms** | [**List[ConfigSynonymData]**](ConfigSynonymData.md) |  | 

## Example

```python
from openapi_client.models.abstract_config_data import AbstractConfigData

# TODO update the JSON string below
json = "{}"
# create an instance of AbstractConfigData from a JSON string
abstract_config_data_instance = AbstractConfigData.from_json(json)
# print the JSON string representation of the object
print AbstractConfigData.to_json()

# convert the object into a dict
abstract_config_data_dict = abstract_config_data_instance.to_dict()
# create an instance of AbstractConfigData from a dict
abstract_config_data_form_dict = abstract_config_data.from_dict(abstract_config_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


