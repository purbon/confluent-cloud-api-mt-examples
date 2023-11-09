# MirrorLag


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partition** | **int** |  | 
**lag** | **int** |  | 
**last_source_fetch_offset** | **int** |  | 

## Example

```python
from openapi_client.models.mirror_lag import MirrorLag

# TODO update the JSON string below
json = "{}"
# create an instance of MirrorLag from a JSON string
mirror_lag_instance = MirrorLag.from_json(json)
# print the JSON string representation of the object
print MirrorLag.to_json()

# convert the object into a dict
mirror_lag_dict = mirror_lag_instance.to_dict()
# create an instance of MirrorLag from a dict
mirror_lag_form_dict = mirror_lag.from_dict(mirror_lag_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


