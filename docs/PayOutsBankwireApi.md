# swagger_client.PayOutsBankwireApi

All URIs are relative to *https://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pay_outs_bankwire_get**](PayOutsBankwireApi.md#pay_outs_bankwire_get) | **GET** /v2.01/PayOutsBankwire/bankwire/{id} | 
[**pay_outs_bankwire_post**](PayOutsBankwireApi.md#pay_outs_bankwire_post) | **POST** /v2.01/PayOutsBankwire/bankwire | 


# **pay_outs_bankwire_get**
> PayOutBankwireResponse pay_outs_bankwire_get(pay_in_id, id)



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
api_instance = swagger_client.PayOutsBankwireApi()
pay_in_id = 789 # int | 
id = 'id_example' # str | 

try: 
    api_response = api_instance.pay_outs_bankwire_get(pay_in_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayOutsBankwireApi->pay_outs_bankwire_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_in_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

[**PayOutBankwireResponse**](PayOutBankwireResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_outs_bankwire_post**
> PayOutBankwireResponse pay_outs_bankwire_post(bankwire_pay_in=bankwire_pay_in)



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
api_instance = swagger_client.PayOutsBankwireApi()
bankwire_pay_in = swagger_client.PayOutBankwirePost() # PayOutBankwirePost |  (optional)

try: 
    api_response = api_instance.pay_outs_bankwire_post(bankwire_pay_in=bankwire_pay_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayOutsBankwireApi->pay_outs_bankwire_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankwire_pay_in** | [**PayOutBankwirePost**](PayOutBankwirePost.md)|  | [optional] 

### Return type

[**PayOutBankwireResponse**](PayOutBankwireResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

