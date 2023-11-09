# BrokerReplicaExclusionRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broker_id** | **int** |  | 
**reason** | **str** |  | 

## Example

```python
from openapi_client.models.broker_replica_exclusion_request_data import BrokerReplicaExclusionRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerReplicaExclusionRequestData from a JSON string
broker_replica_exclusion_request_data_instance = BrokerReplicaExclusionRequestData.from_json(json)
# print the JSON string representation of the object
print BrokerReplicaExclusionRequestData.to_json()

# convert the object into a dict
broker_replica_exclusion_request_data_dict = broker_replica_exclusion_request_data_instance.to_dict()
# create an instance of BrokerReplicaExclusionRequestData from a dict
broker_replica_exclusion_request_data_form_dict = broker_replica_exclusion_request_data.from_dict(broker_replica_exclusion_request_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


