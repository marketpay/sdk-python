# coding: utf-8

"""
    MarketPay API

    API for Smart Contracts and Payments

    OpenAPI spec version: v2.01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.pay_ins_universal_pay_api import PayInsUniversalPayApi


class TestPayInsUniversalPayApi(unittest.TestCase):
    """ PayInsUniversalPayApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.pay_ins_universal_pay_api.PayInsUniversalPayApi()

    def tearDown(self):
        pass

    def test_pay_ins_universal_pay_get_universal_pay_tokenization(self):
        """
        Test case for pay_ins_universal_pay_get_universal_pay_tokenization

        View a UniversalPay card tokenization status
        """
        pass

    def test_pay_ins_universal_pay_universal_pay_get_payment(self):
        """
        Test case for pay_ins_universal_pay_universal_pay_get_payment

        View a UniversalPay payment
        """
        pass

    def test_pay_ins_universal_pay_universal_pay_post_payment_by_web(self):
        """
        Test case for pay_ins_universal_pay_universal_pay_post_payment_by_web

        Create a UniversalPay PayIn Request
        """
        pass

    def test_pay_ins_universal_pay_universal_pay_post_refund(self):
        """
        Test case for pay_ins_universal_pay_universal_pay_post_refund

        Create a UniversalPay Payment Refund
        """
        pass

    def test_pay_ins_universal_pay_universal_pay_save_card(self):
        """
        Test case for pay_ins_universal_pay_universal_pay_save_card

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
