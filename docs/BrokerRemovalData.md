# BrokerRemovalData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**broker_id** | **int** |  | 
**broker_task** | [**Relationship**](Relationship.md) |  | 
**broker** | [**Relationship**](Relationship.md) |  | 

## Example

```python
from openapi_client.models.broker_removal_data import BrokerRemovalData

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerRemovalData from a JSON string
broker_removal_data_instance = BrokerRemovalData.from_json(json)
# print the JSON string representation of the object
print BrokerRemovalData.to_json()

# convert the object into a dict
broker_removal_data_dict = broker_removal_data_instance.to_dict()
# create an instance of BrokerRemovalData from a dict
broker_removal_data_form_dict = broker_removal_data.from_dict(broker_removal_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


