# OrgV2Organization

`Organization` objects represent a customer organization. An organization contains all customer resources (e.g., Environments, Kafka Clusters, Service Accounts, API Keys) and is tied to a billing agreement (including any annual commitment or support plan).  The API allows you to list, view, and update your organizations.   Related guide: [Organizations for Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/hierarchy/organizations/cloud-organization.html).  ## The Organizations Model <SchemaDefinition schemaRef=\"#/components/schemas/org.v2.Organization\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `organizations_per_user` | Confluent Cloud organizations a user belongs to |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**OrgV2OrganizationMetadata**](OrgV2OrganizationMetadata.md) |  | [optional] 
**display_name** | **str** | A human-readable name for the Organization | [optional] 
**jit_enabled** | **bool** | The flag to toggle Just-In-Time user provisioning for SSO-enabled organization. Available for early access only. | [optional] 

## Example

```python
from openapi_client.models.org_v2_organization import OrgV2Organization

# TODO update the JSON string below
json = "{}"
# create an instance of OrgV2Organization from a JSON string
org_v2_organization_instance = OrgV2Organization.from_json(json)
# print the JSON string representation of the object
print OrgV2Organization.to_json()

# convert the object into a dict
org_v2_organization_dict = org_v2_organization_instance.to_dict()
# create an instance of OrgV2Organization from a dict
org_v2_organization_form_dict = org_v2_organization.from_dict(org_v2_organization_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


