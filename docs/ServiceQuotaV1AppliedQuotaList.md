# ServiceQuotaV1AppliedQuotaList

A `quota` object represents a quota configuration for a specific Confluent Cloud resource. Use this API to retrieve an individual quota or list of quotas for a given scope.   Related guide: [Service Quotas for Confluent Cloud](https://docs.confluent.io/cloud/current/quotas/index.html).  ## The Applied Quotas Model <SchemaDefinition schemaRef=\"#/components/schemas/service-quota.v1.AppliedQuota\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**ServiceQuotaV1AppliedQuotaListMetadata**](ServiceQuotaV1AppliedQuotaListMetadata.md) |  | 
**data** | [**List[ServiceQuotaV1AppliedQuotaListDataInner]**](ServiceQuotaV1AppliedQuotaListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.service_quota_v1_applied_quota_list import ServiceQuotaV1AppliedQuotaList

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQuotaV1AppliedQuotaList from a JSON string
service_quota_v1_applied_quota_list_instance = ServiceQuotaV1AppliedQuotaList.from_json(json)
# print the JSON string representation of the object
print ServiceQuotaV1AppliedQuotaList.to_json()

# convert the object into a dict
service_quota_v1_applied_quota_list_dict = service_quota_v1_applied_quota_list_instance.to_dict()
# create an instance of ServiceQuotaV1AppliedQuotaList from a dict
service_quota_v1_applied_quota_list_form_dict = service_quota_v1_applied_quota_list.from_dict(service_quota_v1_applied_quota_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


