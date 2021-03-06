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
from swagger_client.apis.cards_api import CardsApi


class TestCardsApi(unittest.TestCase):
    """ CardsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.cards_api.CardsApi()

    def tearDown(self):
        pass

    def test_cards_get(self):
        """
        Test case for cards_get

        View a Card
        """
        pass

    def test_cards_get_list(self):
        """
        Test case for cards_get_list

        
        """
        pass

    def test_cards_put(self):
        """
        Test case for cards_put

        Deactivate a Card
        """
        pass


if __name__ == '__main__':
    unittest.main()
