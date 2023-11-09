# BrokerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**broker_id** | **int** |  | 
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**rack** | **str** |  | [optional] 
**configs** | [**Relationship**](Relationship.md) |  | 
**partition_replicas** | [**Relationship**](Relationship.md) |  | 

## Example

```python
from openapi_client.models.broker_data import BrokerData

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerData from a JSON string
broker_data_instance = BrokerData.from_json(json)
# print the JSON string representation of the object
print BrokerData.to_json()

# convert the object into a dict
broker_data_dict = broker_data_instance.to_dict()
# create an instance of BrokerData from a dict
broker_data_form_dict = broker_data.from_dict(broker_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


