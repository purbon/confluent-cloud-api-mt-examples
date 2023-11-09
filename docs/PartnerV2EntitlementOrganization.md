# PartnerV2EntitlementOrganization

The organization associated with this object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the referred resource | 
**environment** | **str** | Environment of the referred resource, if env-scoped | [optional] 
**related** | **str** | API URL for accessing or modifying the referred object | [readonly] 
**resource_name** | **str** | CRN reference to the referred resource | [readonly] 
**api_version** | **str** | API group and version of the referred resource | [optional] [readonly] 
**kind** | **str** | Kind of the referred resource | [optional] [readonly] 

## Example

```python
from openapi_client.models.partner_v2_entitlement_organization import PartnerV2EntitlementOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerV2EntitlementOrganization from a JSON string
partner_v2_entitlement_organization_instance = PartnerV2EntitlementOrganization.from_json(json)
# print the JSON string representation of the object
print PartnerV2EntitlementOrganization.to_json()

# convert the object into a dict
partner_v2_entitlement_organization_dict = partner_v2_entitlement_organization_instance.to_dict()
# create an instance of PartnerV2EntitlementOrganization from a dict
partner_v2_entitlement_organization_form_dict = partner_v2_entitlement_organization.from_dict(partner_v2_entitlement_organization_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


