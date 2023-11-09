# PartitionDataList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceCollectionMetadata**](ResourceCollectionMetadata.md) |  | 
**data** | [**List[PartitionData]**](PartitionData.md) |  | 

## Example

```python
from openapi_client.models.partition_data_list import PartitionDataList

# TODO update the JSON string below
json = "{}"
# create an instance of PartitionDataList from a JSON string
partition_data_list_instance = PartitionDataList.from_json(json)
# print the JSON string representation of the object
print PartitionDataList.to_json()

# convert the object into a dict
partition_data_list_dict = partition_data_list_instance.to_dict()
# create an instance of PartitionDataList from a dict
partition_data_list_form_dict = partition_data_list.from_dict(partition_data_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


