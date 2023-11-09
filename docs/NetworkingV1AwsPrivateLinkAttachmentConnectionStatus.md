# NetworkingV1AwsPrivateLinkAttachmentConnectionStatus

Status of a connection to an AWS PrivateLink attachment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | PrivateLinkAttachmentConnectionStatus kind. | 
**vpc_endpoint_service_name** | **str** | Id of the VPC Endpoint service used for PrivateLink. | [readonly] 
**vpc_endpoint_id** | **str** | Id of the VPC Endpoint (if any) that is connected to the VPC Endpoint service. | [readonly] 

## Example

```python
from openapi_client.models.networking_v1_aws_private_link_attachment_connection_status import NetworkingV1AwsPrivateLinkAttachmentConnectionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1AwsPrivateLinkAttachmentConnectionStatus from a JSON string
networking_v1_aws_private_link_attachment_connection_status_instance = NetworkingV1AwsPrivateLinkAttachmentConnectionStatus.from_json(json)
# print the JSON string representation of the object
print NetworkingV1AwsPrivateLinkAttachmentConnectionStatus.to_json()

# convert the object into a dict
networking_v1_aws_private_link_attachment_connection_status_dict = networking_v1_aws_private_link_attachment_connection_status_instance.to_dict()
# create an instance of NetworkingV1AwsPrivateLinkAttachmentConnectionStatus from a dict
networking_v1_aws_private_link_attachment_connection_status_form_dict = networking_v1_aws_private_link_attachment_connection_status.from_dict(networking_v1_aws_private_link_attachment_connection_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


