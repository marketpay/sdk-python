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
from swagger_client.apis.transfers_api import TransfersApi


class TestTransfersApi(unittest.TestCase):
    """ TransfersApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.transfers_api.TransfersApi()

    def tearDown(self):
        pass

    def test_transfers_get(self):
        """
        Test case for transfers_get

        View a Transfer
        """
        pass

    def test_transfers_get_list(self):
        """
        Test case for transfers_get_list

        View a Transfer
        """
        pass

    def test_transfers_post(self):
        """
        Test case for transfers_post

        Create a Transfer
        """
        pass


if __name__ == '__main__':
    unittest.main()
