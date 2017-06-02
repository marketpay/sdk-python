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


class RedsysPreauthorizeByWebPost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, tag=None, save_card=None, card_id=None, author_id=None, statement_descriptor=None, success_url=None, url_ok=None, cancel_url=None, url_ko=None, debited_funds=None):
        """
        RedsysPreauthorizeByWebPost - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'tag': 'str',
            'save_card': 'bool',
            'card_id': 'str',
            'author_id': 'str',
            'statement_descriptor': 'str',
            'success_url': 'str',
            'url_ok': 'str',
            'cancel_url': 'str',
            'url_ko': 'str',
            'debited_funds': 'Money'
        }

        self.attribute_map = {
            'tag': 'Tag',
            'save_card': 'SaveCard',
            'card_id': 'CardId',
            'author_id': 'AuthorId',
            'statement_descriptor': 'StatementDescriptor',
            'success_url': 'SuccessUrl',
            'url_ok': 'UrlOk',
            'cancel_url': 'CancelUrl',
            'url_ko': 'UrlKo',
            'debited_funds': 'DebitedFunds'
        }

        self._tag = tag
        self._save_card = save_card
        self._card_id = card_id
        self._author_id = author_id
        self._statement_descriptor = statement_descriptor
        self._success_url = success_url
        self._url_ok = url_ok
        self._cancel_url = cancel_url
        self._url_ko = url_ko
        self._debited_funds = debited_funds

    @property
    def tag(self):
        """
        Gets the tag of this RedsysPreauthorizeByWebPost.
        Custom data that you can add to this item

        :return: The tag of this RedsysPreauthorizeByWebPost.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this RedsysPreauthorizeByWebPost.
        Custom data that you can add to this item

        :param tag: The tag of this RedsysPreauthorizeByWebPost.
        :type: str
        """

        self._tag = tag

    @property
    def save_card(self):
        """
        Gets the save_card of this RedsysPreauthorizeByWebPost.
        Whether to save or not the card for future use. SaveCard and CardId are mutually exclusive

        :return: The save_card of this RedsysPreauthorizeByWebPost.
        :rtype: bool
        """
        return self._save_card

    @save_card.setter
    def save_card(self, save_card):
        """
        Sets the save_card of this RedsysPreauthorizeByWebPost.
        Whether to save or not the card for future use. SaveCard and CardId are mutually exclusive

        :param save_card: The save_card of this RedsysPreauthorizeByWebPost.
        :type: bool
        """

        self._save_card = save_card

    @property
    def card_id(self):
        """
        Gets the card_id of this RedsysPreauthorizeByWebPost.
        The id of a previous saved card. SaveCard and CardId are mutually exclusive

        :return: The card_id of this RedsysPreauthorizeByWebPost.
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        """
        Sets the card_id of this RedsysPreauthorizeByWebPost.
        The id of a previous saved card. SaveCard and CardId are mutually exclusive

        :param card_id: The card_id of this RedsysPreauthorizeByWebPost.
        :type: str
        """

        self._card_id = card_id

    @property
    def author_id(self):
        """
        Gets the author_id of this RedsysPreauthorizeByWebPost.
        A user's ID

        :return: The author_id of this RedsysPreauthorizeByWebPost.
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """
        Sets the author_id of this RedsysPreauthorizeByWebPost.
        A user's ID

        :param author_id: The author_id of this RedsysPreauthorizeByWebPost.
        :type: str
        """

        self._author_id = author_id

    @property
    def statement_descriptor(self):
        """
        Gets the statement_descriptor of this RedsysPreauthorizeByWebPost.
        A custom description to appear on the user's bank statement. It can be up to 10 characters long, and can only include alphanumeric characters or spaces

        :return: The statement_descriptor of this RedsysPreauthorizeByWebPost.
        :rtype: str
        """
        return self._statement_descriptor

    @statement_descriptor.setter
    def statement_descriptor(self, statement_descriptor):
        """
        Sets the statement_descriptor of this RedsysPreauthorizeByWebPost.
        A custom description to appear on the user's bank statement. It can be up to 10 characters long, and can only include alphanumeric characters or spaces

        :param statement_descriptor: The statement_descriptor of this RedsysPreauthorizeByWebPost.
        :type: str
        """

        self._statement_descriptor = statement_descriptor

    @property
    def success_url(self):
        """
        Gets the success_url of this RedsysPreauthorizeByWebPost.
        Dirección (relativa a la tienda) a la que redirigirá cuando se haya completado el pago.

        :return: The success_url of this RedsysPreauthorizeByWebPost.
        :rtype: str
        """
        return self._success_url

    @success_url.setter
    def success_url(self, success_url):
        """
        Sets the success_url of this RedsysPreauthorizeByWebPost.
        Dirección (relativa a la tienda) a la que redirigirá cuando se haya completado el pago.

        :param success_url: The success_url of this RedsysPreauthorizeByWebPost.
        :type: str
        """
        if success_url is None:
            raise ValueError("Invalid value for `success_url`, must not be `None`")

        self._success_url = success_url

    @property
    def url_ok(self):
        """
        Gets the url_ok of this RedsysPreauthorizeByWebPost.
        Url to redirect the browser in case the payment is completed successfully

        :return: The url_ok of this RedsysPreauthorizeByWebPost.
        :rtype: str
        """
        return self._url_ok

    @url_ok.setter
    def url_ok(self, url_ok):
        """
        Sets the url_ok of this RedsysPreauthorizeByWebPost.
        Url to redirect the browser in case the payment is completed successfully

        :param url_ok: The url_ok of this RedsysPreauthorizeByWebPost.
        :type: str
        """

        self._url_ok = url_ok

    @property
    def cancel_url(self):
        """
        Gets the cancel_url of this RedsysPreauthorizeByWebPost.
        Dirección (relativa a la tienda) a la que redirigirá en caso de error en el pago.

        :return: The cancel_url of this RedsysPreauthorizeByWebPost.
        :rtype: str
        """
        return self._cancel_url

    @cancel_url.setter
    def cancel_url(self, cancel_url):
        """
        Sets the cancel_url of this RedsysPreauthorizeByWebPost.
        Dirección (relativa a la tienda) a la que redirigirá en caso de error en el pago.

        :param cancel_url: The cancel_url of this RedsysPreauthorizeByWebPost.
        :type: str
        """
        if cancel_url is None:
            raise ValueError("Invalid value for `cancel_url`, must not be `None`")

        self._cancel_url = cancel_url

    @property
    def url_ko(self):
        """
        Gets the url_ko of this RedsysPreauthorizeByWebPost.
        Url to redirect the browser in case the payment is not completed successfully

        :return: The url_ko of this RedsysPreauthorizeByWebPost.
        :rtype: str
        """
        return self._url_ko

    @url_ko.setter
    def url_ko(self, url_ko):
        """
        Sets the url_ko of this RedsysPreauthorizeByWebPost.
        Url to redirect the browser in case the payment is not completed successfully

        :param url_ko: The url_ko of this RedsysPreauthorizeByWebPost.
        :type: str
        """

        self._url_ko = url_ko

    @property
    def debited_funds(self):
        """
        Gets the debited_funds of this RedsysPreauthorizeByWebPost.
        Information about the funds that are being debited

        :return: The debited_funds of this RedsysPreauthorizeByWebPost.
        :rtype: Money
        """
        return self._debited_funds

    @debited_funds.setter
    def debited_funds(self, debited_funds):
        """
        Sets the debited_funds of this RedsysPreauthorizeByWebPost.
        Information about the funds that are being debited

        :param debited_funds: The debited_funds of this RedsysPreauthorizeByWebPost.
        :type: Money
        """

        self._debited_funds = debited_funds

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
        if not isinstance(other, RedsysPreauthorizeByWebPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other