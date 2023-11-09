# NetworkingV1GcpPeering

GCP VPC Peering.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Peering kind type. | 
**project** | **str** | The Google Cloud project ID associated with the VPC that you are peering with Confluent Cloud network.  | 
**vpc_network** | **str** | The name of the VPC that you are peering with Confluent Cloud network. | 
**import_custom_routes** | **bool** | Enable customer route import. For more information, see [Importing custom routes](https://cloud.google.com/vpc/docs/vpc-peering#importing-exporting-routes).  | [optional] [default to False]

## Example

```python
from openapi_client.models.networking_v1_gcp_peering import NetworkingV1GcpPeering

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1GcpPeering from a JSON string
networking_v1_gcp_peering_instance = NetworkingV1GcpPeering.from_json(json)
# print the JSON string representation of the object
print NetworkingV1GcpPeering.to_json()

# convert the object into a dict
networking_v1_gcp_peering_dict = networking_v1_gcp_peering_instance.to_dict()
# create an instance of NetworkingV1GcpPeering from a dict
networking_v1_gcp_peering_form_dict = networking_v1_gcp_peering.from_dict(networking_v1_gcp_peering_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


