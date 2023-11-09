# CreateLinkRequestData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_cluster_id** | **str** |  | [optional] 
**destination_cluster_id** | **str** |  | [optional] 
**remote_cluster_id** | **str** | The expected remote cluster ID. | [optional] 
**cluster_link_id** | **str** | The expected cluster link ID. Can be provided when creating the second side of a bidirectional link for validating the link ID is as expected. If it&#39;s not provided, it&#39;s inferred from the remote cluster. | [optional] 
**configs** | [**List[ConfigData]**](ConfigData.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_link_request_data import CreateLinkRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLinkRequestData from a JSON string
create_link_request_data_instance = CreateLinkRequestData.from_json(json)
# print the JSON string representation of the object
print CreateLinkRequestData.to_json()

# convert the object into a dict
create_link_request_data_dict = create_link_request_data_instance.to_dict()
# create an instance of CreateLinkRequestData from a dict
create_link_request_data_form_dict = create_link_request_data.from_dict(create_link_request_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


