# CdxV1SharedTopic

The shared resource details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The shared resource kind | 
**topic** | **str** | The topic name | 

## Example

```python
from openapi_client.models.cdx_v1_shared_topic import CdxV1SharedTopic

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1SharedTopic from a JSON string
cdx_v1_shared_topic_instance = CdxV1SharedTopic.from_json(json)
# print the JSON string representation of the object
print CdxV1SharedTopic.to_json()

# convert the object into a dict
cdx_v1_shared_topic_dict = cdx_v1_shared_topic_instance.to_dict()
# create an instance of CdxV1SharedTopic from a dict
cdx_v1_shared_topic_form_dict = cdx_v1_shared_topic.from_dict(cdx_v1_shared_topic_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


