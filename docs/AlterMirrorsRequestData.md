# AlterMirrorsRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mirror_topic_names** | **List[str]** | The mirror topics specified as a list of topic names. | [optional] 
**mirror_topic_name_pattern** | **str** | The mirror topics specified as a pattern. | [optional] 

## Example

```python
from openapi_client.models.alter_mirrors_request_data import AlterMirrorsRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of AlterMirrorsRequestData from a JSON string
alter_mirrors_request_data_instance = AlterMirrorsRequestData.from_json(json)
# print the JSON string representation of the object
print AlterMirrorsRequestData.to_json()

# convert the object into a dict
alter_mirrors_request_data_dict = alter_mirrors_request_data_instance.to_dict()
# create an instance of AlterMirrorsRequestData from a dict
alter_mirrors_request_data_form_dict = alter_mirrors_request_data.from_dict(alter_mirrors_request_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


