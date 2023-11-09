# ProduceRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**data** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.produce_request_data import ProduceRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of ProduceRequestData from a JSON string
produce_request_data_instance = ProduceRequestData.from_json(json)
# print the JSON string representation of the object
print ProduceRequestData.to_json()

# convert the object into a dict
produce_request_data_dict = produce_request_data_instance.to_dict()
# create an instance of ProduceRequestData from a dict
produce_request_data_form_dict = produce_request_data.from_dict(produce_request_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


