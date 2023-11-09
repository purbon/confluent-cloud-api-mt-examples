# RemoveBrokersRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**broker_ids** | **List[int]** |  | 

## Example

```python
from openapi_client.models.remove_brokers_request_data import RemoveBrokersRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveBrokersRequestData from a JSON string
remove_brokers_request_data_instance = RemoveBrokersRequestData.from_json(json)
# print the JSON string representation of the object
print RemoveBrokersRequestData.to_json()

# convert the object into a dict
remove_brokers_request_data_dict = remove_brokers_request_data_instance.to_dict()
# create an instance of RemoveBrokersRequestData from a dict
remove_brokers_request_data_form_dict = remove_brokers_request_data.from_dict(remove_brokers_request_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


