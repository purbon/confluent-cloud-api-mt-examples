# CreateAclRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | [**AclResourceType**](AclResourceType.md) |  | 
**resource_name** | **str** |  | 
**pattern_type** | **str** |  | 
**principal** | **str** |  | 
**host** | **str** |  | 
**operation** | **str** |  | 
**permission** | **str** |  | 

## Example

```python
from openapi_client.models.create_acl_request_data import CreateAclRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAclRequestData from a JSON string
create_acl_request_data_instance = CreateAclRequestData.from_json(json)
# print the JSON string representation of the object
print CreateAclRequestData.to_json()

# convert the object into a dict
create_acl_request_data_dict = create_acl_request_data_instance.to_dict()
# create an instance of CreateAclRequestData from a dict
create_acl_request_data_form_dict = create_acl_request_data.from_dict(create_acl_request_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


