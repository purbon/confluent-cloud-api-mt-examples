# ServiceQuotaV1ScopeList

Gets a list of all available scopes for applied quotas.   Related guide: [Quota Scopes](https://docs.confluent.io/cloud/current/quotas/quotas.html#query-for-scopes).  ## The Scopes Model <SchemaDefinition schemaRef=\"#/components/schemas/service-quota.v1.Scope\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**ServiceQuotaV1ScopeListMetadata**](ServiceQuotaV1ScopeListMetadata.md) |  | 
**data** | [**List[ServiceQuotaV1ScopeListDataInner]**](ServiceQuotaV1ScopeListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.service_quota_v1_scope_list import ServiceQuotaV1ScopeList

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQuotaV1ScopeList from a JSON string
service_quota_v1_scope_list_instance = ServiceQuotaV1ScopeList.from_json(json)
# print the JSON string representation of the object
print ServiceQuotaV1ScopeList.to_json()

# convert the object into a dict
service_quota_v1_scope_list_dict = service_quota_v1_scope_list_instance.to_dict()
# create an instance of ServiceQuotaV1ScopeList from a dict
service_quota_v1_scope_list_form_dict = service_quota_v1_scope_list.from_dict(service_quota_v1_scope_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


