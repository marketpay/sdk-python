# coding: utf-8

"""
    MarketPay API

    API for Smart Contracts and Payments

    OpenAPI spec version: v2.01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class TransfersApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def transfers_get(self, transfer_id, **kwargs):
        """
        View a Transfer
        A Transfer is a request to relocate e-money from one wallet to another wallet.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.transfers_get(transfer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int transfer_id: The Id of a transfer (required)
        :return: TransferResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.transfers_get_with_http_info(transfer_id, **kwargs)
        else:
            (data) = self.transfers_get_with_http_info(transfer_id, **kwargs)
            return data

    def transfers_get_with_http_info(self, transfer_id, **kwargs):
        """
        View a Transfer
        A Transfer is a request to relocate e-money from one wallet to another wallet.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.transfers_get_with_http_info(transfer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int transfer_id: The Id of a transfer (required)
        :return: TransferResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transfer_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transfers_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'transfer_id' is set
        if ('transfer_id' not in params) or (params['transfer_id'] is None):
            raise ValueError("Missing the required parameter `transfer_id` when calling `transfers_get`")


        collection_formats = {}

        resource_path = '/v2.01/Transfers/{TransferId}'.replace('{format}', 'json')
        path_params = {}
        if 'transfer_id' in params:
            path_params['TransferId'] = params['transfer_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain', 'application/json', 'text/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TransferResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def transfers_post(self, **kwargs):
        """
        Create a Transfer
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.transfers_post(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TransferPost transfer: Transfer Object params
        :return: TransferResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.transfers_post_with_http_info(**kwargs)
        else:
            (data) = self.transfers_post_with_http_info(**kwargs)
            return data

    def transfers_post_with_http_info(self, **kwargs):
        """
        Create a Transfer
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.transfers_post_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param TransferPost transfer: Transfer Object params
        :return: TransferResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['transfer']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transfers_post" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/v2.01/Transfers'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transfer' in params:
            body_params = params['transfer']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain', 'application/json', 'text/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/json-patch+json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TransferResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)