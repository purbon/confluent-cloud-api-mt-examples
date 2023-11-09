# StsV1TokenExchangeReply

token exchange response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | An JWT access token, issued by Confluent, in response to the token exchange request. Client application could use the access token to access confluent public api  | 
**issued_token_type** | **str** | The token type. Always matches the value of requested_token_type from the request. | 
**token_type** | **str** | Indicates the token type value. The only type that Confluent supports is Bearer | 
**expires_in** | **int** | The length of time, in seconds, that the access token is valid. | 

## Example

```python
from openapi_client.models.sts_v1_token_exchange_reply import StsV1TokenExchangeReply

# TODO update the JSON string below
json = "{}"
# create an instance of StsV1TokenExchangeReply from a JSON string
sts_v1_token_exchange_reply_instance = StsV1TokenExchangeReply.from_json(json)
# print the JSON string representation of the object
print StsV1TokenExchangeReply.to_json()

# convert the object into a dict
sts_v1_token_exchange_reply_dict = sts_v1_token_exchange_reply_instance.to_dict()
# create an instance of StsV1TokenExchangeReply from a dict
sts_v1_token_exchange_reply_form_dict = sts_v1_token_exchange_reply.from_dict(sts_v1_token_exchange_reply_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


