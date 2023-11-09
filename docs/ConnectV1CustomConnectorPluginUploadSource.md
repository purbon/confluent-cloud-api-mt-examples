# ConnectV1CustomConnectorPluginUploadSource

[immutable] Upload source of Custom Connector Plugin. Only required in `create` request, will be ignored in `read`, `update` or `list`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | Location of the Custom Connector Plugin source.  | 
**upload_id** | **str** | Upload ID returned by the &#x60;/presigned-upload-url&#x60; API. This field returns an empty string in all responses. | 

## Example

```python
from openapi_client.models.connect_v1_custom_connector_plugin_upload_source import ConnectV1CustomConnectorPluginUploadSource

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1CustomConnectorPluginUploadSource from a JSON string
connect_v1_custom_connector_plugin_upload_source_instance = ConnectV1CustomConnectorPluginUploadSource.from_json(json)
# print the JSON string representation of the object
print ConnectV1CustomConnectorPluginUploadSource.to_json()

# convert the object into a dict
connect_v1_custom_connector_plugin_upload_source_dict = connect_v1_custom_connector_plugin_upload_source_instance.to_dict()
# create an instance of ConnectV1CustomConnectorPluginUploadSource from a dict
connect_v1_custom_connector_plugin_upload_source_form_dict = connect_v1_custom_connector_plugin_upload_source.from_dict(connect_v1_custom_connector_plugin_upload_source_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


