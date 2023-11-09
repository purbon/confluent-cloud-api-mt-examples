# KafkaQuotasV1ClientQuotaMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **object** |  | 
**resource_name** | **object** |  | [optional] 
**created_at** | **datetime** | The date and time at which this object was created. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**updated_at** | **datetime** | The date and time at which this object was last updated. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**deleted_at** | **datetime** | The date and time at which this object was (or will be) deleted. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 

## Example

```python
from openapi_client.models.kafka_quotas_v1_client_quota_metadata import KafkaQuotasV1ClientQuotaMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of KafkaQuotasV1ClientQuotaMetadata from a JSON string
kafka_quotas_v1_client_quota_metadata_instance = KafkaQuotasV1ClientQuotaMetadata.from_json(json)
# print the JSON string representation of the object
print KafkaQuotasV1ClientQuotaMetadata.to_json()

# convert the object into a dict
kafka_quotas_v1_client_quota_metadata_dict = kafka_quotas_v1_client_quota_metadata_instance.to_dict()
# create an instance of KafkaQuotasV1ClientQuotaMetadata from a dict
kafka_quotas_v1_client_quota_metadata_form_dict = kafka_quotas_v1_client_quota_metadata.from_dict(kafka_quotas_v1_client_quota_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


