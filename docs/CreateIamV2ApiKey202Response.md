# CreateIamV2ApiKey202Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**IamV2ApiKeyMetadata**](IamV2ApiKeyMetadata.md) |  | [optional] 
**spec** | [**ListIamV2ApiKeys200ResponseAllOfDataInnerSpec**](ListIamV2ApiKeys200ResponseAllOfDataInnerSpec.md) |  | 

## Example

```python
from openapi_client.models.create_iam_v2_api_key202_response import CreateIamV2ApiKey202Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIamV2ApiKey202Response from a JSON string
create_iam_v2_api_key202_response_instance = CreateIamV2ApiKey202Response.from_json(json)
# print the JSON string representation of the object
print CreateIamV2ApiKey202Response.to_json()

# convert the object into a dict
create_iam_v2_api_key202_response_dict = create_iam_v2_api_key202_response_instance.to_dict()
# create an instance of CreateIamV2ApiKey202Response from a dict
create_iam_v2_api_key202_response_form_dict = create_iam_v2_api_key202_response.from_dict(create_iam_v2_api_key202_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


