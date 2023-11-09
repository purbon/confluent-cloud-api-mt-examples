# IamV2IpFilter

`IP Filter` objects are bindings between IP Groups and Confluent resource(s). For example, a binding between \"CorpNet\" and \"Management APIs\" will enforce that access must come from one of the CIDR blocks associated with CorpNet. If there are multiple IP filters bound to a resource, a request matching any of the CIDR blocks for any of the IP Group will allow the request. If there are no IP Filters for a resource, then access will be granted to requests originating from any IP Address.   ## The IP Filters Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.IpFilter\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**IamV2IpFilterMetadata**](IamV2IpFilterMetadata.md) |  | [optional] 
**filter_name** | **str** | A human readable name for an IP Filter. Can contain any unicode letter or number, the ASCII space character, or any of the following special characters: &#x60;[&#x60;, &#x60;]&#x60;, &#x60;|&#x60;, &#x60;&amp;&#x60;, &#x60;+&#x60;, &#x60;-&#x60;, &#x60;_&#x60;, &#x60;/&#x60;, &#x60;.&#x60;, &#x60;,&#x60;.  | [optional] 
**resource_group** | **str** | Scope of resources covered by this IP filter. The only resource_group currently available is \&quot;management\&quot;. | [optional] 
**ip_groups** | [**List[GlobalObjectReference]**](GlobalObjectReference.md) | A list of IP Groups. | [optional] 

## Example

```python
from openapi_client.models.iam_v2_ip_filter import IamV2IpFilter

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2IpFilter from a JSON string
iam_v2_ip_filter_instance = IamV2IpFilter.from_json(json)
# print the JSON string representation of the object
print IamV2IpFilter.to_json()

# convert the object into a dict
iam_v2_ip_filter_dict = iam_v2_ip_filter_instance.to_dict()
# create an instance of IamV2IpFilter from a dict
iam_v2_ip_filter_form_dict = iam_v2_ip_filter.from_dict(iam_v2_ip_filter_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


