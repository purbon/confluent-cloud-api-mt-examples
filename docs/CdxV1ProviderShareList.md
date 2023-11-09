# CdxV1ProviderShareList

`ProviderShare` object respresents the share that you have created through Stream Sharing.   Related guide: [Provider Stream Shares in Confluent Cloud](https://docs.confluent.io/cloud/current/stream-sharing/produce-shared-data.html#stream-shares).  ## The Provider Shares Model <SchemaDefinition schemaRef=\"#/components/schemas/cdx.v1.ProviderShare\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**CdxV1ProviderShareListMetadata**](CdxV1ProviderShareListMetadata.md) |  | 
**data** | [**List[CdxV1ProviderShareListDataInner]**](CdxV1ProviderShareListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.cdx_v1_provider_share_list import CdxV1ProviderShareList

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1ProviderShareList from a JSON string
cdx_v1_provider_share_list_instance = CdxV1ProviderShareList.from_json(json)
# print the JSON string representation of the object
print CdxV1ProviderShareList.to_json()

# convert the object into a dict
cdx_v1_provider_share_list_dict = cdx_v1_provider_share_list_instance.to_dict()
# create an instance of CdxV1ProviderShareList from a dict
cdx_v1_provider_share_list_form_dict = cdx_v1_provider_share_list.from_dict(cdx_v1_provider_share_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


