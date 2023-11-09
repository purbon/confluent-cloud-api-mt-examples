# ServiceQuotaV1ScopeListMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **object** |  | [optional] 
**last** | **object** |  | [optional] 
**prev** | **object** |  | [optional] 
**next** | **object** |  | [optional] 
**total_size** | **int** | Number of records in the full result set. This response may be paginated and have a smaller number of records. | [optional] 

## Example

```python
from openapi_client.models.service_quota_v1_scope_list_metadata import ServiceQuotaV1ScopeListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQuotaV1ScopeListMetadata from a JSON string
service_quota_v1_scope_list_metadata_instance = ServiceQuotaV1ScopeListMetadata.from_json(json)
# print the JSON string representation of the object
print ServiceQuotaV1ScopeListMetadata.to_json()

# convert the object into a dict
service_quota_v1_scope_list_metadata_dict = service_quota_v1_scope_list_metadata_instance.to_dict()
# create an instance of ServiceQuotaV1ScopeListMetadata from a dict
service_quota_v1_scope_list_metadata_form_dict = service_quota_v1_scope_list_metadata.from_dict(service_quota_v1_scope_list_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


