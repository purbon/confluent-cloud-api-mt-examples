# PartnerSignupResponse

The partner signup response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | The ID of the organization | 
**sso_url** | **str** | The login URL for the customer to access Confluent Cloud | 
**display_message** | **str** | The display message contains useful information which is shown on the Marketplace UI to the customers. | [optional] 

## Example

```python
from openapi_client.models.partner_signup_response import PartnerSignupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerSignupResponse from a JSON string
partner_signup_response_instance = PartnerSignupResponse.from_json(json)
# print the JSON string representation of the object
print PartnerSignupResponse.to_json()

# convert the object into a dict
partner_signup_response_dict = partner_signup_response_instance.to_dict()
# create an instance of PartnerSignupResponse from a dict
partner_signup_response_form_dict = partner_signup_response.from_dict(partner_signup_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


