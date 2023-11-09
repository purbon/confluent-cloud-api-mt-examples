# NetworkingV1TransitGatewayAttachmentUpdate

AWS Transit Gateway Attachments  Related guide: [APIs to manage AWS Transit Gateway Attachments](https://docs.confluent.io/cloud/current/networking/aws-transit-gateway.html).  ## The Transit Gateway Attachments Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.TransitGatewayAttachment\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `tgw_attachments_per_network` | Number of TGW attachments per network |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**NetworkingV1TransitGatewayAttachmentMetadata**](NetworkingV1TransitGatewayAttachmentMetadata.md) |  | [optional] 
**spec** | [**NetworkingV1TransitGatewayAttachmentSpecUpdate**](NetworkingV1TransitGatewayAttachmentSpecUpdate.md) |  | [optional] 
**status** | [**NetworkingV1TransitGatewayAttachmentStatus**](NetworkingV1TransitGatewayAttachmentStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_transit_gateway_attachment_update import NetworkingV1TransitGatewayAttachmentUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1TransitGatewayAttachmentUpdate from a JSON string
networking_v1_transit_gateway_attachment_update_instance = NetworkingV1TransitGatewayAttachmentUpdate.from_json(json)
# print the JSON string representation of the object
print NetworkingV1TransitGatewayAttachmentUpdate.to_json()

# convert the object into a dict
networking_v1_transit_gateway_attachment_update_dict = networking_v1_transit_gateway_attachment_update_instance.to_dict()
# create an instance of NetworkingV1TransitGatewayAttachmentUpdate from a dict
networking_v1_transit_gateway_attachment_update_form_dict = networking_v1_transit_gateway_attachment_update.from_dict(networking_v1_transit_gateway_attachment_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


