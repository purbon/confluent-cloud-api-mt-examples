# ListConnectv1ConnectorPlugins200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | **str** | The connector class name. E.g. BigQuerySink. | 
**type** | **str** | Type of connector, sink or source. | 
**version** | **str** | The version string for the connector available. | [optional] 

## Example

```python
from openapi_client.models.list_connectv1_connector_plugins200_response_inner import ListConnectv1ConnectorPlugins200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListConnectv1ConnectorPlugins200ResponseInner from a JSON string
list_connectv1_connector_plugins200_response_inner_instance = ListConnectv1ConnectorPlugins200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ListConnectv1ConnectorPlugins200ResponseInner.to_json()

# convert the object into a dict
list_connectv1_connector_plugins200_response_inner_dict = list_connectv1_connector_plugins200_response_inner_instance.to_dict()
# create an instance of ListConnectv1ConnectorPlugins200ResponseInner from a dict
list_connectv1_connector_plugins200_response_inner_form_dict = list_connectv1_connector_plugins200_response_inner.from_dict(list_connectv1_connector_plugins200_response_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


