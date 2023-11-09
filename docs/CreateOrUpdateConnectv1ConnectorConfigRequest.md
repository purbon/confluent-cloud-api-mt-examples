# CreateOrUpdateConnectv1ConnectorConfigRequest

Configuration parameters for the connector.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_class** | **str** | \\[Required for Managed Connector, Ignored for Custom Connector\\] The connector class name. E.g. BigQuerySink, GcsSink, etc. | 
**name** | **str** | Name or alias of the class (plugin) for this connector. | 
**kafka_api_key** | **str** | The kafka cluster api key. | 
**kafka_api_secret** | **str** | The kafka cluster api secret key. | 
**confluent_connector_type** | **str** | \\[Required for Custom Connector\\] The connector type.  | [optional] [default to 'MANAGED']
**confluent_custom_plugin_id** | **str** | \\[Required for Custom Connector\\] The custom plugin id of custom connector, e.g., &#x60;ccp-lq5m06&#x60;  | [optional] 
**confluent_custom_connection_endpoints** | **str** | \\[Optional for Custom Connector\\] Egress endpoint(s) for the connector to use when attaching to the sink or source data system.  | [optional] 
**confluent_custom_schema_registry_auto** | **str** | \\[Optional for Custom Connector\\] Automatically add the required schema registry properties in a custom connector config if schema registry is enabled.  | [optional] [default to 'FALSE']

## Example

```python
from openapi_client.models.create_or_update_connectv1_connector_config_request import CreateOrUpdateConnectv1ConnectorConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrUpdateConnectv1ConnectorConfigRequest from a JSON string
create_or_update_connectv1_connector_config_request_instance = CreateOrUpdateConnectv1ConnectorConfigRequest.from_json(json)
# print the JSON string representation of the object
print CreateOrUpdateConnectv1ConnectorConfigRequest.to_json()

# convert the object into a dict
create_or_update_connectv1_connector_config_request_dict = create_or_update_connectv1_connector_config_request_instance.to_dict()
# create an instance of CreateOrUpdateConnectv1ConnectorConfigRequest from a dict
create_or_update_connectv1_connector_config_request_form_dict = create_or_update_connectv1_connector_config_request.from_dict(create_or_update_connectv1_connector_config_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


