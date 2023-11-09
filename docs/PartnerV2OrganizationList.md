# PartnerV2OrganizationList

`Organizations` objects represent an entire Confluent Cloud organization.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**ListMeta**](ListMeta.md) |  | 
**data** | [**List[PartnerV2OrganizationListDataInner]**](PartnerV2OrganizationListDataInner.md) |  | 

## Example

```python
from openapi_client.models.partner_v2_organization_list import PartnerV2OrganizationList

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerV2OrganizationList from a JSON string
partner_v2_organization_list_instance = PartnerV2OrganizationList.from_json(json)
# print the JSON string representation of the object
print PartnerV2OrganizationList.to_json()

# convert the object into a dict
partner_v2_organization_list_dict = partner_v2_organization_list_instance.to_dict()
# create an instance of PartnerV2OrganizationList from a dict
partner_v2_organization_list_form_dict = partner_v2_organization_list.from_dict(partner_v2_organization_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


