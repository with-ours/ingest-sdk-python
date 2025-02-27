# IdentifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The token for your Ours Privacy Source. You can find this in the Ours dashboard. | 
**user_id** | **str** | The Ours user id stored in local storage and cookies on your web properties. If userId is included in the request, we do not lookup the user by email or externalId. | 
**user_properties** | [**IdentifyRequestUserProperties**](IdentifyRequestUserProperties.md) |  | 
**default_properties** | [**TrackRequestDefaultProperties**](TrackRequestDefaultProperties.md) |  | [optional] 

## Example

```python
from oursprivacy_client.models.identify_request import IdentifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IdentifyRequest from a JSON string
identify_request_instance = IdentifyRequest.from_json(json)
# print the JSON string representation of the object
print(IdentifyRequest.to_json())

# convert the object into a dict
identify_request_dict = identify_request_instance.to_dict()
# create an instance of IdentifyRequest from a dict
identify_request_from_dict = IdentifyRequest.from_dict(identify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


