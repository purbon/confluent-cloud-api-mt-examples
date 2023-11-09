# CreateAclRequestDataList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CreateAclRequestData]**](CreateAclRequestData.md) |  | 

## Example

```python
from openapi_client.models.create_acl_request_data_list import CreateAclRequestDataList

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAclRequestDataList from a JSON string
create_acl_request_data_list_instance = CreateAclRequestDataList.from_json(json)
# print the JSON string representation of the object
print CreateAclRequestDataList.to_json()

# convert the object into a dict
create_acl_request_data_list_dict = create_acl_request_data_list_instance.to_dict()
# create an instance of CreateAclRequestDataList from a dict
create_acl_request_data_list_form_dict = create_acl_request_data_list.from_dict(create_acl_request_data_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


