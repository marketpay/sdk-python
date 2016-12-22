# coding: utf-8

"""
    MarketPay API

    API for Smart Contracts and Payments

    OpenAPI spec version: v2.01
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.address import Address
from .models.bank_account_ca_post import BankAccountCaPost
from .models.bank_account_gb_post import BankAccountGbPost
from .models.bank_account_iban_post import BankAccountIbanPost
from .models.bank_account_other_post import BankAccountOtherPost
from .models.bank_account_response import BankAccountResponse
from .models.bank_account_response_ca import BankAccountResponseCa
from .models.bank_account_response_gb import BankAccountResponseGb
from .models.bank_account_response_iban import BankAccountResponseIban
from .models.bank_account_response_other import BankAccountResponseOther
from .models.bank_account_response_us import BankAccountResponseUs
from .models.bank_account_us_post import BankAccountUsPost
from .models.card_put import CardPut
from .models.card_response import CardResponse
from .models.custom_api_error_response import CustomApiErrorResponse
from .models.example_user_natural_post import ExampleUserNaturalPost
from .models.money import Money
from .models.pay_by_web_post import PayByWebPost
from .models.pay_by_web_response import PayByWebResponse
from .models.pay_ins_response import PayInsResponse
from .models.preauthorization_cancellation_post import PreauthorizationCancellationPost
from .models.preauthorization_cancellation_response import PreauthorizationCancellationResponse
from .models.preauthorization_confirmation_post import PreauthorizationConfirmationPost
from .models.preauthorization_confirmation_response import PreauthorizationConfirmationResponse
from .models.preauthorize_by_web_post import PreauthorizeByWebPost
from .models.preauthorize_by_web_response import PreauthorizeByWebResponse
from .models.preauthorize_response import PreauthorizeResponse
from .models.refund_post import RefundPost
from .models.refund_reason import RefundReason
from .models.refund_response import RefundResponse
from .models.transaction_response import TransactionResponse
from .models.transfer_post import TransferPost
from .models.transfer_response import TransferResponse
from .models.user_legal_post import UserLegalPost
from .models.user_legal_response import UserLegalResponse
from .models.user_natural_post import UserNaturalPost
from .models.user_natural_response import UserNaturalResponse
from .models.user_response import UserResponse
from .models.wallet_post import WalletPost
from .models.wallet_put import WalletPut
from .models.wallet_response import WalletResponse

# import apis into sdk package
from .apis.cards_api import CardsApi
from .apis.pay_ins_redsys_api import PayInsRedsysApi
from .apis.refunds_api import RefundsApi
from .apis.transfers_api import TransfersApi
from .apis.users_api import UsersApi
from .apis.wallets_api import WalletsApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
