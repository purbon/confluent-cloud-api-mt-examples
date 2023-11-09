# ServiceQuotaV1AppliedQuotaNetwork

The network ID the quota is associated with. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the referred resource | 
**environment** | **str** | Environment of the referred resource, if env-scoped | [optional] 
**related** | **str** | API URL for accessing or modifying the referred object | [readonly] 
**resource_name** | **str** | CRN reference to the referred resource | [readonly] 

## Example

```python
from openapi_client.models.service_quota_v1_applied_quota_network import ServiceQuotaV1AppliedQuotaNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQuotaV1AppliedQuotaNetwork from a JSON string
service_quota_v1_applied_quota_network_instance = ServiceQuotaV1AppliedQuotaNetwork.from_json(json)
# print the JSON string representation of the object
print ServiceQuotaV1AppliedQuotaNetwork.to_json()

# convert the object into a dict
service_quota_v1_applied_quota_network_dict = service_quota_v1_applied_quota_network_instance.to_dict()
# create an instance of ServiceQuotaV1AppliedQuotaNetwork from a dict
service_quota_v1_applied_quota_network_form_dict = service_quota_v1_applied_quota_network.from_dict(service_quota_v1_applied_quota_network_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


