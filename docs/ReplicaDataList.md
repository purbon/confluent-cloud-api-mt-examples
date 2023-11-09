# ReplicaDataList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceCollectionMetadata**](ResourceCollectionMetadata.md) |  | 
**data** | [**List[ReplicaData]**](ReplicaData.md) |  | 

## Example

```python
from openapi_client.models.replica_data_list import ReplicaDataList

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicaDataList from a JSON string
replica_data_list_instance = ReplicaDataList.from_json(json)
# print the JSON string representation of the object
print ReplicaDataList.to_json()

# convert the object into a dict
replica_data_list_dict = replica_data_list_instance.to_dict()
# create an instance of ReplicaDataList from a dict
replica_data_list_form_dict = replica_data_list.from_dict(replica_data_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


