# CreateKafkaQuotasV1ClientQuotaRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**KafkaQuotasV1ClientQuotaMetadata**](KafkaQuotasV1ClientQuotaMetadata.md) |  | [optional] 
**spec** | [**CreateKafkaQuotasV1ClientQuotaRequestAllOfSpec**](CreateKafkaQuotasV1ClientQuotaRequestAllOfSpec.md) |  | 

## Example

```python
from openapi_client.models.create_kafka_quotas_v1_client_quota_request import CreateKafkaQuotasV1ClientQuotaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKafkaQuotasV1ClientQuotaRequest from a JSON string
create_kafka_quotas_v1_client_quota_request_instance = CreateKafkaQuotasV1ClientQuotaRequest.from_json(json)
# print the JSON string representation of the object
print CreateKafkaQuotasV1ClientQuotaRequest.to_json()

# convert the object into a dict
create_kafka_quotas_v1_client_quota_request_dict = create_kafka_quotas_v1_client_quota_request_instance.to_dict()
# create an instance of CreateKafkaQuotasV1ClientQuotaRequest from a dict
create_kafka_quotas_v1_client_quota_request_form_dict = create_kafka_quotas_v1_client_quota_request.from_dict(create_kafka_quotas_v1_client_quota_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


