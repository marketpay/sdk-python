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


class UniversalPayPayByWebResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, pay_in_id=None, url=None):
        """
        UniversalPayPayByWebResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'pay_in_id': 'str',
            'url': 'str'
        }

        self.attribute_map = {
            'pay_in_id': 'PayInId',
            'url': 'Url'
        }

        self._pay_in_id = pay_in_id
        self._url = url

    @property
    def pay_in_id(self):
        """
        Gets the pay_in_id of this UniversalPayPayByWebResponse.
        Id of the payment

        :return: The pay_in_id of this UniversalPayPayByWebResponse.
        :rtype: str
        """
        return self._pay_in_id

    @pay_in_id.setter
    def pay_in_id(self, pay_in_id):
        """
        Sets the pay_in_id of this UniversalPayPayByWebResponse.
        Id of the payment

        :param pay_in_id: The pay_in_id of this UniversalPayPayByWebResponse.
        :type: str
        """

        self._pay_in_id = pay_in_id

    @property
    def url(self):
        """
        Gets the url of this UniversalPayPayByWebResponse.

        :return: The url of this UniversalPayPayByWebResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this UniversalPayPayByWebResponse.

        :param url: The url of this UniversalPayPayByWebResponse.
        :type: str
        """

        self._url = url

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
        if not isinstance(other, UniversalPayPayByWebResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other