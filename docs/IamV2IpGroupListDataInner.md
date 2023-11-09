# IamV2IpGroupListDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**metadata** | [**IamV2IpGroupMetadata**](IamV2IpGroupMetadata.md) |  | 
**group_name** | **str** | A human readable name for an IP Group. Can contain any unicode letter or number, the ASCII space character, or any of the following special characters: &#x60;[&#x60;, &#x60;]&#x60;, &#x60;|&#x60;, &#x60;&amp;&#x60;, &#x60;+&#x60;, &#x60;-&#x60;, &#x60;_&#x60;, &#x60;/&#x60;, &#x60;.&#x60;, &#x60;,&#x60;.  | 
**cidr_blocks** | **List[str]** | A list of CIDRs. | 

## Example

```python
from openapi_client.models.iam_v2_ip_group_list_data_inner import IamV2IpGroupListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2IpGroupListDataInner from a JSON string
iam_v2_ip_group_list_data_inner_instance = IamV2IpGroupListDataInner.from_json(json)
# print the JSON string representation of the object
print IamV2IpGroupListDataInner.to_json()

# convert the object into a dict
iam_v2_ip_group_list_data_inner_dict = iam_v2_ip_group_list_data_inner_instance.to_dict()
# create an instance of IamV2IpGroupListDataInner from a dict
iam_v2_ip_group_list_data_inner_form_dict = iam_v2_ip_group_list_data_inner.from_dict(iam_v2_ip_group_list_data_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


