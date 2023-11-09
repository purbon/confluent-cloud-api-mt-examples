# IamV2ServiceAccountList

`ServiceAccount` objects are typically used to represent applications and other non-human principals that may access your Confluent resources.  The API allows you to create, retrieve, update, and delete individual service accounts, as well as list all your service accounts.   Related guide: [Service Accounts in Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/service-account.html).  ## The Service Accounts Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.ServiceAccount\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `service_accounts_per_org` | Service Accounts in one Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**IamV2ServiceAccountListMetadata**](IamV2ServiceAccountListMetadata.md) |  | 
**data** | [**List[IamV2ServiceAccountListDataInner]**](IamV2ServiceAccountListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.iam_v2_service_account_list import IamV2ServiceAccountList

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2ServiceAccountList from a JSON string
iam_v2_service_account_list_instance = IamV2ServiceAccountList.from_json(json)
# print the JSON string representation of the object
print IamV2ServiceAccountList.to_json()

# convert the object into a dict
iam_v2_service_account_list_dict = iam_v2_service_account_list_instance.to_dict()
# create an instance of IamV2ServiceAccountList from a dict
iam_v2_service_account_list_form_dict = iam_v2_service_account_list.from_dict(iam_v2_service_account_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


