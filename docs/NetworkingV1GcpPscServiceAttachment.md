# NetworkingV1GcpPscServiceAttachment

GCP PSC Service attachment for a zone with reserved capacity to connect a PSC Endpoint. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone** | **str** | Zone associated with the PSC Service attachment. | [readonly] 
**private_service_connect_service_attachment** | **str** | Id of a Private Service Connect Service Attachment in Confluent Cloud. | [readonly] 

## Example

```python
from openapi_client.models.networking_v1_gcp_psc_service_attachment import NetworkingV1GcpPscServiceAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1GcpPscServiceAttachment from a JSON string
networking_v1_gcp_psc_service_attachment_instance = NetworkingV1GcpPscServiceAttachment.from_json(json)
# print the JSON string representation of the object
print NetworkingV1GcpPscServiceAttachment.to_json()

# convert the object into a dict
networking_v1_gcp_psc_service_attachment_dict = networking_v1_gcp_psc_service_attachment_instance.to_dict()
# create an instance of NetworkingV1GcpPscServiceAttachment from a dict
networking_v1_gcp_psc_service_attachment_form_dict = networking_v1_gcp_psc_service_attachment.from_dict(networking_v1_gcp_psc_service_attachment_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


