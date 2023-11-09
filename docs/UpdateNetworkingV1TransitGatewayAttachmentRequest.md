# UpdateNetworkingV1TransitGatewayAttachmentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**NetworkingV1TransitGatewayAttachmentMetadata**](NetworkingV1TransitGatewayAttachmentMetadata.md) |  | [optional] 
**spec** | [**UpdateCmkV2ClusterRequestAllOfSpec**](UpdateCmkV2ClusterRequestAllOfSpec.md) |  | 
**status** | [**NetworkingV1TransitGatewayAttachmentStatus**](NetworkingV1TransitGatewayAttachmentStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_networking_v1_transit_gateway_attachment_request import UpdateNetworkingV1TransitGatewayAttachmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNetworkingV1TransitGatewayAttachmentRequest from a JSON string
update_networking_v1_transit_gateway_attachment_request_instance = UpdateNetworkingV1TransitGatewayAttachmentRequest.from_json(json)
# print the JSON string representation of the object
print UpdateNetworkingV1TransitGatewayAttachmentRequest.to_json()

# convert the object into a dict
update_networking_v1_transit_gateway_attachment_request_dict = update_networking_v1_transit_gateway_attachment_request_instance.to_dict()
# create an instance of UpdateNetworkingV1TransitGatewayAttachmentRequest from a dict
update_networking_v1_transit_gateway_attachment_request_form_dict = update_networking_v1_transit_gateway_attachment_request.from_dict(update_networking_v1_transit_gateway_attachment_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


