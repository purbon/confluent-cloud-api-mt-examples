# ServiceQuotaV1AppliedQuotaOrganization

A unique organization id to associate a specific organization to this quota.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the referred resource | 
**related** | **str** | API URL for accessing or modifying the referred object | [readonly] 
**resource_name** | **str** | CRN reference to the referred resource | [readonly] 

## Example

```python
from openapi_client.models.service_quota_v1_applied_quota_organization import ServiceQuotaV1AppliedQuotaOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQuotaV1AppliedQuotaOrganization from a JSON string
service_quota_v1_applied_quota_organization_instance = ServiceQuotaV1AppliedQuotaOrganization.from_json(json)
# print the JSON string representation of the object
print ServiceQuotaV1AppliedQuotaOrganization.to_json()

# convert the object into a dict
service_quota_v1_applied_quota_organization_dict = service_quota_v1_applied_quota_organization_instance.to_dict()
# create an instance of ServiceQuotaV1AppliedQuotaOrganization from a dict
service_quota_v1_applied_quota_organization_form_dict = service_quota_v1_applied_quota_organization.from_dict(service_quota_v1_applied_quota_organization_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


