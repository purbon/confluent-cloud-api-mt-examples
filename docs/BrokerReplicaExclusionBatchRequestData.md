# BrokerReplicaExclusionBatchRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BrokerReplicaExclusionRequestData]**](BrokerReplicaExclusionRequestData.md) |  | 

## Example

```python
from openapi_client.models.broker_replica_exclusion_batch_request_data import BrokerReplicaExclusionBatchRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerReplicaExclusionBatchRequestData from a JSON string
broker_replica_exclusion_batch_request_data_instance = BrokerReplicaExclusionBatchRequestData.from_json(json)
# print the JSON string representation of the object
print BrokerReplicaExclusionBatchRequestData.to_json()

# convert the object into a dict
broker_replica_exclusion_batch_request_data_dict = broker_replica_exclusion_batch_request_data_instance.to_dict()
# create an instance of BrokerReplicaExclusionBatchRequestData from a dict
broker_replica_exclusion_batch_request_data_form_dict = broker_replica_exclusion_batch_request_data.from_dict(broker_replica_exclusion_batch_request_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


