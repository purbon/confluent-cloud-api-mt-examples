# ConsumerGroupData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**consumer_group_id** | **str** |  | 
**is_simple** | **bool** |  | 
**partition_assignor** | **str** |  | 
**state** | **str** |  | 
**coordinator** | [**Relationship**](Relationship.md) |  | 
**consumer** | [**Relationship**](Relationship.md) |  | [optional] 
**lag_summary** | [**Relationship**](Relationship.md) |  | 

## Example

```python
from openapi_client.models.consumer_group_data import ConsumerGroupData

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerGroupData from a JSON string
consumer_group_data_instance = ConsumerGroupData.from_json(json)
# print the JSON string representation of the object
print ConsumerGroupData.to_json()

# convert the object into a dict
consumer_group_data_dict = consumer_group_data_instance.to_dict()
# create an instance of ConsumerGroupData from a dict
consumer_group_data_form_dict = consumer_group_data.from_dict(consumer_group_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


