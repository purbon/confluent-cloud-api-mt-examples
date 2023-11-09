# BrokerDataList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceCollectionMetadata**](ResourceCollectionMetadata.md) |  | 
**data** | [**List[BrokerData]**](BrokerData.md) |  | 

## Example

```python
from openapi_client.models.broker_data_list import BrokerDataList

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerDataList from a JSON string
broker_data_list_instance = BrokerDataList.from_json(json)
# print the JSON string representation of the object
print BrokerDataList.to_json()

# convert the object into a dict
broker_data_list_dict = broker_data_list_instance.to_dict()
# create an instance of BrokerDataList from a dict
broker_data_list_form_dict = broker_data_list.from_dict(broker_data_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


