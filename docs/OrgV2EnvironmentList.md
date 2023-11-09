# OrgV2EnvironmentList

`Environment` objects represent an isolated namespace for your Confluent resources for organizational purposes.  The API allows you to create, delete, and update your environments. You can retrieve individual environments as well as a list of all your environments.   Related guide: [Environments in Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/environments.html).  ## The Environments Model <SchemaDefinition schemaRef=\"#/components/schemas/org.v2.Environment\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `environments_per_org` | Environments in one Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**OrgV2EnvironmentListMetadata**](OrgV2EnvironmentListMetadata.md) |  | 
**data** | [**List[OrgV2EnvironmentListDataInner]**](OrgV2EnvironmentListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.org_v2_environment_list import OrgV2EnvironmentList

# TODO update the JSON string below
json = "{}"
# create an instance of OrgV2EnvironmentList from a JSON string
org_v2_environment_list_instance = OrgV2EnvironmentList.from_json(json)
# print the JSON string representation of the object
print OrgV2EnvironmentList.to_json()

# convert the object into a dict
org_v2_environment_list_dict = org_v2_environment_list_instance.to_dict()
# create an instance of OrgV2EnvironmentList from a dict
org_v2_environment_list_form_dict = org_v2_environment_list.from_dict(org_v2_environment_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


