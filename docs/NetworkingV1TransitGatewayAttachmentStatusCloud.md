# NetworkingV1TransitGatewayAttachmentStatusCloud

The cloud-specific TGW attachment details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | AWS Transit Gateway Attachment Status kind type. | [optional] 
**transit_gateway_attachment_id** | **str** | The ID of the AWS Transit Gateway VPC Attachment that attaches Confluent VPC to Transit Gateway. | [readonly] 

## Example

```python
from openapi_client.models.networking_v1_transit_gateway_attachment_status_cloud import NetworkingV1TransitGatewayAttachmentStatusCloud

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1TransitGatewayAttachmentStatusCloud from a JSON string
networking_v1_transit_gateway_attachment_status_cloud_instance = NetworkingV1TransitGatewayAttachmentStatusCloud.from_json(json)
# print the JSON string representation of the object
print NetworkingV1TransitGatewayAttachmentStatusCloud.to_json()

# convert the object into a dict
networking_v1_transit_gateway_attachment_status_cloud_dict = networking_v1_transit_gateway_attachment_status_cloud_instance.to_dict()
# create an instance of NetworkingV1TransitGatewayAttachmentStatusCloud from a dict
networking_v1_transit_gateway_attachment_status_cloud_form_dict = networking_v1_transit_gateway_attachment_status_cloud.from_dict(networking_v1_transit_gateway_attachment_status_cloud_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


