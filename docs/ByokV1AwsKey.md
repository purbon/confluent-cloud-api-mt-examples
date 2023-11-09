# ByokV1AwsKey

The AWS BYOK details 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_arn** | **str** | The Amazon Resource Name (ARN) of an AWS KMS key.  | 
**roles** | **List[str]** | The Amazon Resource Names (ARNs) of IAM Roles created for this key-environment combination.  | [optional] [readonly] 
**kind** | **str** | BYOK kind type.  | 

## Example

```python
from openapi_client.models.byok_v1_aws_key import ByokV1AwsKey

# TODO update the JSON string below
json = "{}"
# create an instance of ByokV1AwsKey from a JSON string
byok_v1_aws_key_instance = ByokV1AwsKey.from_json(json)
# print the JSON string representation of the object
print ByokV1AwsKey.to_json()

# convert the object into a dict
byok_v1_aws_key_dict = byok_v1_aws_key_instance.to_dict()
# create an instance of ByokV1AwsKey from a dict
byok_v1_aws_key_form_dict = byok_v1_aws_key.from_dict(byok_v1_aws_key_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


