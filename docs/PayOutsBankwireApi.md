# swagger_client.PayOutsBankwireApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pay_outs_bankwire_get**](PayOutsBankwireApi.md#pay_outs_bankwire_get) | **GET** /v2.01/PayOutsBankwire/payments/{PayOutId} | View a Bankwire PayOut
[**pay_outs_bankwire_post**](PayOutsBankwireApi.md#pay_outs_bankwire_post) | **POST** /v2.01/PayOutsBankwire/payments/direct | Create a Bankwire PayOut


# **pay_outs_bankwire_get**
> PayOutBankwireResponse pay_outs_bankwire_get(pay_out_id)

View a Bankwire PayOut

View a Bankwire PayOut

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
api_instance = swagger_client.PayOutsBankwireApi()
pay_out_id = 789 # int | The Id of a payment

try: 
    # View a Bankwire PayOut
    api_response = api_instance.pay_outs_bankwire_get(pay_out_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayOutsBankwireApi->pay_outs_bankwire_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_out_id** | **int**| The Id of a payment | 

### Return type

[**PayOutBankwireResponse**](PayOutBankwireResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_outs_bankwire_post**
> PayOutBankwireResponse pay_outs_bankwire_post(bankwire_pay_out=bankwire_pay_out)

Create a Bankwire PayOut

Create a Bankwire PayOut.

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
api_instance = swagger_client.PayOutsBankwireApi()
bankwire_pay_out = swagger_client.PayOutBankwirePost() # PayOutBankwirePost | Redsys PayIn Request Object params (optional)

try: 
    # Create a Bankwire PayOut
    api_response = api_instance.pay_outs_bankwire_post(bankwire_pay_out=bankwire_pay_out)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayOutsBankwireApi->pay_outs_bankwire_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankwire_pay_out** | [**PayOutBankwirePost**](PayOutBankwirePost.md)| Redsys PayIn Request Object params | [optional] 

### Return type

[**PayOutBankwireResponse**](PayOutBankwireResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

