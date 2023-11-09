# ListServiceQuotaV1AppliedQuotas200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**ServiceQuotaV1AppliedQuotaListMetadata**](ServiceQuotaV1AppliedQuotaListMetadata.md) |  | 
**data** | [**List[ListServiceQuotaV1AppliedQuotas200ResponseAllOfDataInner]**](ListServiceQuotaV1AppliedQuotas200ResponseAllOfDataInner.md) |  | 

## Example

```python
from openapi_client.models.list_service_quota_v1_applied_quotas200_response import ListServiceQuotaV1AppliedQuotas200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListServiceQuotaV1AppliedQuotas200Response from a JSON string
list_service_quota_v1_applied_quotas200_response_instance = ListServiceQuotaV1AppliedQuotas200Response.from_json(json)
# print the JSON string representation of the object
print ListServiceQuotaV1AppliedQuotas200Response.to_json()

# convert the object into a dict
list_service_quota_v1_applied_quotas200_response_dict = list_service_quota_v1_applied_quotas200_response_instance.to_dict()
# create an instance of ListServiceQuotaV1AppliedQuotas200Response from a dict
list_service_quota_v1_applied_quotas200_response_form_dict = list_service_quota_v1_applied_quotas200_response.from_dict(list_service_quota_v1_applied_quotas200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


