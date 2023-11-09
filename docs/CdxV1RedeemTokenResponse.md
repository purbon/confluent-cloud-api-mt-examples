# CdxV1RedeemTokenResponse

Share details for the consumer org or user

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**CdxV1RedeemTokenResponseMetadata**](CdxV1RedeemTokenResponseMetadata.md) |  | [optional] 
**api_key** | **str** | The api key | [optional] [readonly] 
**secret** | **str** | The api key secret | [optional] [readonly] 
**kafka_bootstrap_url** | **str** | The kafka cluster bootstrap url | [optional] [readonly] 
**schema_registry_api_key** | **str** | The api key for schema registry | [optional] [readonly] 
**schema_registry_secret** | **str** | The api key secret for schema registry | [optional] [readonly] 
**schema_registry_url** | **str** | The schema registry endpoint url | [optional] [readonly] 
**resources** | [**List[CdxV1RedeemTokenResponseResourcesInner]**](CdxV1RedeemTokenResponseResourcesInner.md) | List of shared resources | [optional] 

## Example

```python
from openapi_client.models.cdx_v1_redeem_token_response import CdxV1RedeemTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1RedeemTokenResponse from a JSON string
cdx_v1_redeem_token_response_instance = CdxV1RedeemTokenResponse.from_json(json)
# print the JSON string representation of the object
print CdxV1RedeemTokenResponse.to_json()

# convert the object into a dict
cdx_v1_redeem_token_response_dict = cdx_v1_redeem_token_response_instance.to_dict()
# create an instance of CdxV1RedeemTokenResponse from a dict
cdx_v1_redeem_token_response_form_dict = cdx_v1_redeem_token_response.from_dict(cdx_v1_redeem_token_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


