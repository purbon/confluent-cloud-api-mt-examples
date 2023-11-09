# AclDataList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceCollectionMetadata**](ResourceCollectionMetadata.md) |  | 
**data** | [**List[AclData]**](AclData.md) |  | 

## Example

```python
from openapi_client.models.acl_data_list import AclDataList

# TODO update the JSON string below
json = "{}"
# create an instance of AclDataList from a JSON string
acl_data_list_instance = AclDataList.from_json(json)
# print the JSON string representation of the object
print AclDataList.to_json()

# convert the object into a dict
acl_data_list_dict = acl_data_list_instance.to_dict()
# create an instance of AclDataList from a dict
acl_data_list_form_dict = acl_data_list.from_dict(acl_data_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


