# ConnectV1CustomConnectorPluginListMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **object** |  | [optional] 
**last** | **object** |  | [optional] 
**prev** | **object** |  | [optional] 
**next** | **object** |  | [optional] 
**total_size** | **int** | Number of records in the full result set. This response may be paginated and have a smaller number of records. | [optional] 

## Example

```python
from openapi_client.models.connect_v1_custom_connector_plugin_list_metadata import ConnectV1CustomConnectorPluginListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1CustomConnectorPluginListMetadata from a JSON string
connect_v1_custom_connector_plugin_list_metadata_instance = ConnectV1CustomConnectorPluginListMetadata.from_json(json)
# print the JSON string representation of the object
print ConnectV1CustomConnectorPluginListMetadata.to_json()

# convert the object into a dict
connect_v1_custom_connector_plugin_list_metadata_dict = connect_v1_custom_connector_plugin_list_metadata_instance.to_dict()
# create an instance of ConnectV1CustomConnectorPluginListMetadata from a dict
connect_v1_custom_connector_plugin_list_metadata_form_dict = connect_v1_custom_connector_plugin_list_metadata.from_dict(connect_v1_custom_connector_plugin_list_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


