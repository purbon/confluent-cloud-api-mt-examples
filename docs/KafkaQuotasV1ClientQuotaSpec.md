# KafkaQuotasV1ClientQuotaSpec

The desired state of the Client Quota

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the client quota. | [optional] 
**description** | **str** | A human readable description for the client quota. | [optional] 
**throughput** | [**KafkaQuotasV1Throughput**](KafkaQuotasV1Throughput.md) |  | [optional] 
**cluster** | [**EnvScopedObjectReference**](EnvScopedObjectReference.md) |  | [optional] 
**principals** | [**List[GlobalObjectReference]**](GlobalObjectReference.md) | A list of principals to apply a client quota to. Use &#x60;\&quot;&lt;default&gt;\&quot;&#x60; to apply a client quota to all service accounts (see [Control application usage with Client Quotas](https://docs.confluent.io/cloud/current/clusters/client-quotas.html#control-application-usage-with-client-quotas) for more details).  | [optional] 
**environment** | [**GlobalObjectReference**](GlobalObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.kafka_quotas_v1_client_quota_spec import KafkaQuotasV1ClientQuotaSpec

# TODO update the JSON string below
json = "{}"
# create an instance of KafkaQuotasV1ClientQuotaSpec from a JSON string
kafka_quotas_v1_client_quota_spec_instance = KafkaQuotasV1ClientQuotaSpec.from_json(json)
# print the JSON string representation of the object
print KafkaQuotasV1ClientQuotaSpec.to_json()

# convert the object into a dict
kafka_quotas_v1_client_quota_spec_dict = kafka_quotas_v1_client_quota_spec_instance.to_dict()
# create an instance of KafkaQuotasV1ClientQuotaSpec from a dict
kafka_quotas_v1_client_quota_spec_form_dict = kafka_quotas_v1_client_quota_spec.from_dict(kafka_quotas_v1_client_quota_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


