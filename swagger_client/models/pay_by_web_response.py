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


class PayByWebResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, pay_in_id=None, url=None, ds_signature_version=None, ds_merchant_parameters=None, ds_signature=None):
        """
        PayByWebResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'pay_in_id': 'str',
            'url': 'str',
            'ds_signature_version': 'str',
            'ds_merchant_parameters': 'str',
            'ds_signature': 'str'
        }

        self.attribute_map = {
            'pay_in_id': 'PayInId',
            'url': 'Url',
            'ds_signature_version': 'Ds_SignatureVersion',
            'ds_merchant_parameters': 'Ds_MerchantParameters',
            'ds_signature': 'Ds_Signature'
        }

        self._pay_in_id = pay_in_id
        self._url = url
        self._ds_signature_version = ds_signature_version
        self._ds_merchant_parameters = ds_merchant_parameters
        self._ds_signature = ds_signature

    @property
    def pay_in_id(self):
        """
        Gets the pay_in_id of this PayByWebResponse.
        Id of the payment

        :return: The pay_in_id of this PayByWebResponse.
        :rtype: str
        """
        return self._pay_in_id

    @pay_in_id.setter
    def pay_in_id(self, pay_in_id):
        """
        Sets the pay_in_id of this PayByWebResponse.
        Id of the payment

        :param pay_in_id: The pay_in_id of this PayByWebResponse.
        :type: str
        """

        self._pay_in_id = pay_in_id

    @property
    def url(self):
        """
        Gets the url of this PayByWebResponse.
        Url to post from the user's browser

        :return: The url of this PayByWebResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this PayByWebResponse.
        Url to post from the user's browser

        :param url: The url of this PayByWebResponse.
        :type: str
        """

        self._url = url

    @property
    def ds_signature_version(self):
        """
        Gets the ds_signature_version of this PayByWebResponse.
        This paramater must be include in the Post to the Url

        :return: The ds_signature_version of this PayByWebResponse.
        :rtype: str
        """
        return self._ds_signature_version

    @ds_signature_version.setter
    def ds_signature_version(self, ds_signature_version):
        """
        Sets the ds_signature_version of this PayByWebResponse.
        This paramater must be include in the Post to the Url

        :param ds_signature_version: The ds_signature_version of this PayByWebResponse.
        :type: str
        """

        self._ds_signature_version = ds_signature_version

    @property
    def ds_merchant_parameters(self):
        """
        Gets the ds_merchant_parameters of this PayByWebResponse.
        This paramater must be include in the Post to the Url

        :return: The ds_merchant_parameters of this PayByWebResponse.
        :rtype: str
        """
        return self._ds_merchant_parameters

    @ds_merchant_parameters.setter
    def ds_merchant_parameters(self, ds_merchant_parameters):
        """
        Sets the ds_merchant_parameters of this PayByWebResponse.
        This paramater must be include in the Post to the Url

        :param ds_merchant_parameters: The ds_merchant_parameters of this PayByWebResponse.
        :type: str
        """

        self._ds_merchant_parameters = ds_merchant_parameters

    @property
    def ds_signature(self):
        """
        Gets the ds_signature of this PayByWebResponse.
        This paramater must be include in the Post to the Url

        :return: The ds_signature of this PayByWebResponse.
        :rtype: str
        """
        return self._ds_signature

    @ds_signature.setter
    def ds_signature(self, ds_signature):
        """
        Sets the ds_signature of this PayByWebResponse.
        This paramater must be include in the Post to the Url

        :param ds_signature: The ds_signature of this PayByWebResponse.
        :type: str
        """

        self._ds_signature = ds_signature

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