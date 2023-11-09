# SrcmV2RegionSpec

The desired state of the Region

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name. | [optional] [readonly] 
**cloud** | **str** | The cloud service provider that hosts the region. | [optional] [readonly] 
**region_name** | **str** | The region name. | [optional] [readonly] 
**packages** | **List[str]** | List of Stream Governance packages allowing placement in this region. | [optional] [readonly] 

## Example

```python
from openapi_client.models.srcm_v2_region_spec import SrcmV2RegionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SrcmV2RegionSpec from a JSON string
srcm_v2_region_spec_instance = SrcmV2RegionSpec.from_json(json)
# print the JSON string representation of the object
print SrcmV2RegionSpec.to_json()

# convert the object into a dict
srcm_v2_region_spec_dict = srcm_v2_region_spec_instance.to_dict()
# create an instance of SrcmV2RegionSpec from a dict
srcm_v2_region_spec_form_dict = srcm_v2_region_spec.from_dict(srcm_v2_region_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


