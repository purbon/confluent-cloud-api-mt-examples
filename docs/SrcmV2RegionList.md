# SrcmV2RegionList

`Region` objects represent cloud provider regions available when placing Schema Registry clusters. The API allows you to list Schema Registry regions.   Related guide: [Confluent Cloud Schema Registry Regions](https://docs.confluent.io/cloud/current/stream-governance/clusters-regions-api.html#schema-registry-regions).  ## The Regions Model <SchemaDefinition schemaRef=\"#/components/schemas/srcm.v2.Region\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**SrcmV2RegionListMetadata**](SrcmV2RegionListMetadata.md) |  | 
**data** | [**List[SrcmV2RegionListDataInner]**](SrcmV2RegionListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.srcm_v2_region_list import SrcmV2RegionList

# TODO update the JSON string below
json = "{}"
# create an instance of SrcmV2RegionList from a JSON string
srcm_v2_region_list_instance = SrcmV2RegionList.from_json(json)
# print the JSON string representation of the object
print SrcmV2RegionList.to_json()

# convert the object into a dict
srcm_v2_region_list_dict = srcm_v2_region_list_instance.to_dict()
# create an instance of SrcmV2RegionList from a dict
srcm_v2_region_list_form_dict = srcm_v2_region_list.from_dict(srcm_v2_region_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


