# ReassignmentDataList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceCollectionMetadata**](ResourceCollectionMetadata.md) |  | 
**data** | [**List[ReassignmentData]**](ReassignmentData.md) |  | 

## Example

```python
from openapi_client.models.reassignment_data_list import ReassignmentDataList

# TODO update the JSON string below
json = "{}"
# create an instance of ReassignmentDataList from a JSON string
reassignment_data_list_instance = ReassignmentDataList.from_json(json)
# print the JSON string representation of the object
print ReassignmentDataList.to_json()

# convert the object into a dict
reassignment_data_list_dict = reassignment_data_list_instance.to_dict()
# create an instance of ReassignmentDataList from a dict
reassignment_data_list_form_dict = reassignment_data_list.from_dict(reassignment_data_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


