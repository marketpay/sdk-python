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


class UserLegalResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, headquarters_address=None, legal_person_type=None, name=None, legal_representative_address=None, legal_representative_birthday=None, legal_representative_country_of_residence=None, legal_representative_nationality=None, legal_representative_email=None, legal_representative_first_name=None, legal_representative_last_name=None, legal_representative_proof_of_identity=None, statute=None, shareholder_declaration=None, proof_of_registration=None, person_type=None, email=None, kyc_level=None, id=None, creation_date=None, tag=None):
        """
        UserLegalResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'headquarters_address': 'Address',
            'legal_person_type': 'str',
            'name': 'str',
            'legal_representative_address': 'Address',
            'legal_representative_birthday': 'int',
            'legal_representative_country_of_residence': 'str',
            'legal_representative_nationality': 'str',
            'legal_representative_email': 'str',
            'legal_representative_first_name': 'str',
            'legal_representative_last_name': 'str',
            'legal_representative_proof_of_identity': 'str',
            'statute': 'str',
            'shareholder_declaration': 'str',
            'proof_of_registration': 'str',
            'person_type': 'str',
            'email': 'str',
            'kyc_level': 'str',
            'id': 'str',
            'creation_date': 'int',
            'tag': 'str'
        }

        self.attribute_map = {
            'headquarters_address': 'HeadquartersAddress',
            'legal_person_type': 'LegalPersonType',
            'name': 'Name',
            'legal_representative_address': 'LegalRepresentativeAddress',
            'legal_representative_birthday': 'LegalRepresentativeBirthday',
            'legal_representative_country_of_residence': 'LegalRepresentativeCountryOfResidence',
            'legal_representative_nationality': 'LegalRepresentativeNationality',
            'legal_representative_email': 'LegalRepresentativeEmail',
            'legal_representative_first_name': 'LegalRepresentativeFirstName',
            'legal_representative_last_name': 'LegalRepresentativeLastName',
            'legal_representative_proof_of_identity': 'LegalRepresentativeProofOfIdentity',
            'statute': 'Statute',
            'shareholder_declaration': 'ShareholderDeclaration',
            'proof_of_registration': 'ProofOfRegistration',
            'person_type': 'PersonType',
            'email': 'Email',
            'kyc_level': 'KYCLevel',
            'id': 'Id',
            'creation_date': 'CreationDate',
            'tag': 'Tag'
        }

        self._headquarters_address = headquarters_address
        self._legal_person_type = legal_person_type
        self._name = name
        self._legal_representative_address = legal_representative_address
        self._legal_representative_birthday = legal_representative_birthday
        self._legal_representative_country_of_residence = legal_representative_country_of_residence
        self._legal_representative_nationality = legal_representative_nationality
        self._legal_representative_email = legal_representative_email
        self._legal_representative_first_name = legal_representative_first_name
        self._legal_representative_last_name = legal_representative_last_name
        self._legal_representative_proof_of_identity = legal_representative_proof_of_identity
        self._statute = statute
        self._shareholder_declaration = shareholder_declaration
        self._proof_of_registration = proof_of_registration
        self._person_type = person_type
        self._email = email
        self._kyc_level = kyc_level
        self._id = id
        self._creation_date = creation_date
        self._tag = tag

    @property
    def headquarters_address(self):
        """
        Gets the headquarters_address of this UserLegalResponse.
        The address of the company’s headquarters

        :return: The headquarters_address of this UserLegalResponse.
        :rtype: Address
        """
        return self._headquarters_address

    @headquarters_address.setter
    def headquarters_address(self, headquarters_address):
        """
        Sets the headquarters_address of this UserLegalResponse.
        The address of the company’s headquarters

        :param headquarters_address: The headquarters_address of this UserLegalResponse.
        :type: Address
        """

        self._headquarters_address = headquarters_address

    @property
    def legal_person_type(self):
        """
        Gets the legal_person_type of this UserLegalResponse.
        The type of legal user

        :return: The legal_person_type of this UserLegalResponse.
        :rtype: str
        """
        return self._legal_person_type

    @legal_person_type.setter
    def legal_person_type(self, legal_person_type):
        """
        Sets the legal_person_type of this UserLegalResponse.
        The type of legal user

        :param legal_person_type: The legal_person_type of this UserLegalResponse.
        :type: str
        """
        allowed_values = ["BUSINESS", "ORGANIZATION", "SOLETRADER"]
        if legal_person_type not in allowed_values:
            raise ValueError(
                "Invalid value for `legal_person_type` ({0}), must be one of {1}"
                .format(legal_person_type, allowed_values)
            )

        self._legal_person_type = legal_person_type

    @property
    def name(self):
        """
        Gets the name of this UserLegalResponse.
        The name of the legal user

        :return: The name of this UserLegalResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserLegalResponse.
        The name of the legal user

        :param name: The name of this UserLegalResponse.
        :type: str
        """

        self._name = name

    @property
    def legal_representative_address(self):
        """
        Gets the legal_representative_address of this UserLegalResponse.
        The address of the company’s Legal representative person

        :return: The legal_representative_address of this UserLegalResponse.
        :rtype: Address
        """
        return self._legal_representative_address

    @legal_representative_address.setter
    def legal_representative_address(self, legal_representative_address):
        """
        Sets the legal_representative_address of this UserLegalResponse.
        The address of the company’s Legal representative person

        :param legal_representative_address: The legal_representative_address of this UserLegalResponse.
        :type: Address
        """

        self._legal_representative_address = legal_representative_address

    @property
    def legal_representative_birthday(self):
        """
        Gets the legal_representative_birthday of this UserLegalResponse.
        The date of birth of the company’s Legal representative person - be careful to set the right timezone (should be UTC) to avoid 00h becoming 23h (and hence interpreted as the day before)

        :return: The legal_representative_birthday of this UserLegalResponse.
        :rtype: int
        """
        return self._legal_representative_birthday

    @legal_representative_birthday.setter
    def legal_representative_birthday(self, legal_representative_birthday):
        """
        Sets the legal_representative_birthday of this UserLegalResponse.
        The date of birth of the company’s Legal representative person - be careful to set the right timezone (should be UTC) to avoid 00h becoming 23h (and hence interpreted as the day before)

        :param legal_representative_birthday: The legal_representative_birthday of this UserLegalResponse.
        :type: int
        """

        self._legal_representative_birthday = legal_representative_birthday

    @property
    def legal_representative_country_of_residence(self):
        """
        Gets the legal_representative_country_of_residence of this UserLegalResponse.
        The country of residence of the company’s Legal representative person

        :return: The legal_representative_country_of_residence of this UserLegalResponse.
        :rtype: str
        """
        return self._legal_representative_country_of_residence

    @legal_representative_country_of_residence.setter
    def legal_representative_country_of_residence(self, legal_representative_country_of_residence):
        """
        Sets the legal_representative_country_of_residence of this UserLegalResponse.
        The country of residence of the company’s Legal representative person

        :param legal_representative_country_of_residence: The legal_representative_country_of_residence of this UserLegalResponse.
        :type: str
        """
        allowed_values = ["NotSpecified", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "FI", "FJ", "FK", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "YE", "YT", "ZA", "ZM", "ZW"]
        if legal_representative_country_of_residence not in allowed_values:
            raise ValueError(
                "Invalid value for `legal_representative_country_of_residence` ({0}), must be one of {1}"
                .format(legal_representative_country_of_residence, allowed_values)
            )

        self._legal_representative_country_of_residence = legal_representative_country_of_residence

    @property
    def legal_representative_nationality(self):
        """
        Gets the legal_representative_nationality of this UserLegalResponse.
        The nationality of the company’s Legal representative person

        :return: The legal_representative_nationality of this UserLegalResponse.
        :rtype: str
        """
        return self._legal_representative_nationality

    @legal_representative_nationality.setter
    def legal_representative_nationality(self, legal_representative_nationality):
        """
        Sets the legal_representative_nationality of this UserLegalResponse.
        The nationality of the company’s Legal representative person

        :param legal_representative_nationality: The legal_representative_nationality of this UserLegalResponse.
        :type: str
        """
        allowed_values = ["NotSpecified", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR", "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "FI", "FJ", "FK", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT", "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK", "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "YE", "YT", "ZA", "ZM", "ZW"]
        if legal_representative_nationality not in allowed_values:
            raise ValueError(
                "Invalid value for `legal_representative_nationality` ({0}), must be one of {1}"
                .format(legal_representative_nationality, allowed_values)
            )

        self._legal_representative_nationality = legal_representative_nationality

    @property
    def legal_representative_email(self):
        """
        Gets the legal_representative_email of this UserLegalResponse.
        The email of the company’s Legal representative person - must be a valid

        :return: The legal_representative_email of this UserLegalResponse.
        :rtype: str
        """
        return self._legal_representative_email

    @legal_representative_email.setter
    def legal_representative_email(self, legal_representative_email):
        """
        Sets the legal_representative_email of this UserLegalResponse.
        The email of the company’s Legal representative person - must be a valid

        :param legal_representative_email: The legal_representative_email of this UserLegalResponse.
        :type: str
        """

        self._legal_representative_email = legal_representative_email

    @property
    def legal_representative_first_name(self):
        """
        Gets the legal_representative_first_name of this UserLegalResponse.
        The firstname of the company’s Legal representative person

        :return: The legal_representative_first_name of this UserLegalResponse.
        :rtype: str
        """
        return self._legal_representative_first_name

    @legal_representative_first_name.setter
    def legal_representative_first_name(self, legal_representative_first_name):
        """
        Sets the legal_representative_first_name of this UserLegalResponse.
        The firstname of the company’s Legal representative person

        :param legal_representative_first_name: The legal_representative_first_name of this UserLegalResponse.
        :type: str
        """

        self._legal_representative_first_name = legal_representative_first_name

    @property
    def legal_representative_last_name(self):
        """
        Gets the legal_representative_last_name of this UserLegalResponse.
        The lastname of the company’s Legal representative person

        :return: The legal_representative_last_name of this UserLegalResponse.
        :rtype: str
        """
        return self._legal_representative_last_name

    @legal_representative_last_name.setter
    def legal_representative_last_name(self, legal_representative_last_name):
        """
        Sets the legal_representative_last_name of this UserLegalResponse.
        The lastname of the company’s Legal representative person

        :param legal_representative_last_name: The legal_representative_last_name of this UserLegalResponse.
        :type: str
        """

        self._legal_representative_last_name = legal_representative_last_name

    @property
    def legal_representative_proof_of_identity(self):
        """
        Gets the legal_representative_proof_of_identity of this UserLegalResponse.
        Legal Representative Proof Of Identity

        :return: The legal_representative_proof_of_identity of this UserLegalResponse.
        :rtype: str
        """
        return self._legal_representative_proof_of_identity

    @legal_representative_proof_of_identity.setter
    def legal_representative_proof_of_identity(self, legal_representative_proof_of_identity):
        """
        Sets the legal_representative_proof_of_identity of this UserLegalResponse.
        Legal Representative Proof Of Identity

        :param legal_representative_proof_of_identity: The legal_representative_proof_of_identity of this UserLegalResponse.
        :type: str
        """

        self._legal_representative_proof_of_identity = legal_representative_proof_of_identity

    @property
    def statute(self):
        """
        Gets the statute of this UserLegalResponse.
        Statute

        :return: The statute of this UserLegalResponse.
        :rtype: str
        """
        return self._statute

    @statute.setter
    def statute(self, statute):
        """
        Sets the statute of this UserLegalResponse.
        Statute

        :param statute: The statute of this UserLegalResponse.
        :type: str
        """

        self._statute = statute

    @property
    def shareholder_declaration(self):
        """
        Gets the shareholder_declaration of this UserLegalResponse.
        Shareholder declaration

        :return: The shareholder_declaration of this UserLegalResponse.
        :rtype: str
        """
        return self._shareholder_declaration

    @shareholder_declaration.setter
    def shareholder_declaration(self, shareholder_declaration):
        """
        Sets the shareholder_declaration of this UserLegalResponse.
        Shareholder declaration

        :param shareholder_declaration: The shareholder_declaration of this UserLegalResponse.
        :type: str
        """

        self._shareholder_declaration = shareholder_declaration

    @property
    def proof_of_registration(self):
        """
        Gets the proof_of_registration of this UserLegalResponse.
        Proof of registration

        :return: The proof_of_registration of this UserLegalResponse.
        :rtype: str
        """
        return self._proof_of_registration

    @proof_of_registration.setter
    def proof_of_registration(self, proof_of_registration):
        """
        Sets the proof_of_registration of this UserLegalResponse.
        Proof of registration

        :param proof_of_registration: The proof_of_registration of this UserLegalResponse.
        :type: str
        """

        self._proof_of_registration = proof_of_registration

    @property
    def person_type(self):
        """
        Gets the person_type of this UserLegalResponse.
        Type of user

        :return: The person_type of this UserLegalResponse.
        :rtype: str
        """
        return self._person_type

    @person_type.setter
    def person_type(self, person_type):
        """
        Sets the person_type of this UserLegalResponse.
        Type of user

        :param person_type: The person_type of this UserLegalResponse.
        :type: str
        """
        allowed_values = ["Natural", "Legal"]
        if person_type not in allowed_values:
            raise ValueError(
                "Invalid value for `person_type` ({0}), must be one of {1}"
                .format(person_type, allowed_values)
            )

        self._person_type = person_type

    @property
    def email(self):
        """
        Gets the email of this UserLegalResponse.
        The user's email address - must be a valid email

        :return: The email of this UserLegalResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserLegalResponse.
        The user's email address - must be a valid email

        :param email: The email of this UserLegalResponse.
        :type: str
        """

        self._email = email

    @property
    def kyc_level(self):
        """
        Gets the kyc_level of this UserLegalResponse.
        

        :return: The kyc_level of this UserLegalResponse.
        :rtype: str
        """
        return self._kyc_level

    @kyc_level.setter
    def kyc_level(self, kyc_level):
        """
        Sets the kyc_level of this UserLegalResponse.
        

        :param kyc_level: The kyc_level of this UserLegalResponse.
        :type: str
        """
        allowed_values = ["NotSpecified", "LIGHT", "REGULAR"]
        if kyc_level not in allowed_values:
            raise ValueError(
                "Invalid value for `kyc_level` ({0}), must be one of {1}"
                .format(kyc_level, allowed_values)
            )

        self._kyc_level = kyc_level

    @property
    def id(self):
        """
        Gets the id of this UserLegalResponse.
        The item's ID

        :return: The id of this UserLegalResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserLegalResponse.
        The item's ID

        :param id: The id of this UserLegalResponse.
        :type: str
        """

        self._id = id

    @property
    def creation_date(self):
        """
        Gets the creation_date of this UserLegalResponse.
        When the item was created

        :return: The creation_date of this UserLegalResponse.
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """
        Sets the creation_date of this UserLegalResponse.
        When the item was created

        :param creation_date: The creation_date of this UserLegalResponse.
        :type: int
        """

        self._creation_date = creation_date

    @property
    def tag(self):
        """
        Gets the tag of this UserLegalResponse.
        Custom data that you can add to this item

        :return: The tag of this UserLegalResponse.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this UserLegalResponse.
        Custom data that you can add to this item

        :param tag: The tag of this UserLegalResponse.
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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
