# NetworkingV1TransitGatewayAttachmentSpec

The desired state of the Transit Gateway Attachment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the TGW attachment | [optional] 
**cloud** | [**NetworkingV1TransitGatewayAttachmentSpecCloud**](NetworkingV1TransitGatewayAttachmentSpecCloud.md) |  | [optional] 
**environment** | [**ObjectReference**](ObjectReference.md) |  | [optional] 
**network** | [**ObjectReference**](ObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_transit_gateway_attachment_spec import NetworkingV1TransitGatewayAttachmentSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1TransitGatewayAttachmentSpec from a JSON string
networking_v1_transit_gateway_attachment_spec_instance = NetworkingV1TransitGatewayAttachmentSpec.from_json(json)
# print the JSON string representation of the object
print NetworkingV1TransitGatewayAttachmentSpec.to_json()

# convert the object into a dict
networking_v1_transit_gateway_attachment_spec_dict = networking_v1_transit_gateway_attachment_spec_instance.to_dict()
# create an instance of NetworkingV1TransitGatewayAttachmentSpec from a dict
networking_v1_transit_gateway_attachment_spec_form_dict = networking_v1_transit_gateway_attachment_spec.from_dict(networking_v1_transit_gateway_attachment_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


