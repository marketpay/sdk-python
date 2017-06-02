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


class WalletResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, owners=None, balance=None, funds_type=None, description=None, currency=None, id=None, creation_date=None, tag=None):
        """
        WalletResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'owners': 'list[str]',
            'balance': 'Money',
            'funds_type': 'str',
            'description': 'str',
            'currency': 'str',
            'id': 'str',
            'creation_date': 'int',
            'tag': 'str'
        }

        self.attribute_map = {
            'owners': 'Owners',
            'balance': 'Balance',
            'funds_type': 'FundsType',
            'description': 'Description',
            'currency': 'Currency',
            'id': 'Id',
            'creation_date': 'CreationDate',
            'tag': 'Tag'
        }

        self._owners = owners
        self._balance = balance
        self._funds_type = funds_type
        self._description = description
        self._currency = currency
        self._id = id
        self._creation_date = creation_date
        self._tag = tag

    @property
    def owners(self):
        """
        Gets the owners of this WalletResponse.
        An array of userIDs of who own's the wallet. For now, you only can set up a unique owner

        :return: The owners of this WalletResponse.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this WalletResponse.
        An array of userIDs of who own's the wallet. For now, you only can set up a unique owner

        :param owners: The owners of this WalletResponse.
        :type: list[str]
        """

        self._owners = owners

    @property
    def balance(self):
        """
        Gets the balance of this WalletResponse.
        The current balance of the wallet

        :return: The balance of this WalletResponse.
        :rtype: Money
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """
        Sets the balance of this WalletResponse.
        The current balance of the wallet

        :param balance: The balance of this WalletResponse.
        :type: Money
        """

        self._balance = balance

    @property
    def funds_type(self):
        """
        Gets the funds_type of this WalletResponse.
        The type of funds in the wallet

        :return: The funds_type of this WalletResponse.
        :rtype: str
        """
        return self._funds_type

    @funds_type.setter
    def funds_type(self, funds_type):
        """
        Sets the funds_type of this WalletResponse.
        The type of funds in the wallet

        :param funds_type: The funds_type of this WalletResponse.
        :type: str
        """
        allowed_values = ["NotSpecified", "DEFAULT", "FEES", "CREDIT"]
        if funds_type not in allowed_values:
            raise ValueError(
                "Invalid value for `funds_type` ({0}), must be one of {1}"
                .format(funds_type, allowed_values)
            )

        self._funds_type = funds_type

    @property
    def description(self):
        """
        Gets the description of this WalletResponse.
        A desciption of the wallet

        :return: The description of this WalletResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WalletResponse.
        A desciption of the wallet

        :param description: The description of this WalletResponse.
        :type: str
        """

        self._description = description

    @property
    def currency(self):
        """
        Gets the currency of this WalletResponse.
        The currency - should be ISO_4217 format

        :return: The currency of this WalletResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """
        Sets the currency of this WalletResponse.
        The currency - should be ISO_4217 format

        :param currency: The currency of this WalletResponse.
        :type: str
        """
        allowed_values = ["NotSpecified", "XXX", "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYR", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "CNY", "COP", "COU", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LTL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STD", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "USS", "UYI", "UYU", "UZS", "VEF", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XBA", "XBB", "XBC", "XBD", "XBT", "XCD", "XDR", "XFU", "XOF", "XPD", "XPF", "XPT", "XSU", "XTS", "XUA", "YER", "ZAR", "ZMW", "ZWD"]
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def id(self):
        """
        Gets the id of this WalletResponse.

        :return: The id of this WalletResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WalletResponse.

        :param id: The id of this WalletResponse.
        :type: str
        """

        self._id = id

    @property
    def creation_date(self):
        """
        Gets the creation_date of this WalletResponse.

        :return: The creation_date of this WalletResponse.
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this WalletResponse.

        :param creation_date: The creation_date of this WalletResponse.
        :type: int
        """

        self._creation_date = creation_date

    @property
    def tag(self):
        """
        Gets the tag of this WalletResponse.

        :return: The tag of this WalletResponse.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this WalletResponse.

        :param tag: The tag of this WalletResponse.
        :type: str
        """

        self._tag = tag

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
        if not isinstance(other, WalletResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
