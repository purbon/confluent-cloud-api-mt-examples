# IamV2IpFilterList

`IP Filter` objects are bindings between IP Groups and Confluent resource(s). For example, a binding between \"CorpNet\" and \"Management APIs\" will enforce that access must come from one of the CIDR blocks associated with CorpNet. If there are multiple IP filters bound to a resource, a request matching any of the CIDR blocks for any of the IP Group will allow the request. If there are no IP Filters for a resource, then access will be granted to requests originating from any IP Address.   ## The IP Filters Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.IpFilter\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**IamV2IpFilterListMetadata**](IamV2IpFilterListMetadata.md) |  | 
**data** | [**List[IamV2IpFilterListDataInner]**](IamV2IpFilterListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.iam_v2_ip_filter_list import IamV2IpFilterList

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2IpFilterList from a JSON string
iam_v2_ip_filter_list_instance = IamV2IpFilterList.from_json(json)
# print the JSON string representation of the object
print IamV2IpFilterList.to_json()

# convert the object into a dict
iam_v2_ip_filter_list_dict = iam_v2_ip_filter_list_instance.to_dict()
# create an instance of IamV2IpFilterList from a dict
iam_v2_ip_filter_list_form_dict = iam_v2_ip_filter_list.from_dict(iam_v2_ip_filter_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


