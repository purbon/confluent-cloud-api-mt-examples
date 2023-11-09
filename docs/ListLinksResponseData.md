# ListLinksResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**source_cluster_id** | **str** |  | [optional] 
**destination_cluster_id** | **str** |  | [optional] 
**remote_cluster_id** | **str** |  | [optional] 
**link_name** | **str** |  | 
**link_id** | **str** |  | [optional] 
**cluster_link_id** | **str** |  | 
**topic_names** | **List[str]** |  | 
**link_error** | **str** |  | [optional] 
**link_error_message** | **str** |  | [optional] 
**link_state** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.list_links_response_data import ListLinksResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ListLinksResponseData from a JSON string
list_links_response_data_instance = ListLinksResponseData.from_json(json)
# print the JSON string representation of the object
print ListLinksResponseData.to_json()

# convert the object into a dict
list_links_response_data_dict = list_links_response_data_instance.to_dict()
# create an instance of ListLinksResponseData from a dict
list_links_response_data_form_dict = list_links_response_data.from_dict(list_links_response_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


