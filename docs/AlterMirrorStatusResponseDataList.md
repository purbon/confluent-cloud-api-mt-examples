# AlterMirrorStatusResponseDataList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceCollectionMetadata**](ResourceCollectionMetadata.md) |  | 
**data** | [**List[AlterMirrorStatusResponseData]**](AlterMirrorStatusResponseData.md) |  | 

## Example

```python
from openapi_client.models.alter_mirror_status_response_data_list import AlterMirrorStatusResponseDataList

# TODO update the JSON string below
json = "{}"
# create an instance of AlterMirrorStatusResponseDataList from a JSON string
alter_mirror_status_response_data_list_instance = AlterMirrorStatusResponseDataList.from_json(json)
# print the JSON string representation of the object
print AlterMirrorStatusResponseDataList.to_json()

# convert the object into a dict
alter_mirror_status_response_data_list_dict = alter_mirror_status_response_data_list_instance.to_dict()
# create an instance of AlterMirrorStatusResponseDataList from a dict
alter_mirror_status_response_data_list_form_dict = alter_mirror_status_response_data_list.from_dict(alter_mirror_status_response_data_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


