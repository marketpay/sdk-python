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


class AplazameRefundPaymentPost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'tag': 'str',
        'debited_funds': 'Money',
        'fees': 'Money'
    }

    attribute_map = {
        'tag': 'Tag',
        'debited_funds': 'DebitedFunds',
        'fees': 'Fees'
    }

    def __init__(self, tag=None, debited_funds=None, fees=None):
        """
        AplazameRefundPaymentPost - a model defined in Swagger
        """

        self._tag = None
        self._debited_funds = None
        self._fees = None

        if tag is not None:
          self.tag = tag
        self.debited_funds = debited_funds
        self.fees = fees

    @property
    def tag(self):
        """
        Gets the tag of this AplazameRefundPaymentPost.
        Custom data that you can add to this item

        :return: The tag of this AplazameRefundPaymentPost.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this AplazameRefundPaymentPost.
        Custom data that you can add to this item

        :param tag: The tag of this AplazameRefundPaymentPost.
        :type: str
        """

        self._tag = tag

    @property
    def debited_funds(self):
        """
        Gets the debited_funds of this AplazameRefundPaymentPost.

        :return: The debited_funds of this AplazameRefundPaymentPost.
        :rtype: Money
        """
        return self._debited_funds

    @debited_funds.setter
    def debited_funds(self, debited_funds):
        """
        Sets the debited_funds of this AplazameRefundPaymentPost.

        :param debited_funds: The debited_funds of this AplazameRefundPaymentPost.
        :type: Money
        """
        if debited_funds is None:
            raise ValueError("Invalid value for `debited_funds`, must not be `None`")

        self._debited_funds = debited_funds

    @property
    def fees(self):
        """
        Gets the fees of this AplazameRefundPaymentPost.

        :return: The fees of this AplazameRefundPaymentPost.
        :rtype: Money
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """
        Sets the fees of this AplazameRefundPaymentPost.

        :param fees: The fees of this AplazameRefundPaymentPost.
        :type: Money
        """
        if fees is None:
            raise ValueError("Invalid value for `fees`, must not be `None`")

        self._fees = fees

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
        if not isinstance(other, AplazameRefundPaymentPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
