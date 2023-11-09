# ServiceQuotaV1AppliedQuota

A `quota` object represents a quota configuration for a specific Confluent Cloud resource. Use this API to retrieve an individual quota or list of quotas for a given scope.   Related guide: [Service Quotas for Confluent Cloud](https://docs.confluent.io/cloud/current/quotas/index.html).  ## The Applied Quotas Model <SchemaDefinition schemaRef=\"#/components/schemas/service-quota.v1.AppliedQuota\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**ServiceQuotaV1AppliedQuotaMetadata**](ServiceQuotaV1AppliedQuotaMetadata.md) |  | [optional] 
**scope** | **str** | The applied scope that this quota belongs to. | [optional] 
**display_name** | **str** | A human-readable name for the quota type name. | [optional] 
**default_limit** | **int** | The default service quota value.  | [optional] 
**applied_limit** | **int** | The latest applied service quota value, taking into account any limit adjustments.  | [optional] 
**usage** | **int** | Show the quota usage value if the quota usage is available for this quota.  | [optional] 
**user** | [**GlobalObjectReference**](GlobalObjectReference.md) |  | [optional] 
**organization** | [**ServiceQuotaV1AppliedQuotaOrganization**](ServiceQuotaV1AppliedQuotaOrganization.md) |  | [optional] 
**environment** | [**ServiceQuotaV1AppliedQuotaEnvironment**](ServiceQuotaV1AppliedQuotaEnvironment.md) |  | [optional] 
**network** | [**ServiceQuotaV1AppliedQuotaNetwork**](ServiceQuotaV1AppliedQuotaNetwork.md) |  | [optional] 
**kafka_cluster** | [**ServiceQuotaV1AppliedQuotaKafkaCluster**](ServiceQuotaV1AppliedQuotaKafkaCluster.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_quota_v1_applied_quota import ServiceQuotaV1AppliedQuota

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQuotaV1AppliedQuota from a JSON string
service_quota_v1_applied_quota_instance = ServiceQuotaV1AppliedQuota.from_json(json)
# print the JSON string representation of the object
print ServiceQuotaV1AppliedQuota.to_json()

# convert the object into a dict
service_quota_v1_applied_quota_dict = service_quota_v1_applied_quota_instance.to_dict()
# create an instance of ServiceQuotaV1AppliedQuota from a dict
service_quota_v1_applied_quota_form_dict = service_quota_v1_applied_quota.from_dict(service_quota_v1_applied_quota_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


