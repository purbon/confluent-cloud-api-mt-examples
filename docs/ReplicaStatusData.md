# ReplicaStatusData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**topic_name** | **str** |  | 
**broker_id** | **int** |  | 
**partition_id** | **int** |  | 
**is_leader** | **bool** |  | 
**is_observer** | **bool** |  | 
**is_isr_eligible** | **bool** |  | 
**is_in_isr** | **bool** |  | 
**is_caught_up** | **bool** |  | 
**log_start_offset** | **int** |  | 
**log_end_offset** | **int** |  | 
**last_caught_up_time_ms** | **int** |  | 
**last_fetch_time_ms** | **int** |  | 
**link_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.replica_status_data import ReplicaStatusData

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicaStatusData from a JSON string
replica_status_data_instance = ReplicaStatusData.from_json(json)
# print the JSON string representation of the object
print ReplicaStatusData.to_json()

# convert the object into a dict
replica_status_data_dict = replica_status_data_instance.to_dict()
# create an instance of ReplicaStatusData from a dict
replica_status_data_form_dict = replica_status_data.from_dict(replica_status_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


