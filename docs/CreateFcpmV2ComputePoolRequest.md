# CreateFcpmV2ComputePoolRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**FcpmV2ComputePoolMetadata**](FcpmV2ComputePoolMetadata.md) |  | [optional] 
**spec** | [**CreateNetworkingV1PeeringRequestAllOfSpec**](CreateNetworkingV1PeeringRequestAllOfSpec.md) |  | 
**status** | [**FcpmV2ComputePoolStatus**](FcpmV2ComputePoolStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_fcpm_v2_compute_pool_request import CreateFcpmV2ComputePoolRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFcpmV2ComputePoolRequest from a JSON string
create_fcpm_v2_compute_pool_request_instance = CreateFcpmV2ComputePoolRequest.from_json(json)
# print the JSON string representation of the object
print CreateFcpmV2ComputePoolRequest.to_json()

# convert the object into a dict
create_fcpm_v2_compute_pool_request_dict = create_fcpm_v2_compute_pool_request_instance.to_dict()
# create an instance of CreateFcpmV2ComputePoolRequest from a dict
create_fcpm_v2_compute_pool_request_form_dict = create_fcpm_v2_compute_pool_request.from_dict(create_fcpm_v2_compute_pool_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


