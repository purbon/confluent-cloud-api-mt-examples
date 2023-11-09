# IamV2RoleBinding

A role binding grants a Principal a role on resources that match a pattern.  The API allows you to perform create, delete, and list operations on role bindings.   Related guide: [Role-Based Access Control (RBAC)](https://docs.confluent.io/cloud/current/access-management/access-control/cloud-rbac.html).  ## The Role Bindings Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.RoleBinding\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**IamV2RoleBindingMetadata**](IamV2RoleBindingMetadata.md) |  | [optional] 
**principal** | **str** | The principal User or Group to bind the role to | [optional] 
**role_name** | **str** | The name of the role to bind to the principal | [optional] 
**crn_pattern** | **str** | A CRN that specifies the scope and resource patterns necessary for the role to bind | [optional] 

## Example

```python
from openapi_client.models.iam_v2_role_binding import IamV2RoleBinding

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2RoleBinding from a JSON string
iam_v2_role_binding_instance = IamV2RoleBinding.from_json(json)
# print the JSON string representation of the object
print IamV2RoleBinding.to_json()

# convert the object into a dict
iam_v2_role_binding_dict = iam_v2_role_binding_instance.to_dict()
# create an instance of IamV2RoleBinding from a dict
iam_v2_role_binding_form_dict = iam_v2_role_binding.from_dict(iam_v2_role_binding_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


