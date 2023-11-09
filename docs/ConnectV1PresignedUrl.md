# ConnectV1PresignedUrl

Request a presigned upload URL for new Custom Connector Plugin. Note that the URL policy expires in one hour. If the policy expires, you can request a new presigned upload URL.  Related guide: [Custom Connector Plugin API](https://docs.confluent.io/cloud/current/connectors/connect-api-section.html).   ## The Presigned Urls Model <SchemaDefinition schemaRef=\"#/components/schemas/connect.v1.PresignedUrl\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**content_format** | **str** | Content format of the Custom Connector Plugin archive. | [optional] [readonly] 
**upload_id** | **str** | Unique identifier of this upload. | [optional] [readonly] 
**upload_url** | **str** | Upload URL for the Custom Connector Plugin archive. | [optional] [readonly] 
**upload_form_data** | **object** | Upload form data of the Custom Connector Plugin. All values should be strings. | [optional] [readonly] 

## Example

```python
from openapi_client.models.connect_v1_presigned_url import ConnectV1PresignedUrl

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1PresignedUrl from a JSON string
connect_v1_presigned_url_instance = ConnectV1PresignedUrl.from_json(json)
# print the JSON string representation of the object
print ConnectV1PresignedUrl.to_json()

# convert the object into a dict
connect_v1_presigned_url_dict = connect_v1_presigned_url_instance.to_dict()
# create an instance of ConnectV1PresignedUrl from a dict
connect_v1_presigned_url_form_dict = connect_v1_presigned_url.from_dict(connect_v1_presigned_url_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


