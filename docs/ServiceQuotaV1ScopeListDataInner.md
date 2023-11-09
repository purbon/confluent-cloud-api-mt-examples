# ServiceQuotaV1ScopeListDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**metadata** | [**ServiceQuotaV1ScopeMetadata**](ServiceQuotaV1ScopeMetadata.md) |  | 
**description** | **str** | the quota scope for listing quotas queries | 

## Example

```python
from openapi_client.models.service_quota_v1_scope_list_data_inner import ServiceQuotaV1ScopeListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQuotaV1ScopeListDataInner from a JSON string
service_quota_v1_scope_list_data_inner_instance = ServiceQuotaV1ScopeListDataInner.from_json(json)
# print the JSON string representation of the object
print ServiceQuotaV1ScopeListDataInner.to_json()

# convert the object into a dict
service_quota_v1_scope_list_data_inner_dict = service_quota_v1_scope_list_data_inner_instance.to_dict()
# create an instance of ServiceQuotaV1ScopeListDataInner from a dict
service_quota_v1_scope_list_data_inner_form_dict = service_quota_v1_scope_list_data_inner.from_dict(service_quota_v1_scope_list_data_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


