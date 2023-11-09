# ServiceQuotaV1ScopeMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **object** |  | 
**resource_name** | **object** |  | [optional] 
**created_at** | **datetime** | The date and time at which this object was created. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**updated_at** | **datetime** | The date and time at which this object was last updated. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**deleted_at** | **datetime** | The date and time at which this object was (or will be) deleted. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 

## Example

```python
from openapi_client.models.service_quota_v1_scope_metadata import ServiceQuotaV1ScopeMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQuotaV1ScopeMetadata from a JSON string
service_quota_v1_scope_metadata_instance = ServiceQuotaV1ScopeMetadata.from_json(json)
# print the JSON string representation of the object
print ServiceQuotaV1ScopeMetadata.to_json()

# convert the object into a dict
service_quota_v1_scope_metadata_dict = service_quota_v1_scope_metadata_instance.to_dict()
# create an instance of ServiceQuotaV1ScopeMetadata from a dict
service_quota_v1_scope_metadata_form_dict = service_quota_v1_scope_metadata.from_dict(service_quota_v1_scope_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


