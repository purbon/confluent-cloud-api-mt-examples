# CdxV1NetworkCloud

The cloud-specific network details. These will be populated when the network reaches the READY state.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Network kind type. | 
**private_link_endpoint_service** | **str** | The AWS VPC endpoint service for the network (used for PrivateLink) if available. | [optional] [readonly] 
**private_link_service_aliases** | **Dict[str, str]** | The mapping of zones to PrivateLink Service Aliases if available.  Keys are zones and values are [Azure PrivateLink Service Aliases](https://docs.microsoft.com/en-us/azure/private-link/private-link-service-overview#share-your-service)  | [optional] [readonly] 
**private_service_connect_service_attachments** | **Dict[str, str]** | The mapping of zones to Private Service Connect Service Attachments if available. Keys are zones and values are [GCP Private Service Connect Service Attachment](https://cloud.google.com/vpc/docs/configure-private-service-connect-producer#api_7)  | [optional] [readonly] 

## Example

```python
from openapi_client.models.cdx_v1_network_cloud import CdxV1NetworkCloud

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1NetworkCloud from a JSON string
cdx_v1_network_cloud_instance = CdxV1NetworkCloud.from_json(json)
# print the JSON string representation of the object
print CdxV1NetworkCloud.to_json()

# convert the object into a dict
cdx_v1_network_cloud_dict = cdx_v1_network_cloud_instance.to_dict()
# create an instance of CdxV1NetworkCloud from a dict
cdx_v1_network_cloud_form_dict = cdx_v1_network_cloud.from_dict(cdx_v1_network_cloud_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


