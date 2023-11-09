# CdxV1CreateProviderShareRequest

Create share request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**CdxV1CreateProviderShareRequestMetadata**](CdxV1CreateProviderShareRequestMetadata.md) |  | [optional] 
**delivery_method** | **str** | Method by which the invite will be delivered | [optional] 
**consumer_restriction** | [**CdxV1CreateProviderShareRequestConsumerRestriction**](CdxV1CreateProviderShareRequestConsumerRestriction.md) |  | [optional] 
**resources** | **List[str]** | List of resource crns to be shared | [optional] 

## Example

```python
from openapi_client.models.cdx_v1_create_provider_share_request import CdxV1CreateProviderShareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1CreateProviderShareRequest from a JSON string
cdx_v1_create_provider_share_request_instance = CdxV1CreateProviderShareRequest.from_json(json)
# print the JSON string representation of the object
print CdxV1CreateProviderShareRequest.to_json()

# convert the object into a dict
cdx_v1_create_provider_share_request_dict = cdx_v1_create_provider_share_request_instance.to_dict()
# create an instance of CdxV1CreateProviderShareRequest from a dict
cdx_v1_create_provider_share_request_form_dict = cdx_v1_create_provider_share_request.from_dict(cdx_v1_create_provider_share_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


