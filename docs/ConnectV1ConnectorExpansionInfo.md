# ConnectV1ConnectorExpansionInfo

Metadata of the connector.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the connector. | [optional] 
**config** | [**ConnectV1ConnectorExpansionInfoConfig**](ConnectV1ConnectorExpansionInfoConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.connect_v1_connector_expansion_info import ConnectV1ConnectorExpansionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1ConnectorExpansionInfo from a JSON string
connect_v1_connector_expansion_info_instance = ConnectV1ConnectorExpansionInfo.from_json(json)
# print the JSON string representation of the object
print ConnectV1ConnectorExpansionInfo.to_json()

# convert the object into a dict
connect_v1_connector_expansion_info_dict = connect_v1_connector_expansion_info_instance.to_dict()
# create an instance of ConnectV1ConnectorExpansionInfo from a dict
connect_v1_connector_expansion_info_form_dict = connect_v1_connector_expansion_info.from_dict(connect_v1_connector_expansion_info_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


