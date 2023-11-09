# NetworkingV1TransitGatewayAttachmentStatus

The status of the Transit Gateway Attachment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecycle phase of the TGW attachment:    PROVISIONING: attachment provisioning is in progress;    PENDING_ACCEPT: attachment request is pending acceptance by the customer;    READY:  attachment is ready;    FAILED: attachment is in a failed state;    DEPROVISIONING: attachment deprovisioning is in progress;    DISCONNECTED: attachment was manually deleted directly in the cloud provider by the customer;    ERROR: invalid customer input during attachment creation.  | [readonly] 
**error_code** | **str** | Error code if TGW attachment is in a failed state. May be used for programmatic error checking. | [optional] [readonly] 
**error_message** | **str** | Displayable error message if TGW attachment is in a failed state | [optional] [readonly] 
**cloud** | [**NetworkingV1TransitGatewayAttachmentStatusCloud**](NetworkingV1TransitGatewayAttachmentStatusCloud.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_transit_gateway_attachment_status import NetworkingV1TransitGatewayAttachmentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1TransitGatewayAttachmentStatus from a JSON string
networking_v1_transit_gateway_attachment_status_instance = NetworkingV1TransitGatewayAttachmentStatus.from_json(json)
# print the JSON string representation of the object
print NetworkingV1TransitGatewayAttachmentStatus.to_json()

# convert the object into a dict
networking_v1_transit_gateway_attachment_status_dict = networking_v1_transit_gateway_attachment_status_instance.to_dict()
# create an instance of NetworkingV1TransitGatewayAttachmentStatus from a dict
networking_v1_transit_gateway_attachment_status_form_dict = networking_v1_transit_gateway_attachment_status.from_dict(networking_v1_transit_gateway_attachment_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


