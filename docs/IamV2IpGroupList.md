# IamV2IpGroupList

Definitions of networks which can be named and referred by IP blocks, commonly used to attach to IP Filter rules.   ## The IP Groups Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.IpGroup\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**IamV2IpGroupListMetadata**](IamV2IpGroupListMetadata.md) |  | 
**data** | [**List[IamV2IpGroupListDataInner]**](IamV2IpGroupListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.iam_v2_ip_group_list import IamV2IpGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2IpGroupList from a JSON string
iam_v2_ip_group_list_instance = IamV2IpGroupList.from_json(json)
# print the JSON string representation of the object
print IamV2IpGroupList.to_json()

# convert the object into a dict
iam_v2_ip_group_list_dict = iam_v2_ip_group_list_instance.to_dict()
# create an instance of IamV2IpGroupList from a dict
iam_v2_ip_group_list_form_dict = iam_v2_ip_group_list.from_dict(iam_v2_ip_group_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


