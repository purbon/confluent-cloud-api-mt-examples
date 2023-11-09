# CreatePartnerV2EntitlementRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  | [optional] 
**external_id** | **str** | The unique external ID of the entitlement (this should be unique to customer) | 
**name** | **str** | The name of the entitlement | 
**plan_id** | **str** | The plan ID the entitlement | 
**product_id** | **str** | The product ID of the entitlement | 
**usage_reporting_id** | **str** | The usage reporting ID of the entitlement (if usage reporting uses a different ID, otherwise, same as external_id)  | [optional] 
**resource_id** | **str** | The resource ID of the entitlement | [optional] 
**organization** | [**PartnerV2EntitlementOrganization**](PartnerV2EntitlementOrganization.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_partner_v2_entitlement_request import CreatePartnerV2EntitlementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePartnerV2EntitlementRequest from a JSON string
create_partner_v2_entitlement_request_instance = CreatePartnerV2EntitlementRequest.from_json(json)
# print the JSON string representation of the object
print CreatePartnerV2EntitlementRequest.to_json()

# convert the object into a dict
create_partner_v2_entitlement_request_dict = create_partner_v2_entitlement_request_instance.to_dict()
# create an instance of CreatePartnerV2EntitlementRequest from a dict
create_partner_v2_entitlement_request_form_dict = create_partner_v2_entitlement_request.from_dict(create_partner_v2_entitlement_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


