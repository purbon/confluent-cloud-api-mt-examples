# NetworkingV1AwsVpcEndpointService

AWS VPC Endpoint service that can be used to create VPC Endpoints. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpc_endpoint_service_name** | **str** | Id of the VPC Endpoint service. | [readonly] 

## Example

```python
from openapi_client.models.networking_v1_aws_vpc_endpoint_service import NetworkingV1AwsVpcEndpointService

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1AwsVpcEndpointService from a JSON string
networking_v1_aws_vpc_endpoint_service_instance = NetworkingV1AwsVpcEndpointService.from_json(json)
# print the JSON string representation of the object
print NetworkingV1AwsVpcEndpointService.to_json()

# convert the object into a dict
networking_v1_aws_vpc_endpoint_service_dict = networking_v1_aws_vpc_endpoint_service_instance.to_dict()
# create an instance of NetworkingV1AwsVpcEndpointService from a dict
networking_v1_aws_vpc_endpoint_service_form_dict = networking_v1_aws_vpc_endpoint_service.from_dict(networking_v1_aws_vpc_endpoint_service_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


