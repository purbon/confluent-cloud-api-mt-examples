# SubjectVersion

Subject version pair

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Name of the subject | [optional] 
**version** | **int** | Version number | [optional] 

## Example

```python
from openapi_client.models.subject_version import SubjectVersion

# TODO update the JSON string below
json = "{}"
# create an instance of SubjectVersion from a JSON string
subject_version_instance = SubjectVersion.from_json(json)
# print the JSON string representation of the object
print SubjectVersion.to_json()

# convert the object into a dict
subject_version_dict = subject_version_instance.to_dict()
# create an instance of SubjectVersion from a dict
subject_version_form_dict = subject_version.from_dict(subject_version_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


