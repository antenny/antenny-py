# coding: utf-8

"""
    Antenny API

    This is an api that allows you to interact with the Antenny platform. It allows you to manage your clients and subscriptions.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: admin@antenny.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from antenny.api_client import ApiClient
from antenny.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class EventsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_events(self, sub_id, **kwargs):  # noqa: E501
        """Gets a list of events for a subscription  # noqa: E501

        Lists events for a subscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_events(sub_id, async_req=True)
        >>> result = thread.get()

        :param sub_id: Subscription id (required)
        :type sub_id: str
        :param sort: Defines sort direction
        :type sort: str
        :param level: Filters events by level
        :type level: str
        :param limit: Limits the number of returned items
        :type limit: int
        :param start_key: Defines start of page of results
        :type start_key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: EventList
        """
        kwargs['_return_http_data_only'] = True
        return self.list_events_with_http_info(sub_id, **kwargs)  # noqa: E501

    def list_events_with_http_info(self, sub_id, **kwargs):  # noqa: E501
        """Gets a list of events for a subscription  # noqa: E501

        Lists events for a subscription  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_events_with_http_info(sub_id, async_req=True)
        >>> result = thread.get()

        :param sub_id: Subscription id (required)
        :type sub_id: str
        :param sort: Defines sort direction
        :type sort: str
        :param level: Filters events by level
        :type level: str
        :param limit: Limits the number of returned items
        :type limit: int
        :param start_key: Defines start of page of results
        :type start_key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(EventList, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'sub_id',
            'sort',
            'level',
            'limit',
            'start_key'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_events" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'sub_id' is set
        if self.api_client.client_side_validation and ('sub_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['sub_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sub_id` when calling `list_events`")  # noqa: E501

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 50:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_events`, must be a value less than or equal to `50`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_events`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'sub_id' in local_var_params:
            path_params['subId'] = local_var_params['sub_id']  # noqa: E501

        query_params = []
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'level' in local_var_params and local_var_params['level'] is not None:  # noqa: E501
            query_params.append(('level', local_var_params['level']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'start_key' in local_var_params and local_var_params['start_key'] is not None:  # noqa: E501
            query_params.append(('startKey', local_var_params['start_key']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/subscriptions/{subId}/events', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EventList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))