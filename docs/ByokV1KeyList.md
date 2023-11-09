# ByokV1KeyList

`Key` objects represent customer managed keys on dedicated Confluent Cloud clusters.  Keys are used to protect data at rest stored in your dedicated Confluent Cloud clusters on AWS and Azure. This API allows you to upload and retrieve self-managed keys on Confluent Cloud.   Related guide: [Confluent Cloud Bring Your Own Key (BYOK) Management API](https://docs.confluent.io/cloud/current/clusters/byok/index.html).  ## The Keys Model <SchemaDefinition schemaRef=\"#/components/schemas/byok.v1.Key\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `byok.max_keys.per_org` | BYOK keys in one Confluent Cloud organisation. |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**ByokV1KeyListMetadata**](ByokV1KeyListMetadata.md) |  | 
**data** | [**List[ByokV1KeyListDataInner]**](ByokV1KeyListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.byok_v1_key_list import ByokV1KeyList

# TODO update the JSON string below
json = "{}"
# create an instance of ByokV1KeyList from a JSON string
byok_v1_key_list_instance = ByokV1KeyList.from_json(json)
# print the JSON string representation of the object
print ByokV1KeyList.to_json()

# convert the object into a dict
byok_v1_key_list_dict = byok_v1_key_list_instance.to_dict()
# create an instance of ByokV1KeyList from a dict
byok_v1_key_list_form_dict = byok_v1_key_list.from_dict(byok_v1_key_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


