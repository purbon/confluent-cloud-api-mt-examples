# NetworkingV1AwsPrivateLinkAccess

AWS PrivateLink access configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | PrivateLink kind type. | 
**account** | **str** | The AWS account ID | 

## Example

```python
from openapi_client.models.networking_v1_aws_private_link_access import NetworkingV1AwsPrivateLinkAccess

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1AwsPrivateLinkAccess from a JSON string
networking_v1_aws_private_link_access_instance = NetworkingV1AwsPrivateLinkAccess.from_json(json)
# print the JSON string representation of the object
print NetworkingV1AwsPrivateLinkAccess.to_json()

# convert the object into a dict
networking_v1_aws_private_link_access_dict = networking_v1_aws_private_link_access_instance.to_dict()
# create an instance of NetworkingV1AwsPrivateLinkAccess from a dict
networking_v1_aws_private_link_access_form_dict = networking_v1_aws_private_link_access.from_dict(networking_v1_aws_private_link_access_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


