# NetworkingV1TransitGatewayAttachmentList

AWS Transit Gateway Attachments  Related guide: [APIs to manage AWS Transit Gateway Attachments](https://docs.confluent.io/cloud/current/networking/aws-transit-gateway.html).  ## The Transit Gateway Attachments Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.TransitGatewayAttachment\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `tgw_attachments_per_network` | Number of TGW attachments per network |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**NetworkingV1TransitGatewayAttachmentListMetadata**](NetworkingV1TransitGatewayAttachmentListMetadata.md) |  | 
**data** | [**List[NetworkingV1TransitGatewayAttachmentListDataInner]**](NetworkingV1TransitGatewayAttachmentListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.networking_v1_transit_gateway_attachment_list import NetworkingV1TransitGatewayAttachmentList

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1TransitGatewayAttachmentList from a JSON string
networking_v1_transit_gateway_attachment_list_instance = NetworkingV1TransitGatewayAttachmentList.from_json(json)
# print the JSON string representation of the object
print NetworkingV1TransitGatewayAttachmentList.to_json()

# convert the object into a dict
networking_v1_transit_gateway_attachment_list_dict = networking_v1_transit_gateway_attachment_list_instance.to_dict()
# create an instance of NetworkingV1TransitGatewayAttachmentList from a dict
networking_v1_transit_gateway_attachment_list_form_dict = networking_v1_transit_gateway_attachment_list.from_dict(networking_v1_transit_gateway_attachment_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


