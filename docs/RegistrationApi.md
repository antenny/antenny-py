# antenny.RegistrationApi

All URIs are relative to *https://api.antenny.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_registration**](RegistrationApi.md#get_registration) | **GET** /customers/{custId}/registration | Gets a customers registration


# **get_registration**
> Registration get_registration(cust_id)

Gets a customers registration

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
    api_instance = antenny.RegistrationApi(api_client)
    cust_id = 'cust_id_example' # str | Customer Id for registration

    try:
        # Gets a customers registration
        api_response = api_instance.get_registration(cust_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RegistrationApi->get_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cust_id** | **str**| Customer Id for registration | 

### Return type

[**Registration**](Registration.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthorized operation |  -  |
**403** | Forbidden operation |  -  |
**404** | Registration not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

