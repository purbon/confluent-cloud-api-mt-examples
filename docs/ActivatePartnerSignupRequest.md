# ActivatePartnerSignupRequest

The partner signup activation request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **object** |  | 
**organization_id** | **str** | The ID of the organization | 

## Example

```python
from openapi_client.models.activate_partner_signup_request import ActivatePartnerSignupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivatePartnerSignupRequest from a JSON string
activate_partner_signup_request_instance = ActivatePartnerSignupRequest.from_json(json)
# print the JSON string representation of the object
print ActivatePartnerSignupRequest.to_json()

# convert the object into a dict
activate_partner_signup_request_dict = activate_partner_signup_request_instance.to_dict()
# create an instance of ActivatePartnerSignupRequest from a dict
activate_partner_signup_request_form_dict = activate_partner_signup_request.from_dict(activate_partner_signup_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


