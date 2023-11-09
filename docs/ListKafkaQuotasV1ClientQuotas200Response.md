# ListKafkaQuotasV1ClientQuotas200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**KafkaQuotasV1ClientQuotaListMetadata**](KafkaQuotasV1ClientQuotaListMetadata.md) |  | 
**data** | [**List[ListKafkaQuotasV1ClientQuotas200ResponseAllOfDataInner]**](ListKafkaQuotasV1ClientQuotas200ResponseAllOfDataInner.md) |  | 

## Example

```python
from openapi_client.models.list_kafka_quotas_v1_client_quotas200_response import ListKafkaQuotasV1ClientQuotas200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListKafkaQuotasV1ClientQuotas200Response from a JSON string
list_kafka_quotas_v1_client_quotas200_response_instance = ListKafkaQuotasV1ClientQuotas200Response.from_json(json)
# print the JSON string representation of the object
print ListKafkaQuotasV1ClientQuotas200Response.to_json()

# convert the object into a dict
list_kafka_quotas_v1_client_quotas200_response_dict = list_kafka_quotas_v1_client_quotas200_response_instance.to_dict()
# create an instance of ListKafkaQuotasV1ClientQuotas200Response from a dict
list_kafka_quotas_v1_client_quotas200_response_form_dict = list_kafka_quotas_v1_client_quotas200_response.from_dict(list_kafka_quotas_v1_client_quotas200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


