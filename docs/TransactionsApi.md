# swagger_client.TransactionsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactions_get_list**](TransactionsApi.md#transactions_get_list) | **GET** /v2.01/Transactions | View a Transaction


# **transactions_get_list**
> ResponseListTransactionResponse transactions_get_list(page=page, per_page=per_page, before_date=before_date, after_date=after_date)

View a Transaction

A Transaction is any movement of money

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
api_instance = swagger_client.TransactionsApi()
page = 56 # int |  (optional)
per_page = 56 # int |  (optional)
before_date = 789 # int |  (optional)
after_date = 789 # int |  (optional)

try: 
    # View a Transaction
    api_response = api_instance.transactions_get_list(page=page, per_page=per_page, before_date=before_date, after_date=after_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->transactions_get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **before_date** | **int**|  | [optional] 
 **after_date** | **int**|  | [optional] 

### Return type

[**ResponseListTransactionResponse**](ResponseListTransactionResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

