# ListLinkConfigsResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**name** | **str** |  | 
**value** | **str** |  | 
**read_only** | **bool** |  | 
**sensitive** | **bool** |  | 
**source** | **str** |  | 
**synonyms** | **List[str]** |  | 
**link_name** | **str** |  | 

## Example

```python
from openapi_client.models.list_link_configs_response_data import ListLinkConfigsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListLinkConfigsResponseData from a JSON string
list_link_configs_response_data_instance = ListLinkConfigsResponseData.from_json(json)
# print the JSON string representation of the object
print ListLinkConfigsResponseData.to_json()

# convert the object into a dict
list_link_configs_response_data_dict = list_link_configs_response_data_instance.to_dict()
# create an instance of ListLinkConfigsResponseData from a dict
list_link_configs_response_data_form_dict = list_link_configs_response_data.from_dict(list_link_configs_response_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


