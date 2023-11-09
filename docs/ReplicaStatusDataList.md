# ReplicaStatusDataList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceCollectionMetadata**](ResourceCollectionMetadata.md) |  | 
**data** | [**List[ReplicaStatusData]**](ReplicaStatusData.md) |  | 

## Example

```python
from openapi_client.models.replica_status_data_list import ReplicaStatusDataList

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicaStatusDataList from a JSON string
replica_status_data_list_instance = ReplicaStatusDataList.from_json(json)
# print the JSON string representation of the object
print ReplicaStatusDataList.to_json()

# convert the object into a dict
replica_status_data_list_dict = replica_status_data_list_instance.to_dict()
# create an instance of ReplicaStatusDataList from a dict
replica_status_data_list_form_dict = replica_status_data_list.from_dict(replica_status_data_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


