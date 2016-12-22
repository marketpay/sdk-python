# swagger_client.WalletsApi

All URIs are relative to *https://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wallets_get**](WalletsApi.md#wallets_get) | **GET** /v2.01/Wallets/{WalletId} | View a Wallet
[**wallets_get_transaction_list**](WalletsApi.md#wallets_get_transaction_list) | **GET** /v2.01/Wallets/{WalletId}/transactions | List a Wallet&#39;s Transactions
[**wallets_post**](WalletsApi.md#wallets_post) | **POST** /v2.01/Wallets | Create a Wallet
[**wallets_put**](WalletsApi.md#wallets_put) | **PUT** /v2.01/Wallets/{WalletId} | Update a Wallet


# **wallets_get**
> WalletResponse wallets_get(wallet_id)

View a Wallet

A Wallet is an object in which PayIns and Transfers from users are stored in order to collect money. You can pay into a Wallet, withdraw funds from a wallet or transfer funds from a Wallet to another Wallet.              Once a wallet is created, its Currency can not be changed

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.WalletsApi()
wallet_id = 789 # int | The Id of a wallet

try: 
    # View a Wallet
    api_response = api_instance.wallets_get(wallet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletsApi->wallets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **int**| The Id of a wallet | 

### Return type

[**WalletResponse**](WalletResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallets_get_transaction_list**
> list[TransactionResponse] wallets_get_transaction_list(wallet_id, page=page, per_page=per_page)

List a Wallet's Transactions



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.WalletsApi()
wallet_id = 789 # int | The Id of a wallet
page = 56 # int | The page number of results you wish to return (optional)
per_page = 56 # int | The number of results to return per page (optional)

try: 
    # List a Wallet's Transactions
    api_response = api_instance.wallets_get_transaction_list(wallet_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletsApi->wallets_get_transaction_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **int**| The Id of a wallet | 
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

# **wallets_post**
> WalletResponse wallets_post(wallet=wallet)

Create a Wallet



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.WalletsApi()
wallet = swagger_client.WalletPost() # WalletPost | Wallet Object params (optional)

try: 
    # Create a Wallet
    api_response = api_instance.wallets_post(wallet=wallet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletsApi->wallets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet** | [**WalletPost**](WalletPost.md)| Wallet Object params | [optional] 

### Return type

[**WalletResponse**](WalletResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **wallets_put**
> WalletResponse wallets_put(wallet_id, wallet=wallet)

Update a Wallet



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.WalletsApi()
wallet_id = 789 # int | The Id of a wallet
wallet = swagger_client.WalletPut() # WalletPut | Wallet Object params (optional)

try: 
    # Update a Wallet
    api_response = api_instance.wallets_put(wallet_id, wallet=wallet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WalletsApi->wallets_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_id** | **int**| The Id of a wallet | 
 **wallet** | [**WalletPut**](WalletPut.md)| Wallet Object params | [optional] 

### Return type

[**WalletResponse**](WalletResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

