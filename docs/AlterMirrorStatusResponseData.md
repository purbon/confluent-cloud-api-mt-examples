# AlterMirrorStatusResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**mirror_topic_name** | **str** |  | 
**error_message** | **str** |  | 
**error_code** | **int** |  | 
**mirror_lags** | [**List[MirrorLag]**](MirrorLag.md) |  | 

## Example

```python
from openapi_client.models.alter_mirror_status_response_data import AlterMirrorStatusResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AlterMirrorStatusResponseData from a JSON string
alter_mirror_status_response_data_instance = AlterMirrorStatusResponseData.from_json(json)
# print the JSON string representation of the object
print AlterMirrorStatusResponseData.to_json()

# convert the object into a dict
alter_mirror_status_response_data_dict = alter_mirror_status_response_data_instance.to_dict()
# create an instance of AlterMirrorStatusResponseData from a dict
alter_mirror_status_response_data_form_dict = alter_mirror_status_response_data.from_dict(alter_mirror_status_response_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


