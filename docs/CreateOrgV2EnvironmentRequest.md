# CreateOrgV2EnvironmentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**OrgV2EnvironmentMetadata**](OrgV2EnvironmentMetadata.md) |  | [optional] 
**display_name** | **str** | A human-readable name for the Environment | 

## Example

```python
from openapi_client.models.create_org_v2_environment_request import CreateOrgV2EnvironmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrgV2EnvironmentRequest from a JSON string
create_org_v2_environment_request_instance = CreateOrgV2EnvironmentRequest.from_json(json)
# print the JSON string representation of the object
print CreateOrgV2EnvironmentRequest.to_json()

# convert the object into a dict
create_org_v2_environment_request_dict = create_org_v2_environment_request_instance.to_dict()
# create an instance of CreateOrgV2EnvironmentRequest from a dict
create_org_v2_environment_request_form_dict = create_org_v2_environment_request.from_dict(create_org_v2_environment_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


