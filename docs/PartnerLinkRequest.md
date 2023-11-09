# PartnerLinkRequest

The partner linking request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The linking token that was generated. | 
**organization** | [**PartnerLinkRequestOrganization**](PartnerLinkRequestOrganization.md) |  | 
**entitlement** | [**OneOf**](OneOf.md) |  | 

## Example

```python
from openapi_client.models.partner_link_request import PartnerLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerLinkRequest from a JSON string
partner_link_request_instance = PartnerLinkRequest.from_json(json)
# print the JSON string representation of the object
print PartnerLinkRequest.to_json()

# convert the object into a dict
partner_link_request_dict = partner_link_request_instance.to_dict()
# create an instance of PartnerLinkRequest from a dict
partner_link_request_form_dict = partner_link_request.from_dict(partner_link_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


