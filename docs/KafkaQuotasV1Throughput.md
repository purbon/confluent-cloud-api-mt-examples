# KafkaQuotasV1Throughput

Quotas on maximum throughput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingress_byte_rate** | **str** | Ingress throughput limit for principals specified in bytes per second. | 
**egress_byte_rate** | **str** | Egress throughput limit for principals specified in bytes per second. | 

## Example

```python
from openapi_client.models.kafka_quotas_v1_throughput import KafkaQuotasV1Throughput

# TODO update the JSON string below
json = "{}"
# create an instance of KafkaQuotasV1Throughput from a JSON string
kafka_quotas_v1_throughput_instance = KafkaQuotasV1Throughput.from_json(json)
# print the JSON string representation of the object
print KafkaQuotasV1Throughput.to_json()

# convert the object into a dict
kafka_quotas_v1_throughput_dict = kafka_quotas_v1_throughput_instance.to_dict()
# create an instance of KafkaQuotasV1Throughput from a dict
kafka_quotas_v1_throughput_form_dict = kafka_quotas_v1_throughput.from_dict(kafka_quotas_v1_throughput_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


