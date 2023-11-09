# PartnerV2Entitlement

`Entitlement` objects represent metadata about a marketplace entitlement.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**ObjectMeta**](ObjectMeta.md) |  | [optional] 
**external_id** | **str** | The unique external ID of the entitlement (this should be unique to customer) | [optional] 
**name** | **str** | The name of the entitlement | [optional] 
**plan_id** | **str** | The plan ID the entitlement | [optional] 
**product_id** | **str** | The product ID of the entitlement | [optional] 
**usage_reporting_id** | **str** | The usage reporting ID of the entitlement (if usage reporting uses a different ID, otherwise, same as external_id)  | [optional] 
**resource_id** | **str** | The resource ID of the entitlement | [optional] 
**organization** | [**PartnerV2EntitlementOrganization**](PartnerV2EntitlementOrganization.md) |  | [optional] 

## Example

```python
from openapi_client.models.partner_v2_entitlement import PartnerV2Entitlement

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerV2Entitlement from a JSON string
partner_v2_entitlement_instance = PartnerV2Entitlement.from_json(json)
# print the JSON string representation of the object
print PartnerV2Entitlement.to_json()

# convert the object into a dict
partner_v2_entitlement_dict = partner_v2_entitlement_instance.to_dict()
# create an instance of PartnerV2Entitlement from a dict
partner_v2_entitlement_form_dict = partner_v2_entitlement.from_dict(partner_v2_entitlement_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


