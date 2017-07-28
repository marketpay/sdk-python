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


class UserNaturalPut(object):
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
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'address': 'Address',
        'birthday': 'int',
        'nationality': 'str',
        'country_of_residence': 'str',
        'occupation': 'str',
        'income_range': 'int',
        'tag': 'str'
    }

    attribute_map = {
        'email': 'Email',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'address': 'Address',
        'birthday': 'Birthday',
        'nationality': 'Nationality',
        'country_of_residence': 'CountryOfResidence',
        'occupation': 'Occupation',
        'income_range': 'IncomeRange',
        'tag': 'Tag'
    }

    def __init__(self, email=None, first_name=None, last_name=None, address=None, birthday=None, nationality=None, country_of_residence=None, occupation=None, income_range=None, tag=None):
        """
        UserNaturalPut - a model defined in Swagger
        """

        self._email = None
        self._first_name = None
        self._last_name = None
        self._address = None
        self._birthday = None
        self._nationality = None
        self._country_of_residence = None
        self._occupation = None
        self._income_range = None
        self._tag = None

        if email is not None:
          self.email = email
        if first_name is not None:
          self.first_name = first_name
        if last_name is not None:
          self.last_name = last_name
        if address is not None:
          self.address = address
        if birthday is not None:
          self.birthday = birthday
        if nationality is not None:
          self.nationality = nationality
        if country_of_residence is not None:
          self.country_of_residence = country_of_residence
        if occupation is not None:
          self.occupation = occupation
        if income_range is not None:
          self.income_range = income_range
        if tag is not None:
          self.tag = tag

    @property
    def email(self):
        """
        Gets the email of this UserNaturalPut.
        The user's email address - must be a valid email

        :return: The email of this UserNaturalPut.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserNaturalPut.
        The user's email address - must be a valid email

        :param email: The email of this UserNaturalPut.
        :type: str
        """

        self._email = email

    @property
    def first_name(self):
        """
        Gets the first_name of this UserNaturalPut.
        The name of the user

        :return: The first_name of this UserNaturalPut.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this UserNaturalPut.
        The name of the user

        :param first_name: The first_name of this UserNaturalPut.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this UserNaturalPut.
        The last name of the user

        :return: The last_name of this UserNaturalPut.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this UserNaturalPut.
        The last name of the user

        :param last_name: The last_name of this UserNaturalPut.
        :type: str
        """

        self._last_name = last_name

    @property
    def address(self):
        """
        Gets the address of this UserNaturalPut.
        The address

        :return: The address of this UserNaturalPut.
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this UserNaturalPut.
        The address

        :param address: The address of this UserNaturalPut.
        :type: Address
        """

        self._address = address

    @property
    def birthday(self):
        """
        Gets the birthday of this UserNaturalPut.
        The date of birth of the user - be careful to set the right timezone (should be UTC) to avoid 00h becoming 23h (and hence interpreted as the day before)

        :return: The birthday of this UserNaturalPut.
        :rtype: int
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """
        Sets the birthday of this UserNaturalPut.
        The date of birth of the user - be careful to set the right timezone (should be UTC) to avoid 00h becoming 23h (and hence interpreted as the day before)

        :param birthday: The birthday of this UserNaturalPut.
        :type: int
        """

        self._birthday = birthday

    @property
    def nationality(self):
        """
        Gets the nationality of this UserNaturalPut.
        The user’s nationality. ISO 3166-1 alpha-2 format is expected

        :return: The nationality of this UserNaturalPut.
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """
        Sets the nationality of this UserNaturalPut.
        The user’s nationality. ISO 3166-1 alpha-2 format is expected

        :param nationality: The nationality of this UserNaturalPut.
        :type: str
        """
        allowed_values = ["NotSpecified", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "FI", "FJ", "FK", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "YE", "YT", "ZA", "ZM", "ZW"]
        if nationality not in allowed_values:
            raise ValueError(
                "Invalid value for `nationality` ({0}), must be one of {1}"
                .format(nationality, allowed_values)
            )

        self._nationality = nationality

    @property
    def country_of_residence(self):
        """
        Gets the country_of_residence of this UserNaturalPut.
        The user’s country of residence. ISO 3166-1 alpha-2 format is expected

        :return: The country_of_residence of this UserNaturalPut.
        :rtype: str
        """
        return self._country_of_residence

    @country_of_residence.setter
    def country_of_residence(self, country_of_residence):
        """
        Sets the country_of_residence of this UserNaturalPut.
        The user’s country of residence. ISO 3166-1 alpha-2 format is expected

        :param country_of_residence: The country_of_residence of this UserNaturalPut.
        :type: str
        """
        allowed_values = ["NotSpecified", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "FI", "FJ", "FK", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "YE", "YT", "ZA", "ZM", "ZW"]
        if country_of_residence not in allowed_values:
            raise ValueError(
                "Invalid value for `country_of_residence` ({0}), must be one of {1}"
                .format(country_of_residence, allowed_values)
            )

        self._country_of_residence = country_of_residence

    @property
    def occupation(self):
        """
        Gets the occupation of this UserNaturalPut.
        User’s occupation, ie. Work

        :return: The occupation of this UserNaturalPut.
        :rtype: str
        """
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        """
        Sets the occupation of this UserNaturalPut.
        User’s occupation, ie. Work

        :param occupation: The occupation of this UserNaturalPut.
        :type: str
        """

        self._occupation = occupation

    @property
    def income_range(self):
        """
        Gets the income_range of this UserNaturalPut.
        Could be only one of these values: 1 - for incomes &lt;18K€),2 - for incomes between 18 and 30K€, 3 - for incomes between 30 and 50K€, 4 - for incomes between 50 and 80K€, 5 - for incomes between 80 and 120K€, 6 - for incomes &gt;120K€

        :return: The income_range of this UserNaturalPut.
        :rtype: int
        """
        return self._income_range

    @income_range.setter
    def income_range(self, income_range):
        """
        Sets the income_range of this UserNaturalPut.
        Could be only one of these values: 1 - for incomes &lt;18K€),2 - for incomes between 18 and 30K€, 3 - for incomes between 30 and 50K€, 4 - for incomes between 50 and 80K€, 5 - for incomes between 80 and 120K€, 6 - for incomes &gt;120K€

        :param income_range: The income_range of this UserNaturalPut.
        :type: int
        """

        self._income_range = income_range

    @property
    def tag(self):
        """
        Gets the tag of this UserNaturalPut.
        Custom data that you can add to this item

        :return: The tag of this UserNaturalPut.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this UserNaturalPut.
        Custom data that you can add to this item

        :param tag: The tag of this UserNaturalPut.
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
        if not isinstance(other, UserNaturalPut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
