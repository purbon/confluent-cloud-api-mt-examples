# BrokerReplicaExclusionData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**broker_id** | **int** |  | 
**reason** | **str** |  | 
**broker** | [**Relationship**](Relationship.md) |  | 

## Example

```python
from openapi_client.models.broker_replica_exclusion_data import BrokerReplicaExclusionData

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerReplicaExclusionData from a JSON string
broker_replica_exclusion_data_instance = BrokerReplicaExclusionData.from_json(json)
# print the JSON string representation of the object
print BrokerReplicaExclusionData.to_json()

# convert the object into a dict
broker_replica_exclusion_data_dict = broker_replica_exclusion_data_instance.to_dict()
# create an instance of BrokerReplicaExclusionData from a dict
broker_replica_exclusion_data_form_dict = broker_replica_exclusion_data.from_dict(broker_replica_exclusion_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


