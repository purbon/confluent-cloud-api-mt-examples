# ProduceRequestHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **bytearray** |  | [optional] 

## Example

```python
from openapi_client.models.produce_request_header import ProduceRequestHeader

# TODO update the JSON string below
json = "{}"
# create an instance of ProduceRequestHeader from a JSON string
produce_request_header_instance = ProduceRequestHeader.from_json(json)
# print the JSON string representation of the object
print ProduceRequestHeader.to_json()

# convert the object into a dict
produce_request_header_dict = produce_request_header_instance.to_dict()
# create an instance of ProduceRequestHeader from a dict
produce_request_header_form_dict = produce_request_header.from_dict(produce_request_header_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


