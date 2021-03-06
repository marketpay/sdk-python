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


class RedsysPayByWebPost(object):
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
        'save_card': 'bool',
        'card_id': 'str',
        'credited_wallet_id': 'str',
        'statement_descriptor': 'str',
        'success_url': 'str',
        'cancel_url': 'str',
        'debited_funds': 'Money',
        'fees': 'Money',
        'language': 'str'
    }

    attribute_map = {
        'tag': 'Tag',
        'save_card': 'SaveCard',
        'card_id': 'CardId',
        'credited_wallet_id': 'CreditedWalletId',
        'statement_descriptor': 'StatementDescriptor',
        'success_url': 'SuccessUrl',
        'cancel_url': 'CancelUrl',
        'debited_funds': 'DebitedFunds',
        'fees': 'Fees',
        'language': 'Language'
    }

    def __init__(self, tag=None, save_card=None, card_id=None, credited_wallet_id=None, statement_descriptor=None, success_url=None, cancel_url=None, debited_funds=None, fees=None, language=None):
        """
        RedsysPayByWebPost - a model defined in Swagger
        """

        self._tag = None
        self._save_card = None
        self._card_id = None
        self._credited_wallet_id = None
        self._statement_descriptor = None
        self._success_url = None
        self._cancel_url = None
        self._debited_funds = None
        self._fees = None
        self._language = None

        if tag is not None:
          self.tag = tag
        if save_card is not None:
          self.save_card = save_card
        if card_id is not None:
          self.card_id = card_id
        self.credited_wallet_id = credited_wallet_id
        if statement_descriptor is not None:
          self.statement_descriptor = statement_descriptor
        self.success_url = success_url
        self.cancel_url = cancel_url
        self.debited_funds = debited_funds
        self.fees = fees
        if language is not None:
          self.language = language

    @property
    def tag(self):
        """
        Gets the tag of this RedsysPayByWebPost.
        Custom data that you can add to this item

        :return: The tag of this RedsysPayByWebPost.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this RedsysPayByWebPost.
        Custom data that you can add to this item

        :param tag: The tag of this RedsysPayByWebPost.
        :type: str
        """

        self._tag = tag

    @property
    def save_card(self):
        """
        Gets the save_card of this RedsysPayByWebPost.
        Whether to save or not the card for future use. SaveCard and CardId are mutually exclusive

        :return: The save_card of this RedsysPayByWebPost.
        :rtype: bool
        """
        return self._save_card

    @save_card.setter
    def save_card(self, save_card):
        """
        Sets the save_card of this RedsysPayByWebPost.
        Whether to save or not the card for future use. SaveCard and CardId are mutually exclusive

        :param save_card: The save_card of this RedsysPayByWebPost.
        :type: bool
        """

        self._save_card = save_card

    @property
    def card_id(self):
        """
        Gets the card_id of this RedsysPayByWebPost.
        The id of a previous saved card. SaveCard and CardId are mutually exclusive

        :return: The card_id of this RedsysPayByWebPost.
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id):
        """
        Sets the card_id of this RedsysPayByWebPost.
        The id of a previous saved card. SaveCard and CardId are mutually exclusive

        :param card_id: The card_id of this RedsysPayByWebPost.
        :type: str
        """

        self._card_id = card_id

    @property
    def credited_wallet_id(self):
        """
        Gets the credited_wallet_id of this RedsysPayByWebPost.
        The ID of the wallet where money will be credited

        :return: The credited_wallet_id of this RedsysPayByWebPost.
        :rtype: str
        """
        return self._credited_wallet_id

    @credited_wallet_id.setter
    def credited_wallet_id(self, credited_wallet_id):
        """
        Sets the credited_wallet_id of this RedsysPayByWebPost.
        The ID of the wallet where money will be credited

        :param credited_wallet_id: The credited_wallet_id of this RedsysPayByWebPost.
        :type: str
        """
        if credited_wallet_id is None:
            raise ValueError("Invalid value for `credited_wallet_id`, must not be `None`")

        self._credited_wallet_id = credited_wallet_id

    @property
    def statement_descriptor(self):
        """
        Gets the statement_descriptor of this RedsysPayByWebPost.
        A custom description to appear on the user's bank statement. It can be up to 10 characters long, and can only include alphanumeric characters or spaces

        :return: The statement_descriptor of this RedsysPayByWebPost.
        :rtype: str
        """
        return self._statement_descriptor

    @statement_descriptor.setter
    def statement_descriptor(self, statement_descriptor):
        """
        Sets the statement_descriptor of this RedsysPayByWebPost.
        A custom description to appear on the user's bank statement. It can be up to 10 characters long, and can only include alphanumeric characters or spaces

        :param statement_descriptor: The statement_descriptor of this RedsysPayByWebPost.
        :type: str
        """

        self._statement_descriptor = statement_descriptor

    @property
    def success_url(self):
        """
        Gets the success_url of this RedsysPayByWebPost.
        Dirección (relativa a la tienda) a la que redirigirá cuando se haya completado el pago.

        :return: The success_url of this RedsysPayByWebPost.
        :rtype: str
        """
        return self._success_url

    @success_url.setter
    def success_url(self, success_url):
        """
        Sets the success_url of this RedsysPayByWebPost.
        Dirección (relativa a la tienda) a la que redirigirá cuando se haya completado el pago.

        :param success_url: The success_url of this RedsysPayByWebPost.
        :type: str
        """
        if success_url is None:
            raise ValueError("Invalid value for `success_url`, must not be `None`")

        self._success_url = success_url

    @property
    def cancel_url(self):
        """
        Gets the cancel_url of this RedsysPayByWebPost.
        Dirección (relativa a la tienda) a la que redirigirá en caso de error en el pago.

        :return: The cancel_url of this RedsysPayByWebPost.
        :rtype: str
        """
        return self._cancel_url

    @cancel_url.setter
    def cancel_url(self, cancel_url):
        """
        Sets the cancel_url of this RedsysPayByWebPost.
        Dirección (relativa a la tienda) a la que redirigirá en caso de error en el pago.

        :param cancel_url: The cancel_url of this RedsysPayByWebPost.
        :type: str
        """
        if cancel_url is None:
            raise ValueError("Invalid value for `cancel_url`, must not be `None`")

        self._cancel_url = cancel_url

    @property
    def debited_funds(self):
        """
        Gets the debited_funds of this RedsysPayByWebPost.
        Information about the funds that are being debited

        :return: The debited_funds of this RedsysPayByWebPost.
        :rtype: Money
        """
        return self._debited_funds

    @debited_funds.setter
    def debited_funds(self, debited_funds):
        """
        Sets the debited_funds of this RedsysPayByWebPost.
        Information about the funds that are being debited

        :param debited_funds: The debited_funds of this RedsysPayByWebPost.
        :type: Money
        """
        if debited_funds is None:
            raise ValueError("Invalid value for `debited_funds`, must not be `None`")

        self._debited_funds = debited_funds

    @property
    def fees(self):
        """
        Gets the fees of this RedsysPayByWebPost.
        Information about the fees that were taken by the client for this transaction (and were hence transferred to the Client's platform wallet)

        :return: The fees of this RedsysPayByWebPost.
        :rtype: Money
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """
        Sets the fees of this RedsysPayByWebPost.
        Information about the fees that were taken by the client for this transaction (and were hence transferred to the Client's platform wallet)

        :param fees: The fees of this RedsysPayByWebPost.
        :type: Money
        """
        if fees is None:
            raise ValueError("Invalid value for `fees`, must not be `None`")

        self._fees = fees

    @property
    def language(self):
        """
        Gets the language of this RedsysPayByWebPost.
        Valid values are ES, EN, CA, FR, DE, NL, IT, SV, PT, PL, GL and EU

        :return: The language of this RedsysPayByWebPost.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this RedsysPayByWebPost.
        Valid values are ES, EN, CA, FR, DE, NL, IT, SV, PT, PL, GL and EU

        :param language: The language of this RedsysPayByWebPost.
        :type: str
        """
        allowed_values = ["NotSpecified", "CA", "DE", "EN", "DA", "ES", "ET", "GL", "FI", "FR", "EL", "EU", "HU", "IT", "NL", "NO", "PL", "PT", "SK", "SV", "CS"]
        if language not in allowed_values:
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"
                .format(language, allowed_values)
            )

        self._language = language

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
        if not isinstance(other, RedsysPayByWebPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
