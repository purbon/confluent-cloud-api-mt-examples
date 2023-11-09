# KafkaQuotasV1ClientQuotaSpecUpdate

The desired state of the Client Quota

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the client quota. | [optional] 
**description** | **str** | A human readable description for the client quota. | [optional] 
**throughput** | [**KafkaQuotasV1Throughput**](KafkaQuotasV1Throughput.md) |  | [optional] 
**principals** | [**List[GlobalObjectReference]**](GlobalObjectReference.md) | A list of principals to apply a client quota to. Use &#x60;\&quot;&lt;default&gt;\&quot;&#x60; to apply a client quota to all service accounts (see [Control application usage with Client Quotas](https://docs.confluent.io/cloud/current/clusters/client-quotas.html#control-application-usage-with-client-quotas) for more details).  | [optional] 

## Example

```python
from openapi_client.models.kafka_quotas_v1_client_quota_spec_update import KafkaQuotasV1ClientQuotaSpecUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of KafkaQuotasV1ClientQuotaSpecUpdate from a JSON string
kafka_quotas_v1_client_quota_spec_update_instance = KafkaQuotasV1ClientQuotaSpecUpdate.from_json(json)
# print the JSON string representation of the object
print KafkaQuotasV1ClientQuotaSpecUpdate.to_json()

# convert the object into a dict
kafka_quotas_v1_client_quota_spec_update_dict = kafka_quotas_v1_client_quota_spec_update_instance.to_dict()
# create an instance of KafkaQuotasV1ClientQuotaSpecUpdate from a dict
kafka_quotas_v1_client_quota_spec_update_form_dict = kafka_quotas_v1_client_quota_spec_update.from_dict(kafka_quotas_v1_client_quota_spec_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


