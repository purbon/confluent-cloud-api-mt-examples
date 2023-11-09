# NetworkingV1AwsTransitGatewayAttachment

AWS Transit Gateway Attachment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | AWS Transit Gateway Attachment kind type. | 
**ram_share_arn** | **str** | The full AWS Resource Name (ARN) for the AWS Resource Access Manager (RAM) Share of the Transit Gateways that you want Confluent Cloud to be attached to. | 
**transit_gateway_id** | **str** | The ID of the AWS Transit Gateway that you want Confluent CLoud to be attached to. | 
**routes** | **List[str]** | List of destination routes. | 

## Example

```python
from openapi_client.models.networking_v1_aws_transit_gateway_attachment import NetworkingV1AwsTransitGatewayAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1AwsTransitGatewayAttachment from a JSON string
networking_v1_aws_transit_gateway_attachment_instance = NetworkingV1AwsTransitGatewayAttachment.from_json(json)
# print the JSON string representation of the object
print NetworkingV1AwsTransitGatewayAttachment.to_json()

# convert the object into a dict
networking_v1_aws_transit_gateway_attachment_dict = networking_v1_aws_transit_gateway_attachment_instance.to_dict()
# create an instance of NetworkingV1AwsTransitGatewayAttachment from a dict
networking_v1_aws_transit_gateway_attachment_form_dict = networking_v1_aws_transit_gateway_attachment.from_dict(networking_v1_aws_transit_gateway_attachment_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


