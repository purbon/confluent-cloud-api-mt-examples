# IamV2ApiKeyList

`ApiKey` objects represent access to different parts of Confluent Cloud. Some types of API keys represent access to a single cluster/resource such as a Kafka cluster, Schema Registry cluster or a ksqlDB cluster. Cloud API Keys represent access to resources within an organization that are not tied to a specific cluster, such as the Org API, IAM API, Metrics API or Connect API.  The API allows you to list, create, update and delete your API Keys.   Related guide: [API Keys in Confluent Cloud](https://docs.confluent.io/cloud/current/client-apps/api-keys.html).  ## The API Keys Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.ApiKey\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `apikeys_per_org` | API Keys in one Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**IamV2ApiKeyListMetadata**](IamV2ApiKeyListMetadata.md) |  | 
**data** | [**List[IamV2ApiKeyListDataInner]**](IamV2ApiKeyListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.iam_v2_api_key_list import IamV2ApiKeyList

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2ApiKeyList from a JSON string
iam_v2_api_key_list_instance = IamV2ApiKeyList.from_json(json)
# print the JSON string representation of the object
print IamV2ApiKeyList.to_json()

# convert the object into a dict
iam_v2_api_key_list_dict = iam_v2_api_key_list_instance.to_dict()
# create an instance of IamV2ApiKeyList from a dict
iam_v2_api_key_list_form_dict = iam_v2_api_key_list.from_dict(iam_v2_api_key_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


