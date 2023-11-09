# ConnectV1ConnectorsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ConnectV1ConnectorsInnerId**](ConnectV1ConnectorsInnerId.md) |  | [optional] 
**config** | [**ConnectV1ConnectorsInnerConfig**](ConnectV1ConnectorsInnerConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.connect_v1_connectors_inner import ConnectV1ConnectorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1ConnectorsInner from a JSON string
connect_v1_connectors_inner_instance = ConnectV1ConnectorsInner.from_json(json)
# print the JSON string representation of the object
print ConnectV1ConnectorsInner.to_json()

# convert the object into a dict
connect_v1_connectors_inner_dict = connect_v1_connectors_inner_instance.to_dict()
# create an instance of ConnectV1ConnectorsInner from a dict
connect_v1_connectors_inner_form_dict = connect_v1_connectors_inner.from_dict(connect_v1_connectors_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


