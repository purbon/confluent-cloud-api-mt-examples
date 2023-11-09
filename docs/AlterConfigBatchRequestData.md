# AlterConfigBatchRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AlterConfigBatchRequestDataDataInner]**](AlterConfigBatchRequestDataDataInner.md) |  | 
**validate_only** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.alter_config_batch_request_data import AlterConfigBatchRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of AlterConfigBatchRequestData from a JSON string
alter_config_batch_request_data_instance = AlterConfigBatchRequestData.from_json(json)
# print the JSON string representation of the object
print AlterConfigBatchRequestData.to_json()

# convert the object into a dict
alter_config_batch_request_data_dict = alter_config_batch_request_data_instance.to_dict()
# create an instance of AlterConfigBatchRequestData from a dict
alter_config_batch_request_data_form_dict = alter_config_batch_request_data.from_dict(alter_config_batch_request_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


