# ListNetworkingV1TransitGatewayAttachments200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**NetworkingV1TransitGatewayAttachmentListMetadata**](NetworkingV1TransitGatewayAttachmentListMetadata.md) |  | 
**data** | [**List[ListNetworkingV1Peerings200ResponseAllOfDataInner]**](ListNetworkingV1Peerings200ResponseAllOfDataInner.md) |  | 

## Example

```python
from openapi_client.models.list_networking_v1_transit_gateway_attachments200_response import ListNetworkingV1TransitGatewayAttachments200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListNetworkingV1TransitGatewayAttachments200Response from a JSON string
list_networking_v1_transit_gateway_attachments200_response_instance = ListNetworkingV1TransitGatewayAttachments200Response.from_json(json)
# print the JSON string representation of the object
print ListNetworkingV1TransitGatewayAttachments200Response.to_json()

# convert the object into a dict
list_networking_v1_transit_gateway_attachments200_response_dict = list_networking_v1_transit_gateway_attachments200_response_instance.to_dict()
# create an instance of ListNetworkingV1TransitGatewayAttachments200Response from a dict
list_networking_v1_transit_gateway_attachments200_response_form_dict = list_networking_v1_transit_gateway_attachments200_response.from_dict(list_networking_v1_transit_gateway_attachments200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


