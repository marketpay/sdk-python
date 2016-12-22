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


class TransferPost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, tag=None, author_id=None, credited_user_id=None, debited_funds=None, fees=None, debited_wallet_id=None, credited_wallet_id=None):
        """
        TransferPost - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'tag': 'str',
            'author_id': 'str',
            'credited_user_id': 'str',
            'debited_funds': 'Money',
            'fees': 'Money',
            'debited_wallet_id': 'str',
            'credited_wallet_id': 'str'
        }

        self.attribute_map = {
            'tag': 'Tag',
            'author_id': 'AuthorId',
            'credited_user_id': 'CreditedUserId',
            'debited_funds': 'DebitedFunds',
            'fees': 'Fees',
            'debited_wallet_id': 'DebitedWalletId',
            'credited_wallet_id': 'CreditedWalletId'
        }

        self._tag = tag
        self._author_id = author_id
        self._credited_user_id = credited_user_id
        self._debited_funds = debited_funds
        self._fees = fees
        self._debited_wallet_id = debited_wallet_id
        self._credited_wallet_id = credited_wallet_id

    @property
    def tag(self):
        """
        Gets the tag of this TransferPost.
        Custom data that you can add to this item

        :return: The tag of this TransferPost.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this TransferPost.
        Custom data that you can add to this item

        :param tag: The tag of this TransferPost.
        :type: str
        """

        self._tag = tag

    @property
    def author_id(self):
        """
        Gets the author_id of this TransferPost.
        A user's ID

        :return: The author_id of this TransferPost.
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """
        Sets the author_id of this TransferPost.
        A user's ID

        :param author_id: The author_id of this TransferPost.
        :type: str
        """

        self._author_id = author_id

    @property
    def credited_user_id(self):
        """
        Gets the credited_user_id of this TransferPost.
        The user ID who was credited

        :return: The credited_user_id of this TransferPost.
        :rtype: str
        """
        return self._credited_user_id

    @credited_user_id.setter
    def credited_user_id(self, credited_user_id):
        """
        Sets the credited_user_id of this TransferPost.
        The user ID who was credited

        :param credited_user_id: The credited_user_id of this TransferPost.
        :type: str
        """

        self._credited_user_id = credited_user_id

    @property
    def debited_funds(self):
        """
        Gets the debited_funds of this TransferPost.
        Information about the funds that are being debited

        :return: The debited_funds of this TransferPost.
        :rtype: Money
        """
        return self._debited_funds

    @debited_funds.setter
    def debited_funds(self, debited_funds):
        """
        Sets the debited_funds of this TransferPost.
        Information about the funds that are being debited

        :param debited_funds: The debited_funds of this TransferPost.
        :type: Money
        """

        self._debited_funds = debited_funds

    @property
    def fees(self):
        """
        Gets the fees of this TransferPost.
        Information about the fees that were taken by the client for this transaction (and were hence transferred to the Client's platform wallet)

        :return: The fees of this TransferPost.
        :rtype: Money
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """
        Sets the fees of this TransferPost.
        Information about the fees that were taken by the client for this transaction (and were hence transferred to the Client's platform wallet)

        :param fees: The fees of this TransferPost.
        :type: Money
        """

        self._fees = fees

    @property
    def debited_wallet_id(self):
        """
        Gets the debited_wallet_id of this TransferPost.
        The ID of the wallet that was debited

        :return: The debited_wallet_id of this TransferPost.
        :rtype: str
        """
        return self._debited_wallet_id

    @debited_wallet_id.setter
    def debited_wallet_id(self, debited_wallet_id):
        """
        Sets the debited_wallet_id of this TransferPost.
        The ID of the wallet that was debited

        :param debited_wallet_id: The debited_wallet_id of this TransferPost.
        :type: str
        """

        self._debited_wallet_id = debited_wallet_id

    @property
    def credited_wallet_id(self):
        """
        Gets the credited_wallet_id of this TransferPost.
        The ID of the wallet where money will be credited

        :return: The credited_wallet_id of this TransferPost.
        :rtype: str
        """
        return self._credited_wallet_id

    @credited_wallet_id.setter
    def credited_wallet_id(self, credited_wallet_id):
        """
        Sets the credited_wallet_id of this TransferPost.
        The ID of the wallet where money will be credited

        :param credited_wallet_id: The credited_wallet_id of this TransferPost.
        :type: str
        """

        self._credited_wallet_id = credited_wallet_id

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