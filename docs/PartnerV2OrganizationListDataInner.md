# PartnerV2OrganizationListDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  | 
**name** | **str** | The name of the organization | [optional] 
**sso_url** | **str** | The login URL for the customer to access Confluent Cloud | [optional] [readonly] 
**sso_config** | [**PartnerV2OrganizationSsoConfig**](PartnerV2OrganizationSsoConfig.md) |  | [optional] 

## Example

```python
from openapi_client.models.partner_v2_organization_list_data_inner import PartnerV2OrganizationListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerV2OrganizationListDataInner from a JSON string
partner_v2_organization_list_data_inner_instance = PartnerV2OrganizationListDataInner.from_json(json)
# print the JSON string representation of the object
print PartnerV2OrganizationListDataInner.to_json()

# convert the object into a dict
partner_v2_organization_list_data_inner_dict = partner_v2_organization_list_data_inner_instance.to_dict()
# create an instance of PartnerV2OrganizationListDataInner from a dict
partner_v2_organization_list_data_inner_form_dict = partner_v2_organization_list_data_inner.from_dict(partner_v2_organization_list_data_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


