# PartnerSignupRequest

The partner signup request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | [**PartnerSignupRequestOrganization**](PartnerSignupRequestOrganization.md) |  | 
**user** | **object** |  | [optional] 
**entitlement** | [**OneOf**](OneOf.md) |  | 

## Example

```python
from openapi_client.models.partner_signup_request import PartnerSignupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerSignupRequest from a JSON string
partner_signup_request_instance = PartnerSignupRequest.from_json(json)
# print the JSON string representation of the object
print PartnerSignupRequest.to_json()

# convert the object into a dict
partner_signup_request_dict = partner_signup_request_instance.to_dict()
# create an instance of PartnerSignupRequest from a dict
partner_signup_request_form_dict = partner_signup_request.from_dict(partner_signup_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


