# ConsumerLagDataList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceCollectionMetadata**](ResourceCollectionMetadata.md) |  | 
**data** | [**List[ConsumerLagData]**](ConsumerLagData.md) |  | 

## Example

```python
from openapi_client.models.consumer_lag_data_list import ConsumerLagDataList

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerLagDataList from a JSON string
consumer_lag_data_list_instance = ConsumerLagDataList.from_json(json)
# print the JSON string representation of the object
print ConsumerLagDataList.to_json()

# convert the object into a dict
consumer_lag_data_list_dict = consumer_lag_data_list_instance.to_dict()
# create an instance of ConsumerLagDataList from a dict
consumer_lag_data_list_form_dict = consumer_lag_data_list.from_dict(consumer_lag_data_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


