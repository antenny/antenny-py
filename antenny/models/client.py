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


class Client(object):
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
        'name': 'str',
        'api_key': 'str',
        'created': 'date',
        'modified': 'date'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'api_key': 'apiKey',
        'created': 'created',
        'modified': 'modified'
    }

    def __init__(self, id=None, name=None, api_key=None, created=None, modified=None, local_vars_configuration=None):  # noqa: E501
        """Client - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._api_key = None
        self._created = None
        self._modified = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if api_key is not None:
            self.api_key = api_key
        if created is not None:
            self.created = created
        if modified is not None:
            self.modified = modified

    @property
    def id(self):
        """Gets the id of this Client.  # noqa: E501


        :return: The id of this Client.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Client.


        :param id: The id of this Client.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Client.  # noqa: E501


        :return: The name of this Client.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Client.


        :param name: The name of this Client.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 32):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 3):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")  # noqa: E501

        self._name = name

    @property
    def api_key(self):
        """Gets the api_key of this Client.  # noqa: E501


        :return: The api_key of this Client.  # noqa: E501
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this Client.


        :param api_key: The api_key of this Client.  # noqa: E501
        :type api_key: str
        """

        self._api_key = api_key

    @property
    def created(self):
        """Gets the created of this Client.  # noqa: E501


        :return: The created of this Client.  # noqa: E501
        :rtype: date
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Client.


        :param created: The created of this Client.  # noqa: E501
        :type created: date
        """

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this Client.  # noqa: E501


        :return: The modified of this Client.  # noqa: E501
        :rtype: date
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Client.


        :param modified: The modified of this Client.  # noqa: E501
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
        if not isinstance(other, Client):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Client):
            return True

        return self.to_dict() != other.to_dict()
