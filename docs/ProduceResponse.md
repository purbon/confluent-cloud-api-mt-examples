# ProduceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** |  | 
**message** | **str** |  | [optional] 
**cluster_id** | **str** |  | [optional] 
**topic_name** | **str** |  | [optional] 
**partition_id** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**key** | [**ProduceResponseData**](ProduceResponseData.md) |  | [optional] 
**value** | [**ProduceResponseData**](ProduceResponseData.md) |  | [optional] 

## Example

```python
from openapi_client.models.produce_response import ProduceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProduceResponse from a JSON string
produce_response_instance = ProduceResponse.from_json(json)
# print the JSON string representation of the object
print ProduceResponse.to_json()

# convert the object into a dict
produce_response_dict = produce_response_instance.to_dict()
# create an instance of ProduceResponse from a dict
produce_response_form_dict = produce_response.from_dict(produce_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


