# ByokV1Key

`Key` objects represent customer managed keys on dedicated Confluent Cloud clusters.  Keys are used to protect data at rest stored in your dedicated Confluent Cloud clusters on AWS and Azure. This API allows you to upload and retrieve self-managed keys on Confluent Cloud.   Related guide: [Confluent Cloud Bring Your Own Key (BYOK) Management API](https://docs.confluent.io/cloud/current/clusters/byok/index.html).  ## The Keys Model <SchemaDefinition schemaRef=\"#/components/schemas/byok.v1.Key\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `byok.max_keys.per_org` | BYOK keys in one Confluent Cloud organisation. |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**ByokV1KeyMetadata**](ByokV1KeyMetadata.md) |  | [optional] 
**key** | [**ByokV1KeyKey**](ByokV1KeyKey.md) |  | [optional] 
**provider** | **str** | The cloud provider of the Key. | [optional] [readonly] 
**state** | **str** | The state of the key:   AVAILABLE: key can be used for a Kafka cluster provisioning   IN_USE: key is already in use by a Kafka cluster provisioning  | [optional] [readonly] 

## Example

```python
from openapi_client.models.byok_v1_key import ByokV1Key

# TODO update the JSON string below
json = "{}"
# create an instance of ByokV1Key from a JSON string
byok_v1_key_instance = ByokV1Key.from_json(json)
# print the JSON string representation of the object
print ByokV1Key.to_json()

# convert the object into a dict
byok_v1_key_dict = byok_v1_key_instance.to_dict()
# create an instance of ByokV1Key from a dict
byok_v1_key_form_dict = byok_v1_key.from_dict(byok_v1_key_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


