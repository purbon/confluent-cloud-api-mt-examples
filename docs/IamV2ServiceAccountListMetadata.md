# IamV2ServiceAccountListMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **object** |  | [optional] 
**last** | **object** |  | [optional] 
**prev** | **object** |  | [optional] 
**next** | **object** |  | [optional] 
**total_size** | **int** | Number of records in the full result set. This response may be paginated and have a smaller number of records. | [optional] 

## Example

```python
from openapi_client.models.iam_v2_service_account_list_metadata import IamV2ServiceAccountListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2ServiceAccountListMetadata from a JSON string
iam_v2_service_account_list_metadata_instance = IamV2ServiceAccountListMetadata.from_json(json)
# print the JSON string representation of the object
print IamV2ServiceAccountListMetadata.to_json()

# convert the object into a dict
iam_v2_service_account_list_metadata_dict = iam_v2_service_account_list_metadata_instance.to_dict()
# create an instance of IamV2ServiceAccountListMetadata from a dict
iam_v2_service_account_list_metadata_form_dict = iam_v2_service_account_list_metadata.from_dict(iam_v2_service_account_list_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


