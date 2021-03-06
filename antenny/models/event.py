# coding: utf-8

"""
    Antenny API

    This is an api that allows you to interact with the Antenny platform. It allows you to manage your clients and subscriptions.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: admin@antenny.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from antenny.configuration import Configuration


class Event(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'subscription_id': 'str',
        'customer_id': 'str',
        'level': 'str',
        'message': 'str',
        'created': 'date',
        'modified': 'date'
    }

    attribute_map = {
        'id': 'id',
        'subscription_id': 'subscriptionId',
        'customer_id': 'customerId',
        'level': 'level',
        'message': 'message',
        'created': 'created',
        'modified': 'modified'
    }

    def __init__(self, id=None, subscription_id=None, customer_id=None, level=None, message=None, created=None, modified=None, local_vars_configuration=None):  # noqa: E501
        """Event - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._subscription_id = None
        self._customer_id = None
        self._level = None
        self._message = None
        self._created = None
        self._modified = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if customer_id is not None:
            self.customer_id = customer_id
        if level is not None:
            self.level = level
        if message is not None:
            self.message = message
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified

    @property
    def id(self):
        """Gets the id of this Event.  # noqa: E501


        :return: The id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Event.


        :param id: The id of this Event.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this Event.  # noqa: E501


        :return: The subscription_id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this Event.


        :param subscription_id: The subscription_id of this Event.  # noqa: E501
        :type subscription_id: str
        """

        self._subscription_id = subscription_id

    @property
    def customer_id(self):
        """Gets the customer_id of this Event.  # noqa: E501


        :return: The customer_id of this Event.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Event.


        :param customer_id: The customer_id of this Event.  # noqa: E501
        :type customer_id: str
        """

        self._customer_id = customer_id

    @property
    def level(self):
        """Gets the level of this Event.  # noqa: E501


        :return: The level of this Event.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this Event.


        :param level: The level of this Event.  # noqa: E501
        :type level: str
        """

        self._level = level

    @property
    def message(self):
        """Gets the message of this Event.  # noqa: E501


        :return: The message of this Event.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Event.


        :param message: The message of this Event.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def created(self):
        """Gets the created of this Event.  # noqa: E501


        :return: The created of this Event.  # noqa: E501
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Event.


        :param created: The created of this Event.  # noqa: E501
        :type created: date
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this Event.  # noqa: E501


        :return: The modified of this Event.  # noqa: E501
        :rtype: date
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Event.


        :param modified: The modified of this Event.  # noqa: E501
        :type modified: date
        """

        self._modified = modified

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Event):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Event):
            return True

        return self.to_dict() != other.to_dict()
