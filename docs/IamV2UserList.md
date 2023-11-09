# IamV2UserList

`User` objects represent individuals who may access your Confluent resources.  The API allows you to retrieve, update, and delete individual users, as well as list of all your users. This API cannot be used to create new user accounts.   Related guide: [Users in Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/user-account.html).  ## The Users Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.User\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `users_per_org` | Users in one Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**IamV2UserListMetadata**](IamV2UserListMetadata.md) |  | 
**data** | [**List[IamV2UserListDataInner]**](IamV2UserListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.iam_v2_user_list import IamV2UserList

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2UserList from a JSON string
iam_v2_user_list_instance = IamV2UserList.from_json(json)
# print the JSON string representation of the object
print IamV2UserList.to_json()

# convert the object into a dict
iam_v2_user_list_dict = iam_v2_user_list_instance.to_dict()
# create an instance of IamV2UserList from a dict
iam_v2_user_list_form_dict = iam_v2_user_list.from_dict(iam_v2_user_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


