# ListIamV2ApiKeys200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**IamV2ApiKeyListMetadata**](IamV2ApiKeyListMetadata.md) |  | 
**data** | [**List[ListIamV2ApiKeys200ResponseAllOfDataInner]**](ListIamV2ApiKeys200ResponseAllOfDataInner.md) |  | 

## Example

```python
from openapi_client.models.list_iam_v2_api_keys200_response import ListIamV2ApiKeys200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListIamV2ApiKeys200Response from a JSON string
list_iam_v2_api_keys200_response_instance = ListIamV2ApiKeys200Response.from_json(json)
# print the JSON string representation of the object
print ListIamV2ApiKeys200Response.to_json()

# convert the object into a dict
list_iam_v2_api_keys200_response_dict = list_iam_v2_api_keys200_response_instance.to_dict()
# create an instance of ListIamV2ApiKeys200Response from a dict
list_iam_v2_api_keys200_response_form_dict = list_iam_v2_api_keys200_response.from_dict(list_iam_v2_api_keys200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


