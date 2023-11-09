# ConsumerLagData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**consumer_group_id** | **str** |  | 
**topic_name** | **str** |  | 
**partition_id** | **int** |  | 
**current_offset** | **int** |  | 
**log_end_offset** | **int** |  | 
**lag** | **int** |  | 
**consumer_id** | **str** |  | 
**instance_id** | **str** |  | [optional] 
**client_id** | **str** |  | 

## Example

```python
from openapi_client.models.consumer_lag_data import ConsumerLagData

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerLagData from a JSON string
consumer_lag_data_instance = ConsumerLagData.from_json(json)
# print the JSON string representation of the object
print ConsumerLagData.to_json()

# convert the object into a dict
consumer_lag_data_dict = consumer_lag_data_instance.to_dict()
# create an instance of ConsumerLagData from a dict
consumer_lag_data_form_dict = consumer_lag_data.from_dict(consumer_lag_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


