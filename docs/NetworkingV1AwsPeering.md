# NetworkingV1AwsPeering

AWS VPC Peering.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Peering kind type. | 
**account** | **str** | The AWS account ID | 
**vpc** | **str** | The VPC ID you are peering with Confluent Cloud network. | 
**routes** | **List[str]** | The [CIDR blocks](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) of the VPC you are peering with Confluent Cloud network. This is used by Confluent Cloud network to route traffic back to your network. The CIDR block must be a private range and cannot overlap with the Confluent Cloud CIDR block.  | 
**customer_region** | **str** | The region of the VPC you are peering with Confluent Cloud network. | 

## Example

```python
from openapi_client.models.networking_v1_aws_peering import NetworkingV1AwsPeering

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1AwsPeering from a JSON string
networking_v1_aws_peering_instance = NetworkingV1AwsPeering.from_json(json)
# print the JSON string representation of the object
print NetworkingV1AwsPeering.to_json()

# convert the object into a dict
networking_v1_aws_peering_dict = networking_v1_aws_peering_instance.to_dict()
# create an instance of NetworkingV1AwsPeering from a dict
networking_v1_aws_peering_form_dict = networking_v1_aws_peering.from_dict(networking_v1_aws_peering_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


