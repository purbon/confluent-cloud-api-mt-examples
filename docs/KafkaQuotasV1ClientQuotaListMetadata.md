# KafkaQuotasV1ClientQuotaListMetadata


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
from openapi_client.models.kafka_quotas_v1_client_quota_list_metadata import KafkaQuotasV1ClientQuotaListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of KafkaQuotasV1ClientQuotaListMetadata from a JSON string
kafka_quotas_v1_client_quota_list_metadata_instance = KafkaQuotasV1ClientQuotaListMetadata.from_json(json)
# print the JSON string representation of the object
print KafkaQuotasV1ClientQuotaListMetadata.to_json()

# convert the object into a dict
kafka_quotas_v1_client_quota_list_metadata_dict = kafka_quotas_v1_client_quota_list_metadata_instance.to_dict()
# create an instance of KafkaQuotasV1ClientQuotaListMetadata from a dict
kafka_quotas_v1_client_quota_list_metadata_form_dict = kafka_quotas_v1_client_quota_list_metadata.from_dict(kafka_quotas_v1_client_quota_list_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


