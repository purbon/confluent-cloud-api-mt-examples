# ServiceQuotaV1AppliedQuotaKafkaCluster

The kafka cluster ID the quota is associated with. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the referred resource | 
**environment** | **str** | Environment of the referred resource, if env-scoped | [optional] 
**related** | **str** | API URL for accessing or modifying the referred object | [readonly] 
**resource_name** | **str** | CRN reference to the referred resource | [readonly] 

## Example

```python
from openapi_client.models.service_quota_v1_applied_quota_kafka_cluster import ServiceQuotaV1AppliedQuotaKafkaCluster

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQuotaV1AppliedQuotaKafkaCluster from a JSON string
service_quota_v1_applied_quota_kafka_cluster_instance = ServiceQuotaV1AppliedQuotaKafkaCluster.from_json(json)
# print the JSON string representation of the object
print ServiceQuotaV1AppliedQuotaKafkaCluster.to_json()

# convert the object into a dict
service_quota_v1_applied_quota_kafka_cluster_dict = service_quota_v1_applied_quota_kafka_cluster_instance.to_dict()
# create an instance of ServiceQuotaV1AppliedQuotaKafkaCluster from a dict
service_quota_v1_applied_quota_kafka_cluster_form_dict = service_quota_v1_applied_quota_kafka_cluster.from_dict(service_quota_v1_applied_quota_kafka_cluster_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


