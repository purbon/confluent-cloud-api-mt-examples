# ConnectV1ConnectorExpansion

Name of connector

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ConnectV1ConnectorExpansionId**](ConnectV1ConnectorExpansionId.md) |  | [optional] 
**info** | [**ConnectV1ConnectorExpansionInfo**](ConnectV1ConnectorExpansionInfo.md) |  | [optional] 
**status** | [**ConnectV1ConnectorExpansionStatus**](ConnectV1ConnectorExpansionStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.connect_v1_connector_expansion import ConnectV1ConnectorExpansion

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1ConnectorExpansion from a JSON string
connect_v1_connector_expansion_instance = ConnectV1ConnectorExpansion.from_json(json)
# print the JSON string representation of the object
print ConnectV1ConnectorExpansion.to_json()

# convert the object into a dict
connect_v1_connector_expansion_dict = connect_v1_connector_expansion_instance.to_dict()
# create an instance of ConnectV1ConnectorExpansion from a dict
connect_v1_connector_expansion_form_dict = connect_v1_connector_expansion.from_dict(connect_v1_connector_expansion_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


