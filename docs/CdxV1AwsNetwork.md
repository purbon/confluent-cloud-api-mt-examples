# CdxV1AwsNetwork

The AWS network details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Network kind type. | 
**private_link_endpoint_service** | **str** | The AWS VPC endpoint service for the network (used for PrivateLink) if available. | [optional] [readonly] 

## Example

```python
from openapi_client.models.cdx_v1_aws_network import CdxV1AwsNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1AwsNetwork from a JSON string
cdx_v1_aws_network_instance = CdxV1AwsNetwork.from_json(json)
# print the JSON string representation of the object
print CdxV1AwsNetwork.to_json()

# convert the object into a dict
cdx_v1_aws_network_dict = cdx_v1_aws_network_instance.to_dict()
# create an instance of CdxV1AwsNetwork from a dict
cdx_v1_aws_network_form_dict = cdx_v1_aws_network.from_dict(cdx_v1_aws_network_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


