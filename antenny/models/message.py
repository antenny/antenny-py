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


class Message(object):
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
        'format': 'str',
        'content': 'str'
    }

    attribute_map = {
        'format': 'format',
        'content': 'content'
    }

    def __init__(self, format=None, content=None, local_vars_configuration=None):  # noqa: E501
        """Message - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._format = None
        self._content = None
        self.discriminator = None

        self.format = format
        self.content = content

    @property
    def format(self):
        """Gets the format of this Message.  # noqa: E501


        :return: The format of this Message.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Message.


        :param format: The format of this Message.  # noqa: E501
        :type format: str
        """
        if self.local_vars_configuration.client_side_validation and format is None:  # noqa: E501
            raise ValueError("Invalid value for `format`, must not be `None`")  # noqa: E501
        allowed_values = ["text", "binary"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and format not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def content(self):
        """Gets the content of this Message.  # noqa: E501


        :return: The content of this Message.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Message.


        :param content: The content of this Message.  # noqa: E501
        :type content: str
        """
        if self.local_vars_configuration.client_side_validation and content is None:  # noqa: E501
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

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
        if not isinstance(other, Message):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Message):
            return True

        return self.to_dict() != other.to_dict()
