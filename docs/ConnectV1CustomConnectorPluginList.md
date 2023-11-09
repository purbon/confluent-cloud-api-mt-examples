# ConnectV1CustomConnectorPluginList

CustomConnectorPlugins objects represent Custom Connector Plugins on Confluent Cloud. The API allows you to list, create, read, update, and delete your Custom Connector Plugins. Related guide: [Custom Connector Plugin API](https://docs.confluent.io/cloud/current/connectors/connect-api-section.html).   ## The Custom Connector Plugins Model <SchemaDefinition schemaRef=\"#/components/schemas/connect.v1.CustomConnectorPlugin\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**ConnectV1CustomConnectorPluginListMetadata**](ConnectV1CustomConnectorPluginListMetadata.md) |  | 
**data** | [**List[ConnectV1CustomConnectorPluginListDataInner]**](ConnectV1CustomConnectorPluginListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.connect_v1_custom_connector_plugin_list import ConnectV1CustomConnectorPluginList

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1CustomConnectorPluginList from a JSON string
connect_v1_custom_connector_plugin_list_instance = ConnectV1CustomConnectorPluginList.from_json(json)
# print the JSON string representation of the object
print ConnectV1CustomConnectorPluginList.to_json()

# convert the object into a dict
connect_v1_custom_connector_plugin_list_dict = connect_v1_custom_connector_plugin_list_instance.to_dict()
# create an instance of ConnectV1CustomConnectorPluginList from a dict
connect_v1_custom_connector_plugin_list_form_dict = connect_v1_custom_connector_plugin_list.from_dict(connect_v1_custom_connector_plugin_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


