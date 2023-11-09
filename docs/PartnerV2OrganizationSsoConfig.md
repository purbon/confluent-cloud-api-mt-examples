# PartnerV2OrganizationSsoConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**tenant_id** | **str** | The Azure AD tenant ID | 

## Example

```python
from openapi_client.models.partner_v2_organization_sso_config import PartnerV2OrganizationSsoConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerV2OrganizationSsoConfig from a JSON string
partner_v2_organization_sso_config_instance = PartnerV2OrganizationSsoConfig.from_json(json)
# print the JSON string representation of the object
print PartnerV2OrganizationSsoConfig.to_json()

# convert the object into a dict
partner_v2_organization_sso_config_dict = partner_v2_organization_sso_config_instance.to_dict()
# create an instance of PartnerV2OrganizationSsoConfig from a dict
partner_v2_organization_sso_config_form_dict = partner_v2_organization_sso_config.from_dict(partner_v2_organization_sso_config_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


