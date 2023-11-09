# PresignedUploadUrlConnectV1PresignedUrl200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**content_format** | **str** | Content format of the Custom Connector Plugin archive. | [optional] [readonly] 
**upload_id** | **str** | Unique identifier of this upload. | [optional] [readonly] 
**upload_url** | **str** | Upload URL for the Custom Connector Plugin archive. | [optional] [readonly] 
**upload_form_data** | **object** | Upload form data of the Custom Connector Plugin. All values should be strings. | [optional] [readonly] 

## Example

```python
from openapi_client.models.presigned_upload_url_connect_v1_presigned_url200_response import PresignedUploadUrlConnectV1PresignedUrl200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PresignedUploadUrlConnectV1PresignedUrl200Response from a JSON string
presigned_upload_url_connect_v1_presigned_url200_response_instance = PresignedUploadUrlConnectV1PresignedUrl200Response.from_json(json)
# print the JSON string representation of the object
print PresignedUploadUrlConnectV1PresignedUrl200Response.to_json()

# convert the object into a dict
presigned_upload_url_connect_v1_presigned_url200_response_dict = presigned_upload_url_connect_v1_presigned_url200_response_instance.to_dict()
# create an instance of PresignedUploadUrlConnectV1PresignedUrl200Response from a dict
presigned_upload_url_connect_v1_presigned_url200_response_form_dict = presigned_upload_url_connect_v1_presigned_url200_response.from_dict(presigned_upload_url_connect_v1_presigned_url200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


