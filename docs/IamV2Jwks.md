# IamV2Jwks

`JWKS` objects represent public key sets for a specific OAuth/OpenID Connect provider within Confluent Cloud.  The API allows you to refresh JWKS public key data.   Related guide: [OAuth for Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/overview.html).  ## The Jwks Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.Jwks\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**spec** | [**IamV2JwksSpec**](IamV2JwksSpec.md) |  | [optional] 
**status** | [**IamV2JwksStatus**](IamV2JwksStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.iam_v2_jwks import IamV2Jwks

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2Jwks from a JSON string
iam_v2_jwks_instance = IamV2Jwks.from_json(json)
# print the JSON string representation of the object
print IamV2Jwks.to_json()

# convert the object into a dict
iam_v2_jwks_dict = iam_v2_jwks_instance.to_dict()
# create an instance of IamV2Jwks from a dict
iam_v2_jwks_form_dict = iam_v2_jwks.from_dict(iam_v2_jwks_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


