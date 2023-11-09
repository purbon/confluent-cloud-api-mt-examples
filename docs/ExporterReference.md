# ExporterReference

The format for a typical exporter object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the exporter | [optional] 
**context_type** | **str** | Context type of the exporter. One of CUSTOM, NONE or AUTO (default) | [optional] 
**context** | **str** | Customized context of the exporter if contextType equals CUSTOM. | [optional] 
**subjects** | **List[str]** | Name of each exporter subject | [optional] 
**subject_rename_format** | **str** | Format string for the subject name in the destination cluster, which may contain ${subject} as a placeholder for the originating subject name. For example, dc_${subject} for the subject orders will map to the destination subject name dc_orders. | [optional] 
**config** | **Dict[str, str]** | The map containing exporter’s configurations | [optional] 

## Example

```python
from openapi_client.models.exporter_reference import ExporterReference

# TODO update the JSON string below
json = "{}"
# create an instance of ExporterReference from a JSON string
exporter_reference_instance = ExporterReference.from_json(json)
# print the JSON string representation of the object
print ExporterReference.to_json()

# convert the object into a dict
exporter_reference_dict = exporter_reference_instance.to_dict()
# create an instance of ExporterReference from a dict
exporter_reference_form_dict = exporter_reference.from_dict(exporter_reference_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


