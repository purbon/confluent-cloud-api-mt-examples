# ConnectV1UploadSourcePresignedUrl

Presigned URL of the uploaded Custom Connector Plugin archive.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | Location of the Custom Connector Plugin source.  | 
**upload_id** | **str** | Upload ID returned by the &#x60;/presigned-upload-url&#x60; API. This field returns an empty string in all responses. | 

## Example

```python
from openapi_client.models.connect_v1_upload_source_presigned_url import ConnectV1UploadSourcePresignedUrl

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectV1UploadSourcePresignedUrl from a JSON string
connect_v1_upload_source_presigned_url_instance = ConnectV1UploadSourcePresignedUrl.from_json(json)
# print the JSON string representation of the object
print ConnectV1UploadSourcePresignedUrl.to_json()

# convert the object into a dict
connect_v1_upload_source_presigned_url_dict = connect_v1_upload_source_presigned_url_instance.to_dict()
# create an instance of ConnectV1UploadSourcePresignedUrl from a dict
connect_v1_upload_source_presigned_url_form_dict = connect_v1_upload_source_presigned_url.from_dict(connect_v1_upload_source_presigned_url_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


