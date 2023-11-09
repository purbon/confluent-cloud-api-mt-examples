# KafkaQuotasV1ClientQuotaUpdate

`ClientQuota` objects represent Client Quotas you can set at the service account level.  The API allows you to list, create, read, update, and delete your client quotas.   Related guide: [Client Quotas in Confluent Cloud](https://docs.confluent.io/cloud/current/clusters/client-quotas.html).  ## The Client Quotas Model <SchemaDefinition schemaRef=\"#/components/schemas/kafka-quotas.v1.ClientQuota\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**KafkaQuotasV1ClientQuotaMetadata**](KafkaQuotasV1ClientQuotaMetadata.md) |  | [optional] 
**spec** | [**KafkaQuotasV1ClientQuotaSpecUpdate**](KafkaQuotasV1ClientQuotaSpecUpdate.md) |  | [optional] 

## Example

```python
from openapi_client.models.kafka_quotas_v1_client_quota_update import KafkaQuotasV1ClientQuotaUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of KafkaQuotasV1ClientQuotaUpdate from a JSON string
kafka_quotas_v1_client_quota_update_instance = KafkaQuotasV1ClientQuotaUpdate.from_json(json)
# print the JSON string representation of the object
print KafkaQuotasV1ClientQuotaUpdate.to_json()

# convert the object into a dict
kafka_quotas_v1_client_quota_update_dict = kafka_quotas_v1_client_quota_update_instance.to_dict()
# create an instance of KafkaQuotasV1ClientQuotaUpdate from a dict
kafka_quotas_v1_client_quota_update_form_dict = kafka_quotas_v1_client_quota_update.from_dict(kafka_quotas_v1_client_quota_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


