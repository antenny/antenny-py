# antenny.ClientApi

All URIs are relative to *https://api.antenny.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client**](ClientApi.md#create_client) | **POST** /clients | Creates a client
[**delete_client**](ClientApi.md#delete_client) | **DELETE** /clients/{clientId} | Deletes a client
[**get_client**](ClientApi.md#get_client) | **GET** /clients/{clientId} | Gets a client
[**list_clients**](ClientApi.md#list_clients) | **GET** /customers/{custId}/clients | Gets a list of clients


# **create_client**
> Client create_client(new_client)

Creates a client

Creates a new client

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
    api_instance = antenny.ClientApi(api_client)
    new_client = antenny.NewClient() # NewClient | 

    try:
        # Creates a client
        api_response = api_instance.create_client(new_client)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientApi->create_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_client** | [**NewClient**](NewClient.md)|  | 

### Return type

[**Client**](Client.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client**
> delete_client(client_id)

Deletes a client

Deletes a client

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
    api_instance = antenny.ClientApi(api_client)
    client_id = 'client_id_example' # str | Client Id to get

    try:
        # Deletes a client
        api_instance.delete_client(client_id)
    except ApiException as e:
        print("Exception when calling ClientApi->delete_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | [**str**](.md)| Client Id to get | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful operation |  -  |
**401** | Unauthorized operation |  -  |
**403** | Forbidden operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client**
> Client get_client(client_id)

Gets a client

Gets a client for a customer

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
    api_instance = antenny.ClientApi(api_client)
    client_id = 'client_id_example' # str | Client Id to get

    try:
        # Gets a client
        api_response = api_instance.get_client(client_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientApi->get_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | [**str**](.md)| Client Id to get | 

### Return type

[**Client**](Client.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Reqeuest |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clients**
> ClientList list_clients(cust_id, sort=sort, limit=limit, start_key=start_key)

Gets a list of clients

List of clients for a customer

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
    api_instance = antenny.ClientApi(api_client)
    cust_id = 'cust_id_example' # str | Customer Id to get clients for
sort = 'sort_example' # str | Defines sort direction (optional)
limit = 56 # int | Limits the number of returned items (optional)
start_key = 'start_key_example' # str | Defines start of page of results (optional)

    try:
        # Gets a list of clients
        api_response = api_instance.list_clients(cust_id, sort=sort, limit=limit, start_key=start_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClientApi->list_clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cust_id** | [**str**](.md)| Customer Id to get clients for | 
 **sort** | **str**| Defines sort direction | [optional] 
 **limit** | **int**| Limits the number of returned items | [optional] 
 **start_key** | **str**| Defines start of page of results | [optional] 

### Return type

[**ClientList**](ClientList.md)

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

