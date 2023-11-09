# GetConnectv1ConnectorConfig200Response

Configuration parameters for the connector.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_environment** | **str** | The cloud environment type. | 
**cloud_provider** | **str** | The cloud service provider, e.g. aws, azure, etc. | 
**connector_class** | **str** | The connector class name. E.g. BigQuerySink, GcsSink, etc. | 
**name** | **str** | Name or alias of the class (plugin) for this connector. For Custom Connector, it must be the same as connector_name. | 
**kafka_endpoint** | **str** | The kafka cluster endpoint. | 
**kafka_region** | **str** | The kafka cluster region. | 
**kafka_api_key** | **str** | The kafka cluster api key. | 
**kafka_api_secret** | **str** | The kafka cluster api secret key. | 

## Example

```python
from openapi_client.models.get_connectv1_connector_config200_response import GetConnectv1ConnectorConfig200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetConnectv1ConnectorConfig200Response from a JSON string
get_connectv1_connector_config200_response_instance = GetConnectv1ConnectorConfig200Response.from_json(json)
# print the JSON string representation of the object
print GetConnectv1ConnectorConfig200Response.to_json()

# convert the object into a dict
get_connectv1_connector_config200_response_dict = get_connectv1_connector_config200_response_instance.to_dict()
# create an instance of GetConnectv1ConnectorConfig200Response from a dict
get_connectv1_connector_config200_response_form_dict = get_connectv1_connector_config200_response.from_dict(get_connectv1_connector_config200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


