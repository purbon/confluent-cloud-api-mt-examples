# ConsumerGroupLagSummaryData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**consumer_group_id** | **str** |  | 
**max_lag_consumer_id** | **str** |  | 
**max_lag_instance_id** | **str** |  | [optional] 
**max_lag_client_id** | **str** |  | 
**max_lag_topic_name** | **str** |  | 
**max_lag_partition_id** | **int** |  | 
**max_lag** | **int** |  | 
**total_lag** | **int** |  | 
**max_lag_consumer** | [**Relationship**](Relationship.md) |  | 
**max_lag_partition** | [**Relationship**](Relationship.md) |  | 

## Example

```python
from openapi_client.models.consumer_group_lag_summary_data import ConsumerGroupLagSummaryData

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerGroupLagSummaryData from a JSON string
consumer_group_lag_summary_data_instance = ConsumerGroupLagSummaryData.from_json(json)
# print the JSON string representation of the object
print ConsumerGroupLagSummaryData.to_json()

# convert the object into a dict
consumer_group_lag_summary_data_dict = consumer_group_lag_summary_data_instance.to_dict()
# create an instance of ConsumerGroupLagSummaryData from a dict
consumer_group_lag_summary_data_form_dict = consumer_group_lag_summary_data.from_dict(consumer_group_lag_summary_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


