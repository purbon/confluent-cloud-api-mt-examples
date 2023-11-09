# IamV2UserUpdate

`User` objects represent individuals who may access your Confluent resources.  The API allows you to retrieve, update, and delete individual users, as well as list of all your users. This API cannot be used to create new user accounts.   Related guide: [Users in Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/user-account.html).  ## The Users Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.User\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `users_per_org` | Users in one Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**IamV2UserMetadata**](IamV2UserMetadata.md) |  | [optional] 
**full_name** | **str** | The user&#39;s full name | [optional] 
**auth_type** | **str** | The user&#39;s authentication method | [optional] [readonly] 

## Example

```python
from openapi_client.models.iam_v2_user_update import IamV2UserUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2UserUpdate from a JSON string
iam_v2_user_update_instance = IamV2UserUpdate.from_json(json)
# print the JSON string representation of the object
print IamV2UserUpdate.to_json()

# convert the object into a dict
iam_v2_user_update_dict = iam_v2_user_update_instance.to_dict()
# create an instance of IamV2UserUpdate from a dict
iam_v2_user_update_form_dict = iam_v2_user_update.from_dict(iam_v2_user_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


