# IamV2ApiKey

`ApiKey` objects represent access to different parts of Confluent Cloud. Some types of API keys represent access to a single cluster/resource such as a Kafka cluster, Schema Registry cluster or a ksqlDB cluster. Cloud API Keys represent access to resources within an organization that are not tied to a specific cluster, such as the Org API, IAM API, Metrics API or Connect API.  The API allows you to list, create, update and delete your API Keys.   Related guide: [API Keys in Confluent Cloud](https://docs.confluent.io/cloud/current/client-apps/api-keys.html).  ## The API Keys Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.ApiKey\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `apikeys_per_org` | API Keys in one Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**IamV2ApiKeyMetadata**](IamV2ApiKeyMetadata.md) |  | [optional] 
**spec** | [**IamV2ApiKeySpec**](IamV2ApiKeySpec.md) |  | [optional] 

## Example

```python
from openapi_client.models.iam_v2_api_key import IamV2ApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2ApiKey from a JSON string
iam_v2_api_key_instance = IamV2ApiKey.from_json(json)
# print the JSON string representation of the object
print IamV2ApiKey.to_json()

# convert the object into a dict
iam_v2_api_key_dict = iam_v2_api_key_instance.to_dict()
# create an instance of IamV2ApiKey from a dict
iam_v2_api_key_form_dict = iam_v2_api_key.from_dict(iam_v2_api_key_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


