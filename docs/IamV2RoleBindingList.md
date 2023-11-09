# IamV2RoleBindingList

A role binding grants a Principal a role on resources that match a pattern.  The API allows you to perform create, delete, and list operations on role bindings.   Related guide: [Role-Based Access Control (RBAC)](https://docs.confluent.io/cloud/current/access-management/access-control/cloud-rbac.html).  ## The Role Bindings Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.RoleBinding\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**IamV2RoleBindingListMetadata**](IamV2RoleBindingListMetadata.md) |  | 
**data** | [**List[IamV2RoleBindingListDataInner]**](IamV2RoleBindingListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.iam_v2_role_binding_list import IamV2RoleBindingList

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2RoleBindingList from a JSON string
iam_v2_role_binding_list_instance = IamV2RoleBindingList.from_json(json)
# print the JSON string representation of the object
print IamV2RoleBindingList.to_json()

# convert the object into a dict
iam_v2_role_binding_list_dict = iam_v2_role_binding_list_instance.to_dict()
# create an instance of IamV2RoleBindingList from a dict
iam_v2_role_binding_list_form_dict = iam_v2_role_binding_list.from_dict(iam_v2_role_binding_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


