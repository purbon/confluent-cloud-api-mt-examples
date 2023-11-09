# ConfigData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from openapi_client.models.config_data import ConfigData

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigData from a JSON string
config_data_instance = ConfigData.from_json(json)
# print the JSON string representation of the object
print ConfigData.to_json()

# convert the object into a dict
config_data_dict = config_data_instance.to_dict()
# create an instance of ConfigData from a dict
config_data_form_dict = config_data.from_dict(config_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


