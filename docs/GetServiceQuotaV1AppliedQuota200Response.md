# GetServiceQuotaV1AppliedQuota200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**metadata** | [**ServiceQuotaV1AppliedQuotaMetadata**](ServiceQuotaV1AppliedQuotaMetadata.md) |  | [optional] 
**scope** | **str** | The applied scope that this quota belongs to. | 
**display_name** | **str** | A human-readable name for the quota type name. | 
**default_limit** | **int** | The default service quota value.  | 
**applied_limit** | **int** | The latest applied service quota value, taking into account any limit adjustments.  | 
**usage** | **int** | Show the quota usage value if the quota usage is available for this quota.  | [optional] 
**user** | **object** |  | [optional] 
**organization** | **object** |  | [optional] 
**environment** | **object** |  | [optional] 
**network** | **object** |  | [optional] 
**kafka_cluster** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.get_service_quota_v1_applied_quota200_response import GetServiceQuotaV1AppliedQuota200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetServiceQuotaV1AppliedQuota200Response from a JSON string
get_service_quota_v1_applied_quota200_response_instance = GetServiceQuotaV1AppliedQuota200Response.from_json(json)
# print the JSON string representation of the object
print GetServiceQuotaV1AppliedQuota200Response.to_json()

# convert the object into a dict
get_service_quota_v1_applied_quota200_response_dict = get_service_quota_v1_applied_quota200_response_instance.to_dict()
# create an instance of GetServiceQuotaV1AppliedQuota200Response from a dict
get_service_quota_v1_applied_quota200_response_form_dict = get_service_quota_v1_applied_quota200_response.from_dict(get_service_quota_v1_applied_quota200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


