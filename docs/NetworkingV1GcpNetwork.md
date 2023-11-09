# NetworkingV1GcpNetwork

The GCP network details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Network kind type. | 
**project** | **str** | The GCP Project ID associated with the Confluent Cloud VPC. | [readonly] 
**vpc_network** | **str** | The network name of the Confluent Cloud VPC. | [readonly] 
**private_service_connect_service_attachments** | **Dict[str, str]** | The mapping of zones to Private Service Connect Service Attachments if available. Keys are zones and values are [GCP Private Service Connect Service Attachment](https://cloud.google.com/vpc/docs/configure-private-service-connect-producer#api_7)  | [optional] [readonly] 

## Example

```python
from openapi_client.models.networking_v1_gcp_network import NetworkingV1GcpNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1GcpNetwork from a JSON string
networking_v1_gcp_network_instance = NetworkingV1GcpNetwork.from_json(json)
# print the JSON string representation of the object
print NetworkingV1GcpNetwork.to_json()

# convert the object into a dict
networking_v1_gcp_network_dict = networking_v1_gcp_network_instance.to_dict()
# create an instance of NetworkingV1GcpNetwork from a dict
networking_v1_gcp_network_form_dict = networking_v1_gcp_network.from_dict(networking_v1_gcp_network_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


