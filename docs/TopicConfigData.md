# TopicConfigData


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
**topic_name** | **str** |  | 

## Example

```python
from openapi_client.models.topic_config_data import TopicConfigData

# TODO update the JSON string below
json = "{}"
# create an instance of TopicConfigData from a JSON string
topic_config_data_instance = TopicConfigData.from_json(json)
# print the JSON string representation of the object
print TopicConfigData.to_json()

# convert the object into a dict
topic_config_data_dict = topic_config_data_instance.to_dict()
# create an instance of TopicConfigData from a dict
topic_config_data_form_dict = topic_config_data.from_dict(topic_config_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


