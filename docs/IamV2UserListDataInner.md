# IamV2UserListDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**metadata** | [**IamV2UserMetadata**](IamV2UserMetadata.md) |  | 
**email** | **str** | The user&#39;s email address | 
**full_name** | **str** | The user&#39;s full name | [optional] 
**auth_type** | **str** | The user&#39;s authentication method | [optional] [readonly] 

## Example

```python
from openapi_client.models.iam_v2_user_list_data_inner import IamV2UserListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2UserListDataInner from a JSON string
iam_v2_user_list_data_inner_instance = IamV2UserListDataInner.from_json(json)
# print the JSON string representation of the object
print IamV2UserListDataInner.to_json()

# convert the object into a dict
iam_v2_user_list_data_inner_dict = iam_v2_user_list_data_inner_instance.to_dict()
# create an instance of IamV2UserListDataInner from a dict
iam_v2_user_list_data_inner_form_dict = iam_v2_user_list_data_inner.from_dict(iam_v2_user_list_data_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


