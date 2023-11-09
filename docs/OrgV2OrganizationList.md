# OrgV2OrganizationList

`Organization` objects represent a customer organization. An organization contains all customer resources (e.g., Environments, Kafka Clusters, Service Accounts, API Keys) and is tied to a billing agreement (including any annual commitment or support plan).  The API allows you to list, view, and update your organizations.   Related guide: [Organizations for Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/hierarchy/organizations/cloud-organization.html).  ## The Organizations Model <SchemaDefinition schemaRef=\"#/components/schemas/org.v2.Organization\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `organizations_per_user` | Confluent Cloud organizations a user belongs to |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**OrgV2OrganizationListMetadata**](OrgV2OrganizationListMetadata.md) |  | 
**data** | [**List[OrgV2OrganizationListDataInner]**](OrgV2OrganizationListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.org_v2_organization_list import OrgV2OrganizationList

# TODO update the JSON string below
json = "{}"
# create an instance of OrgV2OrganizationList from a JSON string
org_v2_organization_list_instance = OrgV2OrganizationList.from_json(json)
# print the JSON string representation of the object
print OrgV2OrganizationList.to_json()

# convert the object into a dict
org_v2_organization_list_dict = org_v2_organization_list_instance.to_dict()
# create an instance of OrgV2OrganizationList from a dict
org_v2_organization_list_form_dict = org_v2_organization_list.from_dict(org_v2_organization_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


