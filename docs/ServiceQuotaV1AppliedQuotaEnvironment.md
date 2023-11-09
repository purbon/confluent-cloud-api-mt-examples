# ServiceQuotaV1AppliedQuotaEnvironment

The environment ID the quota is associated with. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the referred resource | 
**related** | **str** | API URL for accessing or modifying the referred object | [readonly] 
**resource_name** | **str** | CRN reference to the referred resource | [readonly] 

## Example

```python
from openapi_client.models.service_quota_v1_applied_quota_environment import ServiceQuotaV1AppliedQuotaEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQuotaV1AppliedQuotaEnvironment from a JSON string
service_quota_v1_applied_quota_environment_instance = ServiceQuotaV1AppliedQuotaEnvironment.from_json(json)
# print the JSON string representation of the object
print ServiceQuotaV1AppliedQuotaEnvironment.to_json()

# convert the object into a dict
service_quota_v1_applied_quota_environment_dict = service_quota_v1_applied_quota_environment_instance.to_dict()
# create an instance of ServiceQuotaV1AppliedQuotaEnvironment from a dict
service_quota_v1_applied_quota_environment_form_dict = service_quota_v1_applied_quota_environment.from_dict(service_quota_v1_applied_quota_environment_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


