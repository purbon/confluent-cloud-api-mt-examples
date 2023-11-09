# KafkaQuotasV1ClientQuotaList

`ClientQuota` objects represent Client Quotas you can set at the service account level.  The API allows you to list, create, read, update, and delete your client quotas.   Related guide: [Client Quotas in Confluent Cloud](https://docs.confluent.io/cloud/current/clusters/client-quotas.html).  ## The Client Quotas Model <SchemaDefinition schemaRef=\"#/components/schemas/kafka-quotas.v1.ClientQuota\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**KafkaQuotasV1ClientQuotaListMetadata**](KafkaQuotasV1ClientQuotaListMetadata.md) |  | 
**data** | [**List[KafkaQuotasV1ClientQuotaListDataInner]**](KafkaQuotasV1ClientQuotaListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.kafka_quotas_v1_client_quota_list import KafkaQuotasV1ClientQuotaList

# TODO update the JSON string below
json = "{}"
# create an instance of KafkaQuotasV1ClientQuotaList from a JSON string
kafka_quotas_v1_client_quota_list_instance = KafkaQuotasV1ClientQuotaList.from_json(json)
# print the JSON string representation of the object
print KafkaQuotasV1ClientQuotaList.to_json()

# convert the object into a dict
kafka_quotas_v1_client_quota_list_dict = kafka_quotas_v1_client_quota_list_instance.to_dict()
# create an instance of KafkaQuotasV1ClientQuotaList from a dict
kafka_quotas_v1_client_quota_list_form_dict = kafka_quotas_v1_client_quota_list.from_dict(kafka_quotas_v1_client_quota_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


