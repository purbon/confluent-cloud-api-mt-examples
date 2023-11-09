# OrgV2Environment

`Environment` objects represent an isolated namespace for your Confluent resources for organizational purposes.  The API allows you to create, delete, and update your environments. You can retrieve individual environments as well as a list of all your environments.   Related guide: [Environments in Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/environments.html).  ## The Environments Model <SchemaDefinition schemaRef=\"#/components/schemas/org.v2.Environment\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `environments_per_org` | Environments in one Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**OrgV2EnvironmentMetadata**](OrgV2EnvironmentMetadata.md) |  | [optional] 
**display_name** | **str** | A human-readable name for the Environment | [optional] 

## Example

```python
from openapi_client.models.org_v2_environment import OrgV2Environment

# TODO update the JSON string below
json = "{}"
# create an instance of OrgV2Environment from a JSON string
org_v2_environment_instance = OrgV2Environment.from_json(json)
# print the JSON string representation of the object
print OrgV2Environment.to_json()

# convert the object into a dict
org_v2_environment_dict = org_v2_environment_instance.to_dict()
# create an instance of OrgV2Environment from a dict
org_v2_environment_form_dict = org_v2_environment.from_dict(org_v2_environment_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


