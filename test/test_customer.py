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
from swagger_client.models.customer import Customer


class TestCustomer(unittest.TestCase):
    """ Customer unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomer(self):
        """
        Test Customer
        """
        model = swagger_client.models.customer.Customer()


if __name__ == '__main__':
    unittest.main()
