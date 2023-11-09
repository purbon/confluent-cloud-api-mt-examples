# CdxV1ConsumerShareStatus

The status of the Consumer Share

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | Status of share | [readonly] 

## Example

```python
from openapi_client.models.cdx_v1_consumer_share_status import CdxV1ConsumerShareStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1ConsumerShareStatus from a JSON string
cdx_v1_consumer_share_status_instance = CdxV1ConsumerShareStatus.from_json(json)
# print the JSON string representation of the object
print CdxV1ConsumerShareStatus.to_json()

# convert the object into a dict
cdx_v1_consumer_share_status_dict = cdx_v1_consumer_share_status_instance.to_dict()
# create an instance of CdxV1ConsumerShareStatus from a dict
cdx_v1_consumer_share_status_form_dict = cdx_v1_consumer_share_status.from_dict(cdx_v1_consumer_share_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


