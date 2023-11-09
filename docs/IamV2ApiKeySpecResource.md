# IamV2ApiKeySpecResource

The resource associated with this object. The resource can be one of Kafka Cluster ID (example: lkc-12345), Schema Registry Cluster ID (example: lsrc-12345) or ksqlDB Cluster ID (example: lksqlc-12345). May be null or omitted if not associated with a resource. For Cloud API keys, resource should be `null`. [Learn more in Authentication](https://docs.confluent.io/cloud/current/api.html#section/Authentication). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the referred resource | 
**environment** | **str** | Environment of the referred resource, if env-scoped | [optional] 
**related** | **str** | API URL for accessing or modifying the referred object | [readonly] 
**resource_name** | **str** | CRN reference to the referred resource | [readonly] 
**api_version** | **str** | API group and version of the referred resource | [optional] [readonly] 
**kind** | **str** | Kind of the referred resource | [optional] [readonly] 

## Example

```python
from openapi_client.models.iam_v2_api_key_spec_resource import IamV2ApiKeySpecResource

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2ApiKeySpecResource from a JSON string
iam_v2_api_key_spec_resource_instance = IamV2ApiKeySpecResource.from_json(json)
# print the JSON string representation of the object
print IamV2ApiKeySpecResource.to_json()

# convert the object into a dict
iam_v2_api_key_spec_resource_dict = iam_v2_api_key_spec_resource_instance.to_dict()
# create an instance of IamV2ApiKeySpecResource from a dict
iam_v2_api_key_spec_resource_form_dict = iam_v2_api_key_spec_resource.from_dict(iam_v2_api_key_spec_resource_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


