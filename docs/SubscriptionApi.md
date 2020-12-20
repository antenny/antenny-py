# antenny.SubscriptionApi

All URIs are relative to *https://api.antenny.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_subscription**](SubscriptionApi.md#cancel_subscription) | **PATCH** /subscriptions/{subId} | Cancels a subscription
[**create_subscription**](SubscriptionApi.md#create_subscription) | **POST** /subscriptions | Creates a subscription
[**get_subscription**](SubscriptionApi.md#get_subscription) | **GET** /subscriptions/{subId} | Gets a subscription
[**list_subscriptions**](SubscriptionApi.md#list_subscriptions) | **GET** /customers/{custId}/subscriptions | Gets a list of subscriptions


# **cancel_subscription**
> cancel_subscription(sub_id, inline_object)

Cancels a subscription

Cancels a subscription for a customer

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
    api_instance = antenny.SubscriptionApi(api_client)
    sub_id = 'sub_id_example' # str | Subscription id
inline_object = antenny.InlineObject() # InlineObject | 

    try:
        # Cancels a subscription
        api_instance.cancel_subscription(sub_id, inline_object)
    except ApiException as e:
        print("Exception when calling SubscriptionApi->cancel_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | [**str**](.md)| Subscription id | 
 **inline_object** | [**InlineObject**](InlineObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription**
> Subscription create_subscription(new_subscription)

Creates a subscription

Creates a new subscription

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
    api_instance = antenny.SubscriptionApi(api_client)
    new_subscription = antenny.NewSubscription() # NewSubscription | 

    try:
        # Creates a subscription
        api_response = api_instance.create_subscription(new_subscription)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_subscription** | [**NewSubscription**](NewSubscription.md)|  | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> Subscription get_subscription(sub_id)

Gets a subscription

Gets a subscription

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
    api_instance = antenny.SubscriptionApi(api_client)
    sub_id = 'sub_id_example' # str | Subscription id

    try:
        # Gets a subscription
        api_response = api_instance.get_subscription(sub_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionApi->get_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | [**str**](.md)| Subscription id | 

### Return type

[**Subscription**](Subscription.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subscriptions**
> SubscriptionList list_subscriptions(cust_id, sort=sort, limit=limit, start_key=start_key)

Gets a list of subscriptions

Lists subscriptions for a customer

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
    api_instance = antenny.SubscriptionApi(api_client)
    cust_id = 'cust_id_example' # str | Customer Id to get subscriptions
sort = 'sort_example' # str | Defines sort direction (optional)
limit = 56 # int | Limits the number of returned items (optional)
start_key = 'start_key_example' # str | Defines start of page of results (optional)

    try:
        # Gets a list of subscriptions
        api_response = api_instance.list_subscriptions(cust_id, sort=sort, limit=limit, start_key=start_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionApi->list_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cust_id** | [**str**](.md)| Customer Id to get subscriptions | 
 **sort** | **str**| Defines sort direction | [optional] 
 **limit** | **int**| Limits the number of returned items | [optional] 
 **start_key** | **str**| Defines start of page of results | [optional] 

### Return type

[**SubscriptionList**](SubscriptionList.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

