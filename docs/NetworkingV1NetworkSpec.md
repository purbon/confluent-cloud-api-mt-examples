# NetworkingV1NetworkSpec

The desired state of the Network

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the network | [optional] 
**cloud** | **str** | The cloud service provider in which the network exists. | [optional] 
**region** | **str** | The cloud service provider region in which the network exists. | [optional] 
**connection_types** | **List[str]** | The connection types requested for use with the network. | [optional] 
**cidr** | **str** | IPv4 CIDR block | [optional] 
**zones** | **List[str]** | The 3 availability zones for this network. They can optionally be specified for AWS networks used with PrivateLink, for GCP networks used with Private Service Connect, and for AWS and GCP networks used with Peering. Otherwise, they are automatically chosen by Confluent Cloud.  On AWS, zones are AWS [AZ IDs](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html)  (e.g. use1-az3)  On GCP, zones are GCP [zones](https://cloud.google.com/compute/docs/regions-zones)  (e.g. us-central1-c).  On Azure, zones are Confluent-chosen names (e.g. 1, 2, 3) since Azure does not  have universal zone identifiers.  | [optional] 
**zones_info** | [**List[NetworkingV1ZoneInfo]**](NetworkingV1ZoneInfo.md) | Cloud provider zones metadata. | [optional] 
**dns_config** | [**NetworkingV1DnsConfig**](NetworkingV1DnsConfig.md) |  | [optional] 
**reserved_cidr** | **str** | The reserved CIDR config is used only by AWS networks with connection_types &#x3D; Vpc_Peering or Transit_Gateway  An IPv4 [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)   reserved for Confluent Cloud Network. Must be \\24.   If not specified, Confluent Cloud Network uses 172.20.255.0/24  Note - The attribute is in a [Limited Availability lifecycle stage](https://docs.confluent.io/cloud/current/api.html#section/Versioning/API-Lifecycle-Policy)  | [optional] 
**environment** | [**ObjectReference**](ObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_network_spec import NetworkingV1NetworkSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkSpec from a JSON string
networking_v1_network_spec_instance = NetworkingV1NetworkSpec.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkSpec.to_json()

# convert the object into a dict
networking_v1_network_spec_dict = networking_v1_network_spec_instance.to_dict()
# create an instance of NetworkingV1NetworkSpec from a dict
networking_v1_network_spec_form_dict = networking_v1_network_spec.from_dict(networking_v1_network_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


