# NetworkingV1ZoneInfo

Cloud provider zone metadata.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_id** | **str** | Cloud provider zone id | [optional] 
**cidr** | **str** | The IPv4 [CIDR block](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) to used for this network. Must be a &#x60;/27&#x60;. Required for VPC peering and AWS TransitGateway.  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_zone_info import NetworkingV1ZoneInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1ZoneInfo from a JSON string
networking_v1_zone_info_instance = NetworkingV1ZoneInfo.from_json(json)
# print the JSON string representation of the object
print NetworkingV1ZoneInfo.to_json()

# convert the object into a dict
networking_v1_zone_info_dict = networking_v1_zone_info_instance.to_dict()
# create an instance of NetworkingV1ZoneInfo from a dict
networking_v1_zone_info_form_dict = networking_v1_zone_info.from_dict(networking_v1_zone_info_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


