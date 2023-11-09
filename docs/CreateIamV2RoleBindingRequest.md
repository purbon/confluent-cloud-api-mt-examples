# CreateIamV2RoleBindingRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**IamV2RoleBindingMetadata**](IamV2RoleBindingMetadata.md) |  | [optional] 
**principal** | **str** | The principal User or Group to bind the role to | 
**role_name** | **str** | The name of the role to bind to the principal | 
**crn_pattern** | **str** | A CRN that specifies the scope and resource patterns necessary for the role to bind | 

## Example

```python
from openapi_client.models.create_iam_v2_role_binding_request import CreateIamV2RoleBindingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIamV2RoleBindingRequest from a JSON string
create_iam_v2_role_binding_request_instance = CreateIamV2RoleBindingRequest.from_json(json)
# print the JSON string representation of the object
print CreateIamV2RoleBindingRequest.to_json()

# convert the object into a dict
create_iam_v2_role_binding_request_dict = create_iam_v2_role_binding_request_instance.to_dict()
# create an instance of CreateIamV2RoleBindingRequest from a dict
create_iam_v2_role_binding_request_form_dict = create_iam_v2_role_binding_request.from_dict(create_iam_v2_role_binding_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


