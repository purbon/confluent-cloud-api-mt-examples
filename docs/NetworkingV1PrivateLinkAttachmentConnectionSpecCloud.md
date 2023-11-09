# NetworkingV1PrivateLinkAttachmentConnectionSpecCloud

The cloud-specific PrivateLink attachment connection details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | PrivateLinkAttachmentConnection kind. | 
**vpc_endpoint_id** | **str** | Id of a VPC Endpoint that is connected to the VPC Endpoint service. | 
**private_endpoint_resource_id** | **str** | Resource Id of the PrivateEndpoint that is connected to the PrivateLink service.  | 
**private_service_connect_connection_id** | **str** | Id of the Private Service connection. | [readonly] 

## Example

```python
from openapi_client.models.networking_v1_private_link_attachment_connection_spec_cloud import NetworkingV1PrivateLinkAttachmentConnectionSpecCloud

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAttachmentConnectionSpecCloud from a JSON string
networking_v1_private_link_attachment_connection_spec_cloud_instance = NetworkingV1PrivateLinkAttachmentConnectionSpecCloud.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAttachmentConnectionSpecCloud.to_json()

# convert the object into a dict
networking_v1_private_link_attachment_connection_spec_cloud_dict = networking_v1_private_link_attachment_connection_spec_cloud_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAttachmentConnectionSpecCloud from a dict
networking_v1_private_link_attachment_connection_spec_cloud_form_dict = networking_v1_private_link_attachment_connection_spec_cloud.from_dict(networking_v1_private_link_attachment_connection_spec_cloud_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


