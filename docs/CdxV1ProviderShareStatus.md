# CdxV1ProviderShareStatus

The status of the Provider Share

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | Status of share | [readonly] 

## Example

```python
from openapi_client.models.cdx_v1_provider_share_status import CdxV1ProviderShareStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1ProviderShareStatus from a JSON string
cdx_v1_provider_share_status_instance = CdxV1ProviderShareStatus.from_json(json)
# print the JSON string representation of the object
print CdxV1ProviderShareStatus.to_json()

# convert the object into a dict
cdx_v1_provider_share_status_dict = cdx_v1_provider_share_status_instance.to_dict()
# create an instance of CdxV1ProviderShareStatus from a dict
cdx_v1_provider_share_status_form_dict = cdx_v1_provider_share_status.from_dict(cdx_v1_provider_share_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


