# swagger_client.UsersApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_get**](UsersApi.md#users_get) | **GET** /v2.01/Users/{UserId} | View a User
[**users_get_bank_account**](UsersApi.md#users_get_bank_account) | **GET** /v2.01/Users/{UserId}/bankaccounts/{BankAccountId} | View a Bank Account
[**users_get_bank_account_list**](UsersApi.md#users_get_bank_account_list) | **GET** /v2.01/Users/{UserId}/bankaccounts | List Bank Accounts for a User
[**users_get_card_list**](UsersApi.md#users_get_card_list) | **GET** /v2.01/Users/{UserId}/cards | List Cards for a User
[**users_get_legal**](UsersApi.md#users_get_legal) | **GET** /v2.01/Users/legal/{UserId} | View a Legal User
[**users_get_list**](UsersApi.md#users_get_list) | **GET** /v2.01/Users | List all Users
[**users_get_natural**](UsersApi.md#users_get_natural) | **GET** /v2.01/Users/natural/{UserId} | View a Natural User
[**users_get_transaction_list**](UsersApi.md#users_get_transaction_list) | **GET** /v2.01/Users/{UserId}/transactions | List Transactions for a User
[**users_get_wallet_list**](UsersApi.md#users_get_wallet_list) | **GET** /v2.01/Users/{UserId}/wallets | List Wallets for a User
[**users_post_bank_account_ca**](UsersApi.md#users_post_bank_account_ca) | **POST** /v2.01/Users/{UserId}/bankaccounts/CA | Create a CA BankAccount
[**users_post_bank_account_gb**](UsersApi.md#users_post_bank_account_gb) | **POST** /v2.01/Users/{UserId}/bankaccounts/GB | Create a GB BankAccount
[**users_post_bank_account_iban**](UsersApi.md#users_post_bank_account_iban) | **POST** /v2.01/Users/{UserId}/bankaccounts/IBAN | Create an IBAN BankAccount
[**users_post_bank_account_other**](UsersApi.md#users_post_bank_account_other) | **POST** /v2.01/Users/{UserId}/bankaccounts/OTHER | Create an OTHER BankAccount
[**users_post_bank_account_us**](UsersApi.md#users_post_bank_account_us) | **POST** /v2.01/Users/{UserId}/bankaccounts/US | Create an US BankAccount
[**users_post_legal**](UsersApi.md#users_post_legal) | **POST** /v2.01/Users/legal | Create a Legal User
[**users_post_natural**](UsersApi.md#users_post_natural) | **POST** /v2.01/Users/natural | Create a Natural User
[**users_put_legal**](UsersApi.md#users_put_legal) | **PUT** /v2.01/Users/legal/{UserId} | Update a Legal User
[**users_put_natural**](UsersApi.md#users_put_natural) | **PUT** /v2.01/Users/natural/{UserId} | Update a Natural User


# **users_get**
> UserResponse users_get(user_id)

View a User

A User can be \"Natural\" or \"Legal\". With a UserId, you are able to:              Fetch a user and get their details              List all the wallets of a user              Get all your users in a list

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 789 # int | The Id of a user

try: 
    # View a User
    api_response = api_instance.users_get(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a user | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_bank_account**
> BankAccountResponse users_get_bank_account(user_id, bank_account_id)

View a Bank Account



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 56 # int | The Id of a user
bank_account_id = 56 # int | The Id of a bank account

try: 
    # View a Bank Account
    api_response = api_instance.users_get_bank_account(user_id, bank_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_bank_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a user | 
 **bank_account_id** | **int**| The Id of a bank account | 

### Return type

[**BankAccountResponse**](BankAccountResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_bank_account_list**
> list[BankAccountResponse] users_get_bank_account_list(user_id, page=page, per_page=per_page)

List Bank Accounts for a User



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 789 # int | The Id of a user
page = 56 # int | The page number of results you wish to return (optional)
per_page = 56 # int | The number of results to return per page (optional)

try: 
    # List Bank Accounts for a User
    api_response = api_instance.users_get_bank_account_list(user_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_bank_account_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a user | 
 **page** | **int**| The page number of results you wish to return | [optional] 
 **per_page** | **int**| The number of results to return per page | [optional] 

### Return type

[**list[BankAccountResponse]**](BankAccountResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_card_list**
> list[CardResponse] users_get_card_list(user_id, page=page, per_page=per_page)

List Cards for a User



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 789 # int | The Id of a user
page = 56 # int | The page number of results you wish to return (optional)
per_page = 56 # int | The number of results to return per page (optional)

try: 
    # List Cards for a User
    api_response = api_instance.users_get_card_list(user_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_card_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a user | 
 **page** | **int**| The page number of results you wish to return | [optional] 
 **per_page** | **int**| The number of results to return per page | [optional] 

### Return type

[**list[CardResponse]**](CardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_legal**
> UserLegalResponse users_get_legal(user_id)

View a Legal User



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 789 # int | The Id of a legal user

try: 
    # View a Legal User
    api_response = api_instance.users_get_legal(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_legal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a legal user | 

### Return type

[**UserLegalResponse**](UserLegalResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_list**
> list[UserResponse] users_get_list(page=page, per_page=per_page)

List all Users



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
page = 56 # int | The page number of results you wish to return (optional)
per_page = 56 # int | The number of results to return per page (optional)

try: 
    # List all Users
    api_response = api_instance.users_get_list(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number of results you wish to return | [optional] 
 **per_page** | **int**| The number of results to return per page | [optional] 

### Return type

[**list[UserResponse]**](UserResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_natural**
> UserNaturalResponse users_get_natural(user_id)

View a Natural User



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 789 # int | The Id of a natural user

try: 
    # View a Natural User
    api_response = api_instance.users_get_natural(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_natural: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a natural user | 

### Return type

[**UserNaturalResponse**](UserNaturalResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_transaction_list**
> list[TransactionResponse] users_get_transaction_list(user_id, page=page, per_page=per_page)

List Transactions for a User



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 789 # int | The Id of a user
page = 56 # int | The page number of results you wish to return (optional)
per_page = 56 # int | The number of results to return per page (optional)

try: 
    # List Transactions for a User
    api_response = api_instance.users_get_transaction_list(user_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_transaction_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a user | 
 **page** | **int**| The page number of results you wish to return | [optional] 
 **per_page** | **int**| The number of results to return per page | [optional] 

### Return type

[**list[TransactionResponse]**](TransactionResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_wallet_list**
> list[WalletResponse] users_get_wallet_list(user_id, page=page, per_page=per_page)

List Wallets for a User



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 789 # int | The Id of a user
page = 56 # int | The page number of results you wish to return (optional)
per_page = 56 # int | The number of results to return per page (optional)

try: 
    # List Wallets for a User
    api_response = api_instance.users_get_wallet_list(user_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get_wallet_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a user | 
 **page** | **int**| The page number of results you wish to return | [optional] 
 **per_page** | **int**| The number of results to return per page | [optional] 

### Return type

[**list[WalletResponse]**](WalletResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post_bank_account_ca**
> BankAccountResponseCa users_post_bank_account_ca(user_id, bank_account_ca=bank_account_ca)

Create a CA BankAccount

In the case of CAD PayOut, the author (AuthorId) of the PayOut should have their address (Address for Natural Users or HeaquartersAddress for Legal Users) completed in their User object

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 789 # int | The Id of a user
bank_account_ca = swagger_client.BankAccountCaPost() # BankAccountCaPost | BankAccountCA Object params (optional)

try: 
    # Create a CA BankAccount
    api_response = api_instance.users_post_bank_account_ca(user_id, bank_account_ca=bank_account_ca)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_post_bank_account_ca: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a user | 
 **bank_account_ca** | [**BankAccountCaPost**](BankAccountCaPost.md)| BankAccountCA Object params | [optional] 

### Return type

[**BankAccountResponseCa**](BankAccountResponseCa.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post_bank_account_gb**
> BankAccountResponseGb users_post_bank_account_gb(user_id, bank_account_gb=bank_account_gb)

Create a GB BankAccount



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 789 # int | The Id of a user
bank_account_gb = swagger_client.BankAccountGbPost() # BankAccountGbPost |  (optional)

try: 
    # Create a GB BankAccount
    api_response = api_instance.users_post_bank_account_gb(user_id, bank_account_gb=bank_account_gb)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_post_bank_account_gb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a user | 
 **bank_account_gb** | [**BankAccountGbPost**](BankAccountGbPost.md)|  | [optional] 

### Return type

[**BankAccountResponseGb**](BankAccountResponseGb.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post_bank_account_iban**
> BankAccountResponseIban users_post_bank_account_iban(user_id, bank_account_iban=bank_account_iban)

Create an IBAN BankAccount



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 789 # int | The Id of a user
bank_account_iban = swagger_client.BankAccountIbanPost() # BankAccountIbanPost | BankAccountIBAN Object params (optional)

try: 
    # Create an IBAN BankAccount
    api_response = api_instance.users_post_bank_account_iban(user_id, bank_account_iban=bank_account_iban)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_post_bank_account_iban: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a user | 
 **bank_account_iban** | [**BankAccountIbanPost**](BankAccountIbanPost.md)| BankAccountIBAN Object params | [optional] 

### Return type

[**BankAccountResponseIban**](BankAccountResponseIban.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post_bank_account_other**
> BankAccountResponseOther users_post_bank_account_other(user_id, bank_account_other=bank_account_other)

Create an OTHER BankAccount



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 789 # int | The Id of a user
bank_account_other = swagger_client.BankAccountOtherPost() # BankAccountOtherPost |  (optional)

try: 
    # Create an OTHER BankAccount
    api_response = api_instance.users_post_bank_account_other(user_id, bank_account_other=bank_account_other)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_post_bank_account_other: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a user | 
 **bank_account_other** | [**BankAccountOtherPost**](BankAccountOtherPost.md)|  | [optional] 

### Return type

[**BankAccountResponseOther**](BankAccountResponseOther.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post_bank_account_us**
> BankAccountResponseUs users_post_bank_account_us(user_id, bank_account_us=bank_account_us)

Create an US BankAccount

In the case of USD PayOut, the author (AuthorId) of the PayOut should have their address (Address for Natural Users or HeaquartersAddress for Legal Users) completed in their User object.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 789 # int | The Id of a user
bank_account_us = swagger_client.BankAccountUsPost() # BankAccountUsPost | BankAccountUS Object params (optional)

try: 
    # Create an US BankAccount
    api_response = api_instance.users_post_bank_account_us(user_id, bank_account_us=bank_account_us)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_post_bank_account_us: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a user | 
 **bank_account_us** | [**BankAccountUsPost**](BankAccountUsPost.md)| BankAccountUS Object params | [optional] 

### Return type

[**BankAccountResponseUs**](BankAccountResponseUs.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post_legal**
> UserLegalResponse users_post_legal(user_legal=user_legal)

Create a Legal User

Note that the LegalRepresentativeBirthday field is a timestamp, but be careful to ensure that the time is midnight UTC (otherwise a local time can be understood as 23h UTC, and therefore rendering the wrong date which will present problems when needing to validate the KYC identity)

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_legal = swagger_client.UserLegalPost() # UserLegalPost | UserLegal Object params (optional)

try: 
    # Create a Legal User
    api_response = api_instance.users_post_legal(user_legal=user_legal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_post_legal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_legal** | [**UserLegalPost**](UserLegalPost.md)| UserLegal Object params | [optional] 

### Return type

[**UserLegalResponse**](UserLegalResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post_natural**
> UserNaturalResponse users_post_natural(user_natural=user_natural)

Create a Natural User

Note that the Birthday field is a timestamp, but be careful to ensure that the time is midnight UTC (otherwise a local time can be understood as 23h UTC, and therefore rendering the wrong date which will present problems when needing to validate the KYC identity)

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_natural = swagger_client.UserNaturalPost() # UserNaturalPost | UserNatural Object params (optional)

try: 
    # Create a Natural User
    api_response = api_instance.users_post_natural(user_natural=user_natural)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_post_natural: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_natural** | [**UserNaturalPost**](UserNaturalPost.md)| UserNatural Object params | [optional] 

### Return type

[**UserNaturalResponse**](UserNaturalResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_put_legal**
> UserLegalResponse users_put_legal(user_id, user_legal=user_legal)

Update a Legal User

Note that the LegalRepresentativeBirthday field is a timestamp, but be careful to ensure that the time is midnight UTC (otherwise a local time can be understood as 23h UTC, and therefore rendering the wrong date which will present problems when needing to validate the KYC identity)

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 789 # int | The Id of a user
user_legal = swagger_client.UserLegalPut() # UserLegalPut | UserLegal Object params (optional)

try: 
    # Update a Legal User
    api_response = api_instance.users_put_legal(user_id, user_legal=user_legal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_put_legal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a user | 
 **user_legal** | [**UserLegalPut**](UserLegalPut.md)| UserLegal Object params | [optional] 

### Return type

[**UserLegalResponse**](UserLegalResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_put_natural**
> UserNaturalResponse users_put_natural(user_id, user_natural=user_natural)

Update a Natural User

Note that the Birthday field is a timestamp, but be careful to ensure that the time is midnight UTC (otherwise a local time can be understood as 23h UTC, and therefore rendering the wrong date which will present problems when needing to validate the KYC identity)

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.UsersApi()
user_id = 789 # int | The Id of a user
user_natural = swagger_client.UserNaturalPut() # UserNaturalPut | UserNatural Object params (optional)

try: 
    # Update a Natural User
    api_response = api_instance.users_put_natural(user_id, user_natural=user_natural)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_put_natural: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| The Id of a user | 
 **user_natural** | [**UserNaturalPut**](UserNaturalPut.md)| UserNatural Object params | [optional] 

### Return type

[**UserNaturalResponse**](UserNaturalResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

