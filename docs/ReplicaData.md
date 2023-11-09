# ReplicaData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**topic_name** | **str** |  | 
**partition_id** | **int** |  | 
**broker_id** | **int** |  | 
**is_leader** | **bool** |  | 
**is_in_sync** | **bool** |  | 
**broker** | [**Relationship**](Relationship.md) |  | 

## Example

```python
from openapi_client.models.replica_data import ReplicaData

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicaData from a JSON string
replica_data_instance = ReplicaData.from_json(json)
# print the JSON string representation of the object
print ReplicaData.to_json()

# convert the object into a dict
replica_data_dict = replica_data_instance.to_dict()
# create an instance of ReplicaData from a dict
replica_data_form_dict = replica_data.from_dict(replica_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


