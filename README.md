# antenny-py

antenny - Python client for [antenny](https://antenny.io). This is an api that allows you to interact with Antenny. It allows you to manage your clients and subscriptions.
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project.

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install antenny-py
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import antenny
from antenny.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = antenny.Configuration(
    host = "https://api.antenny.io",
    api_key = {
        'ApiKeyAuth': 'YOUR_API_KEY'
    }
)

# Enter a context with an instance of the API client
with antenny.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = antenny.SubscriptionApi(api_client)
    new_subscription = antenny.NewSubscription(
        name = 'test-subscription',
        customer_id = 'customerId',
        region = 'aws-region',
        resource = antenny.Resource(
            protocol = 'ws',
            url = 'wss://example.com'
        ),
        endpoint = antenny.Endpoint(
            protocol = 'http',
            url = 'http://example.com'
        )
    )

    try:
        # Creates a subscription
        api_response = api_instance.create_subscription(new_subscription)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubscriptionApi->create_subscription: %s\n" % e)
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
