# GetOrgV2Organization200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**metadata** | [**OrgV2OrganizationMetadata**](OrgV2OrganizationMetadata.md) |  | [optional] 
**display_name** | **str** | A human-readable name for the Organization | [optional] 
**jit_enabled** | **bool** | The flag to toggle Just-In-Time user provisioning for SSO-enabled organization. Available for early access only. | [optional] 

## Example

```python
from openapi_client.models.get_org_v2_organization200_response import GetOrgV2Organization200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrgV2Organization200Response from a JSON string
get_org_v2_organization200_response_instance = GetOrgV2Organization200Response.from_json(json)
# print the JSON string representation of the object
print GetOrgV2Organization200Response.to_json()

# convert the object into a dict
get_org_v2_organization200_response_dict = get_org_v2_organization200_response_instance.to_dict()
# create an instance of GetOrgV2Organization200Response from a dict
get_org_v2_organization200_response_form_dict = get_org_v2_organization200_response.from_dict(get_org_v2_organization200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


