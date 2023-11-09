# NetworkingV1TransitGatewayAttachmentSpecUpdate

The desired state of the Transit Gateway Attachment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the TGW attachment | [optional] 
**environment** | [**ObjectReference**](ObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_transit_gateway_attachment_spec_update import NetworkingV1TransitGatewayAttachmentSpecUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1TransitGatewayAttachmentSpecUpdate from a JSON string
networking_v1_transit_gateway_attachment_spec_update_instance = NetworkingV1TransitGatewayAttachmentSpecUpdate.from_json(json)
# print the JSON string representation of the object
print NetworkingV1TransitGatewayAttachmentSpecUpdate.to_json()

# convert the object into a dict
networking_v1_transit_gateway_attachment_spec_update_dict = networking_v1_transit_gateway_attachment_spec_update_instance.to_dict()
# create an instance of NetworkingV1TransitGatewayAttachmentSpecUpdate from a dict
networking_v1_transit_gateway_attachment_spec_update_form_dict = networking_v1_transit_gateway_attachment_spec_update.from_dict(networking_v1_transit_gateway_attachment_spec_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


