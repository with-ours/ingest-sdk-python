# oursprivacy_client.OursPrivacyApi

All URIs are relative to *https://api.oursprivacy.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**identify**](OursPrivacyApi.md#identify) | **POST** /identify | Identify Visitors
[**track**](OursPrivacyApi.md#track) | **POST** /track | Track Events


# **identify**
> Track200Response identify(identify_request)

Identify Visitors

Define visitor properties on an existing visitor or create a new visitor. Note: This does not fire an event. If you want to fire an event, use the track method and include properties for the visitor.

### Example


```python
import oursprivacy_client
from oursprivacy_client.models.identify_request import IdentifyRequest
from oursprivacy_client.models.track200_response import Track200Response
from oursprivacy_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.oursprivacy.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = oursprivacy_client.Configuration(
    host = "https://api.oursprivacy.com/api/v1"
)


# Enter a context with an instance of the API client
with oursprivacy_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oursprivacy_client.OursPrivacyApi(api_client)
    identify_request = oursprivacy_client.IdentifyRequest() # IdentifyRequest | The payload to identify a visitor

    try:
        # Identify Visitors
        api_response = api_instance.identify(identify_request)
        print("The response of OursPrivacyApi->identify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OursPrivacyApi->identify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identify_request** | [**IdentifyRequest**](IdentifyRequest.md)| The payload to identify a visitor | 

### Return type

[**Track200Response**](Track200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - your event was sent to our servers |  -  |
**400** | Bad Request - Something about the body of your request is invalid. Please update your payload and try again. |  -  |
**401** | Unauthorized - you are not authorized to send events to Ours. Please contact support. |  -  |
**429** | Too Many Requests - We recommend starting with a backoff of 2s and doubling backoff until 60s, with 1-5s of jitter. |  -  |
**500** | Internal Server Error - in the unlikely event that you see this error, please backoff as described for a 429 response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track**
> Track200Response track(track_request)

Track Events

Track events from your server. Please include at least one of: userId, externalId, or email. These properties help us associate events with existing users. For all fields, null values unset the property and undefined values do not unset existing properties.

### Example


```python
import oursprivacy_client
from oursprivacy_client.models.track200_response import Track200Response
from oursprivacy_client.models.track_request import TrackRequest
from oursprivacy_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.oursprivacy.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = oursprivacy_client.Configuration(
    host = "https://api.oursprivacy.com/api/v1"
)


# Enter a context with an instance of the API client
with oursprivacy_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = oursprivacy_client.OursPrivacyApi(api_client)
    track_request = oursprivacy_client.TrackRequest() # TrackRequest | The payload to track an event

    try:
        # Track Events
        api_response = api_instance.track(track_request)
        print("The response of OursPrivacyApi->track:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OursPrivacyApi->track: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **track_request** | [**TrackRequest**](TrackRequest.md)| The payload to track an event | 

### Return type

[**Track200Response**](Track200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success - your event was sent to our servers |  -  |
**400** | Bad Request - Something about the body of your request is invalid. Please update your payload and try again. |  -  |
**401** | Unauthorized - you are not authorized to send events to Ours. Please contact support. |  -  |
**429** | Too Many Requests - We recommend starting with a backoff of 2s and doubling backoff until 60s, with 1-5s of jitter. |  -  |
**500** | Internal Server Error - in the unlikely event that you see this error, please backoff as described for a 429 response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

