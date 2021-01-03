# coding: utf-8

# flake8: noqa

"""
    Antenny API

    This is an api that allows you to interact with the Antenny platform. It allows you to manage your clients and subscriptions.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: admin@antenny.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.2.0"

# import apis into sdk package
from antenny.api.client_api import ClientApi
from antenny.api.events_api import EventsApi
from antenny.api.registration_api import RegistrationApi
from antenny.api.subscription_api import SubscriptionApi

# import ApiClient
from antenny.api_client import ApiClient
from antenny.configuration import Configuration
from antenny.exceptions import OpenApiException
from antenny.exceptions import ApiTypeError
from antenny.exceptions import ApiValueError
from antenny.exceptions import ApiKeyError
from antenny.exceptions import ApiAttributeError
from antenny.exceptions import ApiException
# import models into sdk package
from antenny.models.client import Client
from antenny.models.client_list import ClientList
from antenny.models.endpoint import Endpoint
from antenny.models.event import Event
from antenny.models.event_list import EventList
from antenny.models.header import Header
from antenny.models.inline_object import InlineObject
from antenny.models.message import Message
from antenny.models.new_client import NewClient
from antenny.models.new_subscription import NewSubscription
from antenny.models.registration import Registration
from antenny.models.resource import Resource
from antenny.models.subscription import Subscription
from antenny.models.subscription_list import SubscriptionList

