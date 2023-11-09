# NetworkingV1TransitGatewayAttachmentSpecCloud

The cloud-specific Transit Gateway details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | AWS Transit Gateway Attachment kind type. | 
**ram_share_arn** | **str** | The full AWS Resource Name (ARN) for the AWS Resource Access Manager (RAM) Share of the Transit Gateways that you want Confluent Cloud to be attached to. | 
**transit_gateway_id** | **str** | The ID of the AWS Transit Gateway that you want Confluent CLoud to be attached to. | 
**routes** | **List[str]** | List of destination routes. | 

## Example

```python
from openapi_client.models.networking_v1_transit_gateway_attachment_spec_cloud import NetworkingV1TransitGatewayAttachmentSpecCloud

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1TransitGatewayAttachmentSpecCloud from a JSON string
networking_v1_transit_gateway_attachment_spec_cloud_instance = NetworkingV1TransitGatewayAttachmentSpecCloud.from_json(json)
# print the JSON string representation of the object
print NetworkingV1TransitGatewayAttachmentSpecCloud.to_json()

# convert the object into a dict
networking_v1_transit_gateway_attachment_spec_cloud_dict = networking_v1_transit_gateway_attachment_spec_cloud_instance.to_dict()
# create an instance of NetworkingV1TransitGatewayAttachmentSpecCloud from a dict
networking_v1_transit_gateway_attachment_spec_cloud_form_dict = networking_v1_transit_gateway_attachment_spec_cloud.from_dict(networking_v1_transit_gateway_attachment_spec_cloud_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


