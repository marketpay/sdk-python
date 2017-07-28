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


class AplazameOrderItem(object):
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
        'id': 'str',
        'name': 'str',
        'url': 'str',
        'image_url': 'str',
        'quantity': 'int',
        'price': 'int',
        'description': 'str',
        'tax_rate': 'int'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'url': 'Url',
        'image_url': 'ImageUrl',
        'quantity': 'Quantity',
        'price': 'Price',
        'description': 'Description',
        'tax_rate': 'TaxRate'
    }

    def __init__(self, id=None, name=None, url=None, image_url=None, quantity=None, price=None, description=None, tax_rate=None):
        """
        AplazameOrderItem - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._url = None
        self._image_url = None
        self._quantity = None
        self._price = None
        self._description = None
        self._tax_rate = None

        if id is not None:
          self.id = id
        self.name = name
        if url is not None:
          self.url = url
        if image_url is not None:
          self.image_url = image_url
        if quantity is not None:
          self.quantity = quantity
        self.price = price
        if description is not None:
          self.description = description
        if tax_rate is not None:
          self.tax_rate = tax_rate

    @property
    def id(self):
        """
        Gets the id of this AplazameOrderItem.

        :return: The id of this AplazameOrderItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AplazameOrderItem.

        :param id: The id of this AplazameOrderItem.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this AplazameOrderItem.

        :return: The name of this AplazameOrderItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AplazameOrderItem.

        :param name: The name of this AplazameOrderItem.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def url(self):
        """
        Gets the url of this AplazameOrderItem.

        :return: The url of this AplazameOrderItem.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this AplazameOrderItem.

        :param url: The url of this AplazameOrderItem.
        :type: str
        """

        self._url = url

    @property
    def image_url(self):
        """
        Gets the image_url of this AplazameOrderItem.

        :return: The image_url of this AplazameOrderItem.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """
        Sets the image_url of this AplazameOrderItem.

        :param image_url: The image_url of this AplazameOrderItem.
        :type: str
        """

        self._image_url = image_url

    @property
    def quantity(self):
        """
        Gets the quantity of this AplazameOrderItem.

        :return: The quantity of this AplazameOrderItem.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this AplazameOrderItem.

        :param quantity: The quantity of this AplazameOrderItem.
        :type: int
        """

        self._quantity = quantity

    @property
    def price(self):
        """
        Gets the price of this AplazameOrderItem.

        :return: The price of this AplazameOrderItem.
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this AplazameOrderItem.

        :param price: The price of this AplazameOrderItem.
        :type: int
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")

        self._price = price

    @property
    def description(self):
        """
        Gets the description of this AplazameOrderItem.

        :return: The description of this AplazameOrderItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AplazameOrderItem.

        :param description: The description of this AplazameOrderItem.
        :type: str
        """

        self._description = description

    @property
    def tax_rate(self):
        """
        Gets the tax_rate of this AplazameOrderItem.

        :return: The tax_rate of this AplazameOrderItem.
        :rtype: int
        """
        return self._tax_rate

    @tax_rate.setter
    def tax_rate(self, tax_rate):
        """
        Sets the tax_rate of this AplazameOrderItem.

        :param tax_rate: The tax_rate of this AplazameOrderItem.
        :type: int
        """

        self._tax_rate = tax_rate

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
        if not isinstance(other, AplazameOrderItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
