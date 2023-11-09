# AclData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**resource_type** | [**AclResourceType**](AclResourceType.md) |  | 
**resource_name** | **str** |  | 
**pattern_type** | **str** |  | 
**principal** | **str** |  | 
**host** | **str** |  | 
**operation** | **str** |  | 
**permission** | **str** |  | 

## Example

```python
from openapi_client.models.acl_data import AclData

# TODO update the JSON string below
json = "{}"
# create an instance of AclData from a JSON string
acl_data_instance = AclData.from_json(json)
# print the JSON string representation of the object
print AclData.to_json()

# convert the object into a dict
acl_data_dict = acl_data_instance.to_dict()
# create an instance of AclData from a dict
acl_data_form_dict = acl_data.from_dict(acl_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


