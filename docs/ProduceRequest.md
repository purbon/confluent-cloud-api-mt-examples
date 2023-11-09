# ProduceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partition_id** | **int** |  | [optional] 
**headers** | [**List[ProduceRequestHeader]**](ProduceRequestHeader.md) |  | [optional] 
**key** | [**ProduceRequestData**](ProduceRequestData.md) |  | [optional] 
**value** | [**ProduceRequestData**](ProduceRequestData.md) |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.produce_request import ProduceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProduceRequest from a JSON string
produce_request_instance = ProduceRequest.from_json(json)
# print the JSON string representation of the object
print ProduceRequest.to_json()

# convert the object into a dict
produce_request_dict = produce_request_instance.to_dict()
# create an instance of ProduceRequest from a dict
produce_request_form_dict = produce_request.from_dict(produce_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


