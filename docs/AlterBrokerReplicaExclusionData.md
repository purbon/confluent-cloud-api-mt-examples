# AlterBrokerReplicaExclusionData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**broker_id** | **int** |  | 
**exclusion** | **str** |  | 
**reason** | **str** |  | 
**error_code** | **int** |  | [optional] 
**error_message** | **str** |  | [optional] 
**broker** | [**Relationship**](Relationship.md) |  | 

## Example

```python
from openapi_client.models.alter_broker_replica_exclusion_data import AlterBrokerReplicaExclusionData

# TODO update the JSON string below
json = "{}"
# create an instance of AlterBrokerReplicaExclusionData from a JSON string
alter_broker_replica_exclusion_data_instance = AlterBrokerReplicaExclusionData.from_json(json)
# print the JSON string representation of the object
print AlterBrokerReplicaExclusionData.to_json()

# convert the object into a dict
alter_broker_replica_exclusion_data_dict = alter_broker_replica_exclusion_data_instance.to_dict()
# create an instance of AlterBrokerReplicaExclusionData from a dict
alter_broker_replica_exclusion_data_form_dict = alter_broker_replica_exclusion_data.from_dict(alter_broker_replica_exclusion_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


