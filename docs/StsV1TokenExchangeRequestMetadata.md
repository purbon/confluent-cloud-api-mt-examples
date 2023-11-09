# StsV1TokenExchangeRequestMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **object** |  | 
**resource_name** | **object** |  | [optional] 
**created_at** | **datetime** | The date and time at which this object was created. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**updated_at** | **datetime** | The date and time at which this object was last updated. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**deleted_at** | **datetime** | The date and time at which this object was (or will be) deleted. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 

## Example

```python
from openapi_client.models.sts_v1_token_exchange_request_metadata import StsV1TokenExchangeRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of StsV1TokenExchangeRequestMetadata from a JSON string
sts_v1_token_exchange_request_metadata_instance = StsV1TokenExchangeRequestMetadata.from_json(json)
# print the JSON string representation of the object
print StsV1TokenExchangeRequestMetadata.to_json()

# convert the object into a dict
sts_v1_token_exchange_request_metadata_dict = sts_v1_token_exchange_request_metadata_instance.to_dict()
# create an instance of StsV1TokenExchangeRequestMetadata from a dict
sts_v1_token_exchange_request_metadata_form_dict = sts_v1_token_exchange_request_metadata.from_dict(sts_v1_token_exchange_request_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


