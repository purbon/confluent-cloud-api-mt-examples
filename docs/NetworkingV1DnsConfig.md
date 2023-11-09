# NetworkingV1DnsConfig

The network DNS config

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution** | **str** | Network DNS resolution type. | 

## Example

```python
from openapi_client.models.networking_v1_dns_config import NetworkingV1DnsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1DnsConfig from a JSON string
networking_v1_dns_config_instance = NetworkingV1DnsConfig.from_json(json)
# print the JSON string representation of the object
print NetworkingV1DnsConfig.to_json()

# convert the object into a dict
networking_v1_dns_config_dict = networking_v1_dns_config_instance.to_dict()
# create an instance of NetworkingV1DnsConfig from a dict
networking_v1_dns_config_form_dict = networking_v1_dns_config.from_dict(networking_v1_dns_config_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


