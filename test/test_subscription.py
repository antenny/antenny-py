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
from antenny.models.subscription import Subscription  # noqa: E501
from antenny.rest import ApiException

class TestSubscription(unittest.TestCase):
    """Subscription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Subscription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = antenny.models.subscription.Subscription()  # noqa: E501
        if include_optional :
            return Subscription(
                id = '0', 
                name = '012', 
                resource = antenny.models.resource.Resource(
                    protocol = 'ws', 
                    url = '0', ), 
                endpoint = antenny.models.endpoint.Endpoint(
                    protocol = 'http', 
                    url = '0', ), 
                status = 'PENDING', 
                created = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                modified = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else :
            return Subscription(
        )

    def testSubscription(self):
        """Test Subscription"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()