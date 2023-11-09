# CdxV1SharedSubject

The shared resource details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The shared resource kind | 
**subject** | **str** | The subject name | 

## Example

```python
from openapi_client.models.cdx_v1_shared_subject import CdxV1SharedSubject

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1SharedSubject from a JSON string
cdx_v1_shared_subject_instance = CdxV1SharedSubject.from_json(json)
# print the JSON string representation of the object
print CdxV1SharedSubject.to_json()

# convert the object into a dict
cdx_v1_shared_subject_dict = cdx_v1_shared_subject_instance.to_dict()
# create an instance of CdxV1SharedSubject from a dict
cdx_v1_shared_subject_form_dict = cdx_v1_shared_subject.from_dict(cdx_v1_shared_subject_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


