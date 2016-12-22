# coding: utf-8

"""
    MarketPay API

    API for Smart Contracts and Payments

    OpenAPI spec version: v2.01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BankAccountGbPost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, sort_code=None, account_number=None, tag=None, owner_address=None, owner_name=None):
        """
        BankAccountGbPost - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'sort_code': 'str',
            'account_number': 'str',
            'tag': 'str',
            'owner_address': 'Address',
            'owner_name': 'str'
        }

        self.attribute_map = {
            'sort_code': 'SortCode',
            'account_number': 'AccountNumber',
            'tag': 'Tag',
            'owner_address': 'OwnerAddress',
            'owner_name': 'OwnerName'
        }

        self._sort_code = sort_code
        self._account_number = account_number
        self._tag = tag
        self._owner_address = owner_address
        self._owner_name = owner_name

    @property
    def sort_code(self):
        """
        Gets the sort_code of this BankAccountGbPost.
        The sort code of the bank account. Must be numbers only, and 6 digits long

        :return: The sort_code of this BankAccountGbPost.
        :rtype: str
        """
        return self._sort_code

    @sort_code.setter
    def sort_code(self, sort_code):
        """
        Sets the sort_code of this BankAccountGbPost.
        The sort code of the bank account. Must be numbers only, and 6 digits long

        :param sort_code: The sort_code of this BankAccountGbPost.
        :type: str
        """

        self._sort_code = sort_code

    @property
    def account_number(self):
        """
        Gets the account_number of this BankAccountGbPost.
        The account number of the bank account. Must be numbers only. GB account numbers must be 8 digits long

        :return: The account_number of this BankAccountGbPost.
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """
        Sets the account_number of this BankAccountGbPost.
        The account number of the bank account. Must be numbers only. GB account numbers must be 8 digits long

        :param account_number: The account_number of this BankAccountGbPost.
        :type: str
        """

        self._account_number = account_number

    @property
    def tag(self):
        """
        Gets the tag of this BankAccountGbPost.
        Custom data that you can add to this item

        :return: The tag of this BankAccountGbPost.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this BankAccountGbPost.
        Custom data that you can add to this item

        :param tag: The tag of this BankAccountGbPost.
        :type: str
        """

        self._tag = tag

    @property
    def owner_address(self):
        """
        Gets the owner_address of this BankAccountGbPost.
        The address of the owner of the bank account

        :return: The owner_address of this BankAccountGbPost.
        :rtype: Address
        """
        return self._owner_address

    @owner_address.setter
    def owner_address(self, owner_address):
        """
        Sets the owner_address of this BankAccountGbPost.
        The address of the owner of the bank account

        :param owner_address: The owner_address of this BankAccountGbPost.
        :type: Address
        """

        self._owner_address = owner_address

    @property
    def owner_name(self):
        """
        Gets the owner_name of this BankAccountGbPost.
        The name of the owner of the bank account

        :return: The owner_name of this BankAccountGbPost.
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """
        Sets the owner_name of this BankAccountGbPost.
        The name of the owner of the bank account

        :param owner_name: The owner_name of this BankAccountGbPost.
        :type: str
        """

        self._owner_name = owner_name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other