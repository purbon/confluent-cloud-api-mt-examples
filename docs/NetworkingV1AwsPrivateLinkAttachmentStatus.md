# NetworkingV1AwsPrivateLinkAttachmentStatus

AWS PrivateLink attachment represents reserved capacity in an AWS VPC Endpoint Service that can be used to establish PrivateLink connections. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | PrivateLinkAttachmentStatus kind. | [readonly] 
**vpc_endpoint_service** | [**NetworkingV1AwsPrivateLinkAttachmentStatusVpcEndpointService**](NetworkingV1AwsPrivateLinkAttachmentStatusVpcEndpointService.md) |  | 

## Example

```python
from openapi_client.models.networking_v1_aws_private_link_attachment_status import NetworkingV1AwsPrivateLinkAttachmentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1AwsPrivateLinkAttachmentStatus from a JSON string
networking_v1_aws_private_link_attachment_status_instance = NetworkingV1AwsPrivateLinkAttachmentStatus.from_json(json)
# print the JSON string representation of the object
print NetworkingV1AwsPrivateLinkAttachmentStatus.to_json()

# convert the object into a dict
networking_v1_aws_private_link_attachment_status_dict = networking_v1_aws_private_link_attachment_status_instance.to_dict()
# create an instance of NetworkingV1AwsPrivateLinkAttachmentStatus from a dict
networking_v1_aws_private_link_attachment_status_form_dict = networking_v1_aws_private_link_attachment_status.from_dict(networking_v1_aws_private_link_attachment_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


