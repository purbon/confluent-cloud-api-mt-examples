# ConnectV1ConnectorsInnerConfig

Configuration parameters for the connector. These configurations are the minimum set of key-value pairs (KVP) which can be used to define how the connector connects Kafka to the external system. Some of these KVPs are common to all the connectors, such as connection parameters to Kafka, connector metadata, etc. The list of common connector configurations is as follows    - cloud.environment   - cloud.provider   - connector.class   - kafka.api.key   - kafka.api.secret   - kafka.endpoint   - kafka.region   - name  A specific connector such as `GcsSink` would have additional parameters such as `gcs.bucket.name`, `flush.size`, etc.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_environment** | **str** | The cloud environment type. | 
**cloud_provider** | **str** | The cloud service provider, e.g. aws, azure, etc. | 
**connector_class** | **str** | The connector class name. E.g. BigQuerySink, GcsSink, etc. | 
**name** | **str** | Name or alias of the class (plugin) for this connector. | 
**kafka_endpoint** | **str** | The kafka cluster endpoint. | 
**kafka_region** | **str** | The kafka cluster region. | 
**kafka_api_key** | **str** | The kafka cluster api key. | 
**kafka_api_secret** | **str** | The kafka cluster api secret key. | 

## Example

```python
from openapi_client.models.connect_v1_connectors_inner_config import ConnectV1ConnectorsInnerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1ConnectorsInnerConfig from a JSON string
connect_v1_connectors_inner_config_instance = ConnectV1ConnectorsInnerConfig.from_json(json)
# print the JSON string representation of the object
print ConnectV1ConnectorsInnerConfig.to_json()

# convert the object into a dict
connect_v1_connectors_inner_config_dict = connect_v1_connectors_inner_config_instance.to_dict()
# create an instance of ConnectV1ConnectorsInnerConfig from a dict
connect_v1_connectors_inner_config_form_dict = connect_v1_connectors_inner_config.from_dict(connect_v1_connectors_inner_config_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


