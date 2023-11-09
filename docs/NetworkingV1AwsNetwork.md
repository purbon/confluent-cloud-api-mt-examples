# NetworkingV1AwsNetwork

The AWS network details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Network kind type. | 
**vpc** | **str** | The Confluent Cloud VPC ID. | [readonly] 
**account** | **str** | The AWS account ID associated with the Confluent Cloud VPC. | [readonly] 
**private_link_endpoint_service** | **str** | The endpoint service of the Confluent Cloud VPC. (used for PrivateLink) if available. | [optional] [readonly] 

## Example

```python
from openapi_client.models.networking_v1_aws_network import NetworkingV1AwsNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1AwsNetwork from a JSON string
networking_v1_aws_network_instance = NetworkingV1AwsNetwork.from_json(json)
# print the JSON string representation of the object
print NetworkingV1AwsNetwork.to_json()

# convert the object into a dict
networking_v1_aws_network_dict = networking_v1_aws_network_instance.to_dict()
# create an instance of NetworkingV1AwsNetwork from a dict
networking_v1_aws_network_form_dict = networking_v1_aws_network.from_dict(networking_v1_aws_network_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


