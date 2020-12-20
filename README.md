# antenny-py
This is an api that allows you to interact with the Antenny platform. It allows you to manage your clients and subscriptions.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://antenny.io](https://antenny.io)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import antenny
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import antenny
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.antenny.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ClientApi* | [**create_client**](docs/ClientApi.md#create_client) | **POST** /clients | Creates a client
*ClientApi* | [**delete_client**](docs/ClientApi.md#delete_client) | **DELETE** /clients/{clientId} | Deletes a client
*ClientApi* | [**get_client**](docs/ClientApi.md#get_client) | **GET** /clients/{clientId} | Gets a client
*ClientApi* | [**list_clients**](docs/ClientApi.md#list_clients) | **GET** /customers/{custId}/clients | Gets a list of clients
*EventsApi* | [**list_events**](docs/EventsApi.md#list_events) | **GET** /subscriptions/{subId}/events | Gets a list of events for a subscription
*RegistrationApi* | [**get_registration**](docs/RegistrationApi.md#get_registration) | **GET** /customers/{custId}/registration | Gets a customers registration
*SubscriptionApi* | [**cancel_subscription**](docs/SubscriptionApi.md#cancel_subscription) | **PATCH** /subscriptions/{subId} | Cancels a subscription
*SubscriptionApi* | [**create_subscription**](docs/SubscriptionApi.md#create_subscription) | **POST** /subscriptions | Creates a subscription
*SubscriptionApi* | [**get_subscription**](docs/SubscriptionApi.md#get_subscription) | **GET** /subscriptions/{subId} | Gets a subscription
*SubscriptionApi* | [**list_subscriptions**](docs/SubscriptionApi.md#list_subscriptions) | **GET** /customers/{custId}/subscriptions | Gets a list of subscriptions


## Documentation For Models

 - [Client](docs/Client.md)
 - [ClientList](docs/ClientList.md)
 - [Endpoint](docs/Endpoint.md)
 - [Event](docs/Event.md)
 - [EventList](docs/EventList.md)
 - [InlineObject](docs/InlineObject.md)
 - [NewClient](docs/NewClient.md)
 - [NewSubscription](docs/NewSubscription.md)
 - [Registration](docs/Registration.md)
 - [Resource](docs/Resource.md)
 - [Subscription](docs/Subscription.md)
 - [SubscriptionList](docs/SubscriptionList.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header


## Author

admin@antenny.io


