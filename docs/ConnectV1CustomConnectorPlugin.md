# ConnectV1CustomConnectorPlugin

CustomConnectorPlugins objects represent Custom Connector Plugins on Confluent Cloud. The API allows you to list, create, read, update, and delete your Custom Connector Plugins. Related guide: [Custom Connector Plugin API](https://docs.confluent.io/cloud/current/connectors/connect-api-section.html).   ## The Custom Connector Plugins Model <SchemaDefinition schemaRef=\"#/components/schemas/connect.v1.CustomConnectorPlugin\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**ConnectV1CustomConnectorPluginMetadata**](ConnectV1CustomConnectorPluginMetadata.md) |  | [optional] 
**display_name** | **str** | Display name of Custom Connector Plugin. | [optional] 
**content_format** | **str** | Archive format of Custom Connector Plugin. | [optional] [readonly] 
**description** | **str** | Description of Custom Connector Plugin. | [optional] 
**documentation_link** | **str** | Document link of Custom Connector Plugin. | [optional] 
**connector_class** | **str** | Java class or alias for connector. You can get connector class from connector documentation provided by developer. | [optional] 
**connector_type** | **str** | Custom Connector type.  | [optional] 
**sensitive_config_properties** | **List[str]** | A sensitive property is a connector configuration property that must be hidden after a user enters property value when setting up connector. | [optional] 
**upload_source** | [**ConnectV1CustomConnectorPluginUploadSource**](ConnectV1CustomConnectorPluginUploadSource.md) |  | [optional] 

## Example

```python
from openapi_client.models.connect_v1_custom_connector_plugin import ConnectV1CustomConnectorPlugin

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1CustomConnectorPlugin from a JSON string
connect_v1_custom_connector_plugin_instance = ConnectV1CustomConnectorPlugin.from_json(json)
# print the JSON string representation of the object
print ConnectV1CustomConnectorPlugin.to_json()

# convert the object into a dict
connect_v1_custom_connector_plugin_dict = connect_v1_custom_connector_plugin_instance.to_dict()
# create an instance of ConnectV1CustomConnectorPlugin from a dict
connect_v1_custom_connector_plugin_form_dict = connect_v1_custom_connector_plugin.from_dict(connect_v1_custom_connector_plugin_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


