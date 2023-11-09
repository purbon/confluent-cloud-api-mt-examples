# PresignedUploadUrlConnectV1PresignedUrlRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**ConnectV1PresignedUrlRequestMetadata**](ConnectV1PresignedUrlRequestMetadata.md) |  | [optional] 
**content_format** | **str** | Archive format of the Custom Connector Plugin. | 

## Example

```python
from openapi_client.models.presigned_upload_url_connect_v1_presigned_url_request import PresignedUploadUrlConnectV1PresignedUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PresignedUploadUrlConnectV1PresignedUrlRequest from a JSON string
presigned_upload_url_connect_v1_presigned_url_request_instance = PresignedUploadUrlConnectV1PresignedUrlRequest.from_json(json)
# print the JSON string representation of the object
print PresignedUploadUrlConnectV1PresignedUrlRequest.to_json()

# convert the object into a dict
presigned_upload_url_connect_v1_presigned_url_request_dict = presigned_upload_url_connect_v1_presigned_url_request_instance.to_dict()
# create an instance of PresignedUploadUrlConnectV1PresignedUrlRequest from a dict
presigned_upload_url_connect_v1_presigned_url_request_form_dict = presigned_upload_url_connect_v1_presigned_url_request.from_dict(presigned_upload_url_connect_v1_presigned_url_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


