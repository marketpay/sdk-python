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


class PayInsUniversalPayApi(object):
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

    def pay_ins_universal_pay_get_universal_pay_tokenization(self, token_id, **kwargs):
        """
        View a UniversalPay card tokenization status
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.pay_ins_universal_pay_get_universal_pay_tokenization(token_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int token_id: The Id of a tokenization (required)
        :return: UniversalPayTokenizationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.pay_ins_universal_pay_get_universal_pay_tokenization_with_http_info(token_id, **kwargs)
        else:
            (data) = self.pay_ins_universal_pay_get_universal_pay_tokenization_with_http_info(token_id, **kwargs)
            return data

    def pay_ins_universal_pay_get_universal_pay_tokenization_with_http_info(self, token_id, **kwargs):
        """
        View a UniversalPay card tokenization status
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.pay_ins_universal_pay_get_universal_pay_tokenization_with_http_info(token_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int token_id: The Id of a tokenization (required)
        :return: UniversalPayTokenizationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pay_ins_universal_pay_get_universal_pay_tokenization" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token_id' is set
        if ('token_id' not in params) or (params['token_id'] is None):
            raise ValueError("Missing the required parameter `token_id` when calling `pay_ins_universal_pay_get_universal_pay_tokenization`")


        collection_formats = {}

        path_params = {}
        if 'token_id' in params:
            path_params['TokenId'] = params['token_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain', 'application/json', 'text/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api('/v2.01/PayInsUniversalPay/token/{TokenId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UniversalPayTokenizationResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def pay_ins_universal_pay_universal_pay_get_payment(self, pay_in_id, **kwargs):
        """
        View a UniversalPay payment
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.pay_ins_universal_pay_universal_pay_get_payment(pay_in_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int pay_in_id: The Id of a payment (required)
        :return: UniversalPayPayInsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.pay_ins_universal_pay_universal_pay_get_payment_with_http_info(pay_in_id, **kwargs)
        else:
            (data) = self.pay_ins_universal_pay_universal_pay_get_payment_with_http_info(pay_in_id, **kwargs)
            return data

    def pay_ins_universal_pay_universal_pay_get_payment_with_http_info(self, pay_in_id, **kwargs):
        """
        View a UniversalPay payment
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.pay_ins_universal_pay_universal_pay_get_payment_with_http_info(pay_in_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int pay_in_id: The Id of a payment (required)
        :return: UniversalPayPayInsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pay_in_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pay_ins_universal_pay_universal_pay_get_payment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pay_in_id' is set
        if ('pay_in_id' not in params) or (params['pay_in_id'] is None):
            raise ValueError("Missing the required parameter `pay_in_id` when calling `pay_ins_universal_pay_universal_pay_get_payment`")


        collection_formats = {}

        path_params = {}
        if 'pay_in_id' in params:
            path_params['PayInId'] = params['pay_in_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain', 'application/json', 'text/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api('/v2.01/PayInsUniversalPay/payments/{PayInId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UniversalPayPayInsResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def pay_ins_universal_pay_universal_pay_post_payment_by_web(self, **kwargs):
        """
        Create a UniversalPay PayIn Request
        Prepares a payment on UniversalPay. The data returned is used to show the UniversalPay interface to the user.  Once the payment is done, the user will be redirected to one of UrlOk or UrlKo passed parameters.  In order to redirect the user, a Post request with Content-Type of application/x-www-form-urlencoded must be executed from the user's browser.  Below there is an example of a request where the params surrounded by curly braces have to be replaced with the response's params.  curl -X POST -H \"Content-Type: application/x-www-form-urlencoded\" -H \"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\" -H \"Cache-Control: no-cache\" -d 'Ds_SignatureVersion={Ds_SignatureVersion}&amp;Ds_MerchantParameters={Ds_MerchantParameters}&amp;Ds_Signature={Ds_Signature}' \"{Url}\"
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.pay_ins_universal_pay_universal_pay_post_payment_by_web(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UniversalPayPayByWebPost universal_pay_pay_in: UniversalPay PayIn Request Object params
        :return: UniversalPayPayByWebResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.pay_ins_universal_pay_universal_pay_post_payment_by_web_with_http_info(**kwargs)
        else:
            (data) = self.pay_ins_universal_pay_universal_pay_post_payment_by_web_with_http_info(**kwargs)
            return data

    def pay_ins_universal_pay_universal_pay_post_payment_by_web_with_http_info(self, **kwargs):
        """
        Create a UniversalPay PayIn Request
        Prepares a payment on UniversalPay. The data returned is used to show the UniversalPay interface to the user.  Once the payment is done, the user will be redirected to one of UrlOk or UrlKo passed parameters.  In order to redirect the user, a Post request with Content-Type of application/x-www-form-urlencoded must be executed from the user's browser.  Below there is an example of a request where the params surrounded by curly braces have to be replaced with the response's params.  curl -X POST -H \"Content-Type: application/x-www-form-urlencoded\" -H \"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\" -H \"Cache-Control: no-cache\" -d 'Ds_SignatureVersion={Ds_SignatureVersion}&amp;Ds_MerchantParameters={Ds_MerchantParameters}&amp;Ds_Signature={Ds_Signature}' \"{Url}\"
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.pay_ins_universal_pay_universal_pay_post_payment_by_web_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UniversalPayPayByWebPost universal_pay_pay_in: UniversalPay PayIn Request Object params
        :return: UniversalPayPayByWebResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['universal_pay_pay_in']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pay_ins_universal_pay_universal_pay_post_payment_by_web" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'universal_pay_pay_in' in params:
            body_params = params['universal_pay_pay_in']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain', 'application/json', 'text/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/json-patch+json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api('/v2.01/PayInsUniversalPay/payments/web', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UniversalPayPayByWebResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def pay_ins_universal_pay_universal_pay_post_refund(self, pay_in_id, **kwargs):
        """
        Create a UniversalPay Payment Refund
        A PayIn Refund is a request to reimburse a user on their payment card. The money which has already been paid will automatically go back to the user’s bank account.              Minimum amount to refund is 1€.              If you're doing a partial Refund, note that you can only refund the same amount on the same transaction once per day (this is to prevent unintended duplicate refunds). After 24h you can do another refund of the same amount on the same transaction. If it is a different amount on the same transaction, there is not this limit.              If you do not specify DebitedFunds and Fees parameters, it will automatically fully refund the PayIn. However if you do provide one or the other, you must provide both. Note that Fees must be negative if you wish to refund them - adding a positive value for the Fees is a way to charge your customers for the Refund (in the same way you might for a PayIn, Transfer or any other Transaction
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.pay_ins_universal_pay_universal_pay_post_refund(pay_in_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int pay_in_id: The Id of a PayIn (required)
        :param UniversalPayRefundPost universal_pay_refund: Refund Object params
        :return: UniversalPayRefundResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.pay_ins_universal_pay_universal_pay_post_refund_with_http_info(pay_in_id, **kwargs)
        else:
            (data) = self.pay_ins_universal_pay_universal_pay_post_refund_with_http_info(pay_in_id, **kwargs)
            return data

    def pay_ins_universal_pay_universal_pay_post_refund_with_http_info(self, pay_in_id, **kwargs):
        """
        Create a UniversalPay Payment Refund
        A PayIn Refund is a request to reimburse a user on their payment card. The money which has already been paid will automatically go back to the user’s bank account.              Minimum amount to refund is 1€.              If you're doing a partial Refund, note that you can only refund the same amount on the same transaction once per day (this is to prevent unintended duplicate refunds). After 24h you can do another refund of the same amount on the same transaction. If it is a different amount on the same transaction, there is not this limit.              If you do not specify DebitedFunds and Fees parameters, it will automatically fully refund the PayIn. However if you do provide one or the other, you must provide both. Note that Fees must be negative if you wish to refund them - adding a positive value for the Fees is a way to charge your customers for the Refund (in the same way you might for a PayIn, Transfer or any other Transaction
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.pay_ins_universal_pay_universal_pay_post_refund_with_http_info(pay_in_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int pay_in_id: The Id of a PayIn (required)
        :param UniversalPayRefundPost universal_pay_refund: Refund Object params
        :return: UniversalPayRefundResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pay_in_id', 'universal_pay_refund']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pay_ins_universal_pay_universal_pay_post_refund" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pay_in_id' is set
        if ('pay_in_id' not in params) or (params['pay_in_id'] is None):
            raise ValueError("Missing the required parameter `pay_in_id` when calling `pay_ins_universal_pay_universal_pay_post_refund`")


        collection_formats = {}

        path_params = {}
        if 'pay_in_id' in params:
            path_params['PayInId'] = params['pay_in_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'universal_pay_refund' in params:
            body_params = params['universal_pay_refund']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain', 'application/json', 'text/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/json-patch+json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api('/v2.01/PayInsUniversalPay/payments/{PayInId}/refunds', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UniversalPayRefundResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def pay_ins_universal_pay_universal_pay_save_card(self, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.pay_ins_universal_pay_universal_pay_save_card(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UniversalPayTokenRequestPost universal_pay_save_card:
        :return: UniversalPayTokenizeByWebResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.pay_ins_universal_pay_universal_pay_save_card_with_http_info(**kwargs)
        else:
            (data) = self.pay_ins_universal_pay_universal_pay_save_card_with_http_info(**kwargs)
            return data

    def pay_ins_universal_pay_universal_pay_save_card_with_http_info(self, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.pay_ins_universal_pay_universal_pay_save_card_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param UniversalPayTokenRequestPost universal_pay_save_card:
        :return: UniversalPayTokenizeByWebResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['universal_pay_save_card']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pay_ins_universal_pay_universal_pay_save_card" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'universal_pay_save_card' in params:
            body_params = params['universal_pay_save_card']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['text/plain', 'application/json', 'text/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json', 'application/json-patch+json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api('/v2.01/PayInsUniversalPay/token/web', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UniversalPayTokenizeByWebResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
