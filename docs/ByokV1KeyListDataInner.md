# ByokV1KeyListDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**metadata** | [**ByokV1KeyMetadata**](ByokV1KeyMetadata.md) |  | 
**key** | [**ByokV1KeyKey**](ByokV1KeyKey.md) |  | 
**provider** | **str** | The cloud provider of the Key. | [readonly] 
**state** | **str** | The state of the key:   AVAILABLE: key can be used for a Kafka cluster provisioning   IN_USE: key is already in use by a Kafka cluster provisioning  | [readonly] 

## Example

```python
from openapi_client.models.byok_v1_key_list_data_inner import ByokV1KeyListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ByokV1KeyListDataInner from a JSON string
byok_v1_key_list_data_inner_instance = ByokV1KeyListDataInner.from_json(json)
# print the JSON string representation of the object
print ByokV1KeyListDataInner.to_json()

# convert the object into a dict
byok_v1_key_list_data_inner_dict = byok_v1_key_list_data_inner_instance.to_dict()
# create an instance of ByokV1KeyListDataInner from a dict
byok_v1_key_list_data_inner_form_dict = byok_v1_key_list_data_inner.from_dict(byok_v1_key_list_data_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


