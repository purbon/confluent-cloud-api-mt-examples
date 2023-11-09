# DeleteKafkaAcls200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AclData]**](AclData.md) |  | 

## Example

```python
from openapi_client.models.delete_kafka_acls200_response import DeleteKafkaAcls200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteKafkaAcls200Response from a JSON string
delete_kafka_acls200_response_instance = DeleteKafkaAcls200Response.from_json(json)
# print the JSON string representation of the object
print DeleteKafkaAcls200Response.to_json()

# convert the object into a dict
delete_kafka_acls200_response_dict = delete_kafka_acls200_response_instance.to_dict()
# create an instance of DeleteKafkaAcls200Response from a dict
delete_kafka_acls200_response_form_dict = delete_kafka_acls200_response.from_dict(delete_kafka_acls200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


