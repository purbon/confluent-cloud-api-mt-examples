# ConnectV1ConnectorExpansionId

The ID of connector.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the connector. | [optional] 
**id_type** | **str** | Type of the value in the &#x60;id&#x60; property. | [optional] 

## Example

```python
from openapi_client.models.connect_v1_connector_expansion_id import ConnectV1ConnectorExpansionId

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1ConnectorExpansionId from a JSON string
connect_v1_connector_expansion_id_instance = ConnectV1ConnectorExpansionId.from_json(json)
# print the JSON string representation of the object
print ConnectV1ConnectorExpansionId.to_json()

# convert the object into a dict
connect_v1_connector_expansion_id_dict = connect_v1_connector_expansion_id_instance.to_dict()
# create an instance of ConnectV1ConnectorExpansionId from a dict
connect_v1_connector_expansion_id_form_dict = connect_v1_connector_expansion_id.from_dict(connect_v1_connector_expansion_id_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


