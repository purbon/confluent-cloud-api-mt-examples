# ListLinkConfigsResponseDataList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceCollectionMetadata**](ResourceCollectionMetadata.md) |  | 
**data** | [**List[ListLinkConfigsResponseData]**](ListLinkConfigsResponseData.md) |  | 

## Example

```python
from openapi_client.models.list_link_configs_response_data_list import ListLinkConfigsResponseDataList

# TODO update the JSON string below
json = "{}"
# create an instance of ListLinkConfigsResponseDataList from a JSON string
list_link_configs_response_data_list_instance = ListLinkConfigsResponseDataList.from_json(json)
# print the JSON string representation of the object
print ListLinkConfigsResponseDataList.to_json()

# convert the object into a dict
list_link_configs_response_data_list_dict = list_link_configs_response_data_list_instance.to_dict()
# create an instance of ListLinkConfigsResponseDataList from a dict
list_link_configs_response_data_list_form_dict = list_link_configs_response_data_list.from_dict(list_link_configs_response_data_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


