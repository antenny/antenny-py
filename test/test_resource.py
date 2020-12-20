# coding: utf-8

"""
    Antenny API

    This is an api that allows you to interact with the Antenny platform. It allows you to manage your clients and subscriptions.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: admin@antenny.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import antenny
from antenny.models.resource import Resource  # noqa: E501
from antenny.rest import ApiException

class TestResource(unittest.TestCase):
    """Resource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Resource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = antenny.models.resource.Resource()  # noqa: E501
        if include_optional :
            return Resource(
                protocol = 'ws', 
                url = '0'
            )
        else :
            return Resource(
                protocol = 'ws',
                url = '0',
        )

    def testResource(self):
        """Test Resource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()