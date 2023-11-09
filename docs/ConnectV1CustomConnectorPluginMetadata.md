# ConnectV1CustomConnectorPluginMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **object** |  | 
**resource_name** | **object** |  | [optional] 
**created_at** | **datetime** | The date and time at which this object was created. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**updated_at** | **datetime** | The date and time at which this object was last updated. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**deleted_at** | **datetime** | The date and time at which this object was (or will be) deleted. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 

## Example

```python
from openapi_client.models.connect_v1_custom_connector_plugin_metadata import ConnectV1CustomConnectorPluginMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1CustomConnectorPluginMetadata from a JSON string
connect_v1_custom_connector_plugin_metadata_instance = ConnectV1CustomConnectorPluginMetadata.from_json(json)
# print the JSON string representation of the object
print ConnectV1CustomConnectorPluginMetadata.to_json()

# convert the object into a dict
connect_v1_custom_connector_plugin_metadata_dict = connect_v1_custom_connector_plugin_metadata_instance.to_dict()
# create an instance of ConnectV1CustomConnectorPluginMetadata from a dict
connect_v1_custom_connector_plugin_metadata_form_dict = connect_v1_custom_connector_plugin_metadata.from_dict(connect_v1_custom_connector_plugin_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


