# ConsumerData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**consumer_group_id** | **str** |  | 
**consumer_id** | **str** |  | 
**instance_id** | **str** |  | [optional] 
**client_id** | **str** |  | 
**assignments** | [**Relationship**](Relationship.md) |  | 

## Example

```python
from openapi_client.models.consumer_data import ConsumerData

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerData from a JSON string
consumer_data_instance = ConsumerData.from_json(json)
# print the JSON string representation of the object
print ConsumerData.to_json()

# convert the object into a dict
consumer_data_dict = consumer_data_instance.to_dict()
# create an instance of ConsumerData from a dict
consumer_data_form_dict = consumer_data.from_dict(consumer_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


