# CdxV1EmailConsumerRestriction

Consumer restrictions limits by authenticated user's email

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The resource kind | 
**email** | **str** | Email based matching for the consumers | 

## Example

```python
from openapi_client.models.cdx_v1_email_consumer_restriction import CdxV1EmailConsumerRestriction

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1EmailConsumerRestriction from a JSON string
cdx_v1_email_consumer_restriction_instance = CdxV1EmailConsumerRestriction.from_json(json)
# print the JSON string representation of the object
print CdxV1EmailConsumerRestriction.to_json()

# convert the object into a dict
cdx_v1_email_consumer_restriction_dict = cdx_v1_email_consumer_restriction_instance.to_dict()
# create an instance of CdxV1EmailConsumerRestriction from a dict
cdx_v1_email_consumer_restriction_form_dict = cdx_v1_email_consumer_restriction.from_dict(cdx_v1_email_consumer_restriction_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


