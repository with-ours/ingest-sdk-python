# TrackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** | The name of the event you&#39;re tracking. This must be whitelisted in the Ours dashboard. | 
**token** | **str** | The token for your Ours Privacy Source. You can find this in the Ours dashboard. | 
**user_id** | **str** | The Ours user id stored in local storage and cookies on your web properties. If userId is included in the request, we do not lookup the user by email or externalId. | [optional] 
**external_id** | **str** | The externalId (the ID in your system) of a user. We will associate this event with the user or create a user. If included in the request, email lookup is ignored. | [optional] 
**email** | **str** | The email address of a user. We will associate this event with the user or create a user. Used for lookup if externalId and userId are not included in the request. | [optional] 
**event_properties** | **Dict[str, Optional[object]]** | Any additional event properties you want to pass along. | [optional] 
**user_properties** | [**TrackRequestUserProperties**](TrackRequestUserProperties.md) |  | [optional] 
**default_properties** | [**TrackRequestDefaultProperties**](TrackRequestDefaultProperties.md) |  | [optional] 
**distinct_id** | **str** | A unique identifier for the event. This helps prevent duplicate events. | [optional] 

## Example

```python
from oursprivacy_client.models.track_request import TrackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackRequest from a JSON string
track_request_instance = TrackRequest.from_json(json)
# print the JSON string representation of the object
print(TrackRequest.to_json())

# convert the object into a dict
track_request_dict = track_request_instance.to_dict()
# create an instance of TrackRequest from a dict
track_request_from_dict = TrackRequest.from_dict(track_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


