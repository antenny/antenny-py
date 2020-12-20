# antenny.EventsApi

All URIs are relative to *https://api.antenny.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_events**](EventsApi.md#list_events) | **GET** /subscriptions/{subId}/events | Gets a list of events for a subscription


# **list_events**
> EventList list_events(sub_id, sort=sort, level=level, limit=limit, start_key=start_key)

Gets a list of events for a subscription

Lists events for a subscription

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import antenny
from antenny.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.antenny.io
# See configuration.py for a list of all supported configuration parameters.
configuration = antenny.Configuration(
    host = "https://api.antenny.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration = antenny.Configuration(
    host = "https://api.antenny.io",
    api_key = {
        'ApiKeyAuth': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with antenny.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = antenny.EventsApi(api_client)
    sub_id = 'sub_id_example' # str | Subscription id
sort = 'sort_example' # str | Defines sort direction (optional)
level = 'level_example' # str | Filters events by level (optional)
limit = 56 # int | Limits the number of returned items (optional)
start_key = 'start_key_example' # str | Defines start of page of results (optional)

    try:
        # Gets a list of events for a subscription
        api_response = api_instance.list_events(sub_id, sort=sort, level=level, limit=limit, start_key=start_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventsApi->list_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | [**str**](.md)| Subscription id | 
 **sort** | **str**| Defines sort direction | [optional] 
 **level** | **str**| Filters events by level | [optional] 
 **limit** | **int**| Limits the number of returned items | [optional] 
 **start_key** | **str**| Defines start of page of results | [optional] 

### Return type

[**EventList**](EventList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

