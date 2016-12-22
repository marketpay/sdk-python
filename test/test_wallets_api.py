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
from swagger_client.apis.wallets_api import WalletsApi


class TestWalletsApi(unittest.TestCase):
    """ WalletsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.wallets_api.WalletsApi()

    def tearDown(self):
        pass

    def test_wallets_get(self):
        """
        Test case for wallets_get

        View a Wallet
        """
        pass

    def test_wallets_get_transaction_list(self):
        """
        Test case for wallets_get_transaction_list

        List a Wallet's Transactions
        """
        pass

    def test_wallets_post(self):
        """
        Test case for wallets_post

        Create a Wallet
        """
        pass

    def test_wallets_put(self):
        """
        Test case for wallets_put

        Update a Wallet
        """
        pass


if __name__ == '__main__':
    unittest.main()
