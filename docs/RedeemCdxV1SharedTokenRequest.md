# RedeemCdxV1SharedTokenRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**CdxV1RedeemTokenRequestMetadata**](CdxV1RedeemTokenRequestMetadata.md) |  | [optional] 
**token** | **str** | The encrypted token | 
**aws_account** | **str** | Consumer&#39;s AWS account ID for PrivateLink access. | [optional] 
**azure_subscription** | **str** | Consumer&#39;s Azure subscription ID for PrivateLink access. | [optional] 
**gcp_project** | **str** | Consumer&#39;s GCP project ID for Private Service Connect access. | [optional] 

## Example

```python
from openapi_client.models.redeem_cdx_v1_shared_token_request import RedeemCdxV1SharedTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedeemCdxV1SharedTokenRequest from a JSON string
redeem_cdx_v1_shared_token_request_instance = RedeemCdxV1SharedTokenRequest.from_json(json)
# print the JSON string representation of the object
print RedeemCdxV1SharedTokenRequest.to_json()

# convert the object into a dict
redeem_cdx_v1_shared_token_request_dict = redeem_cdx_v1_shared_token_request_instance.to_dict()
# create an instance of RedeemCdxV1SharedTokenRequest from a dict
redeem_cdx_v1_shared_token_request_form_dict = redeem_cdx_v1_shared_token_request.from_dict(redeem_cdx_v1_shared_token_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


