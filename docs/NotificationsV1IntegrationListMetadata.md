# NotificationsV1IntegrationListMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **object** |  | [optional] 
**last** | **object** |  | [optional] 
**prev** | **object** |  | [optional] 
**next** | **object** |  | [optional] 
**total_size** | **int** | Number of records in the full result set. This response may be paginated and have a smaller number of records. | [optional] 

## Example

```python
from openapi_client.models.notifications_v1_integration_list_metadata import NotificationsV1IntegrationListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsV1IntegrationListMetadata from a JSON string
notifications_v1_integration_list_metadata_instance = NotificationsV1IntegrationListMetadata.from_json(json)
# print the JSON string representation of the object
print NotificationsV1IntegrationListMetadata.to_json()

# convert the object into a dict
notifications_v1_integration_list_metadata_dict = notifications_v1_integration_list_metadata_instance.to_dict()
# create an instance of NotificationsV1IntegrationListMetadata from a dict
notifications_v1_integration_list_metadata_form_dict = notifications_v1_integration_list_metadata.from_dict(notifications_v1_integration_list_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


