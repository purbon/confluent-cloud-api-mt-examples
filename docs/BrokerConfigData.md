# BrokerConfigData


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
**broker_id** | **int** |  | 

## Example

```python
from openapi_client.models.broker_config_data import BrokerConfigData

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerConfigData from a JSON string
broker_config_data_instance = BrokerConfigData.from_json(json)
# print the JSON string representation of the object
print BrokerConfigData.to_json()

# convert the object into a dict
broker_config_data_dict = broker_config_data_instance.to_dict()
# create an instance of BrokerConfigData from a dict
broker_config_data_form_dict = broker_config_data.from_dict(broker_config_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


