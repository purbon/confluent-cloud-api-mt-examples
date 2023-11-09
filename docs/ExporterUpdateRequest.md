# ExporterUpdateRequest

Exporter update request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_type** | **str** | Context type of the exporter. One of CUSTOM, NONE or AUTO (default) | [optional] 
**context** | **str** | Customized context of the exporter if contextType equals CUSTOM. | [optional] 
**subjects** | **List[str]** | Name of each exporter subject | [optional] 
**subject_rename_format** | **str** | Format string for the subject name in the destination cluster, which may contain ${subject} as a placeholder for the originating subject name. For example, dc_${subject} for the subject orders will map to the destination subject name dc_orders. | [optional] 
**config** | **Dict[str, str]** | The map containing exporter’s configurations | [optional] 

## Example

```python
from openapi_client.models.exporter_update_request import ExporterUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExporterUpdateRequest from a JSON string
exporter_update_request_instance = ExporterUpdateRequest.from_json(json)
# print the JSON string representation of the object
print ExporterUpdateRequest.to_json()

# convert the object into a dict
exporter_update_request_dict = exporter_update_request_instance.to_dict()
# create an instance of ExporterUpdateRequest from a dict
exporter_update_request_form_dict = exporter_update_request.from_dict(exporter_update_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


