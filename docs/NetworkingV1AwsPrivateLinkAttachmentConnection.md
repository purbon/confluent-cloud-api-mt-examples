# NetworkingV1AwsPrivateLinkAttachmentConnection

Represents a connection between an AWS VPC Endpoint and an Endpoint service.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | PrivateLinkAttachmentConnection kind. | 
**vpc_endpoint_id** | **str** | Id of a VPC Endpoint that is connected to the VPC Endpoint service. | 

## Example

```python
from openapi_client.models.networking_v1_aws_private_link_attachment_connection import NetworkingV1AwsPrivateLinkAttachmentConnection

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1AwsPrivateLinkAttachmentConnection from a JSON string
networking_v1_aws_private_link_attachment_connection_instance = NetworkingV1AwsPrivateLinkAttachmentConnection.from_json(json)
# print the JSON string representation of the object
print NetworkingV1AwsPrivateLinkAttachmentConnection.to_json()

# convert the object into a dict
networking_v1_aws_private_link_attachment_connection_dict = networking_v1_aws_private_link_attachment_connection_instance.to_dict()
# create an instance of NetworkingV1AwsPrivateLinkAttachmentConnection from a dict
networking_v1_aws_private_link_attachment_connection_form_dict = networking_v1_aws_private_link_attachment_connection.from_dict(networking_v1_aws_private_link_attachment_connection_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


