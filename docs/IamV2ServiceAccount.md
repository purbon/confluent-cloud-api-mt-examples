# IamV2ServiceAccount

`ServiceAccount` objects are typically used to represent applications and other non-human principals that may access your Confluent resources.  The API allows you to create, retrieve, update, and delete individual service accounts, as well as list all your service accounts.   Related guide: [Service Accounts in Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/service-account.html).  ## The Service Accounts Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.ServiceAccount\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `service_accounts_per_org` | Service Accounts in one Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**IamV2ServiceAccountMetadata**](IamV2ServiceAccountMetadata.md) |  | [optional] 
**display_name** | **str** | A human-readable name for the Service Account | [optional] 
**description** | **str** | A free-form description of the Service Account | [optional] 

## Example

```python
from openapi_client.models.iam_v2_service_account import IamV2ServiceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2ServiceAccount from a JSON string
iam_v2_service_account_instance = IamV2ServiceAccount.from_json(json)
# print the JSON string representation of the object
print IamV2ServiceAccount.to_json()

# convert the object into a dict
iam_v2_service_account_dict = iam_v2_service_account_instance.to_dict()
# create an instance of IamV2ServiceAccount from a dict
iam_v2_service_account_form_dict = iam_v2_service_account.from_dict(iam_v2_service_account_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


