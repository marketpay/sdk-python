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


class CustomerDetail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, email=None, first_name=None, last_name=None, telephone=None, address=None):
        """
        CustomerDetail - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'email': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'telephone': 'Telephone',
            'address': 'Address'
        }

        self.attribute_map = {
            'email': 'Email',
            'first_name': 'FirstName',
            'last_name': 'LastName',
            'telephone': 'Telephone',
            'address': 'Address'
        }

        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._telephone = telephone
        self._address = address

    @property
    def email(self):
        """
        Gets the email of this CustomerDetail.

        :return: The email of this CustomerDetail.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CustomerDetail.

        :param email: The email of this CustomerDetail.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")
        if email is not None and len(email) > 50:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `50`")

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this CustomerDetail.

        :return: The first_name of this CustomerDetail.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this CustomerDetail.

        :param first_name: The first_name of this CustomerDetail.
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")
        if first_name is not None and len(first_name) > 32:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `32`")

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this CustomerDetail.

        :return: The last_name of this CustomerDetail.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this CustomerDetail.

        :param last_name: The last_name of this CustomerDetail.
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")
        if last_name is not None and len(last_name) > 32:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `32`")

        self._last_name = last_name

    @property
    def telephone(self):
        """
        Gets the telephone of this CustomerDetail.

        :return: The telephone of this CustomerDetail.
        :rtype: Telephone
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """
        Sets the telephone of this CustomerDetail.

        :param telephone: The telephone of this CustomerDetail.
        :type: Telephone
        """

        self._telephone = telephone

    @property
    def address(self):
        """
        Gets the address of this CustomerDetail.

        :return: The address of this CustomerDetail.
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this CustomerDetail.

        :param address: The address of this CustomerDetail.
        :type: Address
        """

        self._address = address

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
        if not isinstance(other, CustomerDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
