# ConnectV1ConnectorsInnerId

The ID of task.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector** | **str** | The name of the connector the task belongs to. | [optional] 
**task** | **int** | Task ID within the connector. | [optional] 

## Example

```python
from openapi_client.models.connect_v1_connectors_inner_id import ConnectV1ConnectorsInnerId

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1ConnectorsInnerId from a JSON string
connect_v1_connectors_inner_id_instance = ConnectV1ConnectorsInnerId.from_json(json)
# print the JSON string representation of the object
print ConnectV1ConnectorsInnerId.to_json()

# convert the object into a dict
connect_v1_connectors_inner_id_dict = connect_v1_connectors_inner_id_instance.to_dict()
# create an instance of ConnectV1ConnectorsInnerId from a dict
connect_v1_connectors_inner_id_form_dict = connect_v1_connectors_inner_id.from_dict(connect_v1_connectors_inner_id_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


