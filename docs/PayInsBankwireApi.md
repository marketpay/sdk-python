# swagger_client.PayInsBankwireApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pay_ins_bankwire_bankwire_get_payment**](PayInsBankwireApi.md#pay_ins_bankwire_bankwire_get_payment) | **GET** /v2.01/PayInsBankwire/payments/{PayInId} | View a Bankwire PayIn
[**pay_ins_bankwire_bankwire_payment_by_direct**](PayInsBankwireApi.md#pay_ins_bankwire_bankwire_payment_by_direct) | **POST** /v2.01/PayInsBankwire/payments/direct | Create a Bankwire PayIn


# **pay_ins_bankwire_bankwire_get_payment**
> PayInBankwireResponse pay_ins_bankwire_bankwire_get_payment(pay_in_id)

View a Bankwire PayIn

View a Bankwire PayIn

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
api_instance = swagger_client.PayInsBankwireApi()
pay_in_id = 789 # int | The Id of a payment

try: 
    # View a Bankwire PayIn
    api_response = api_instance.pay_ins_bankwire_bankwire_get_payment(pay_in_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsBankwireApi->pay_ins_bankwire_bankwire_get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_in_id** | **int**| The Id of a payment | 

### Return type

[**PayInBankwireResponse**](PayInBankwireResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_bankwire_bankwire_payment_by_direct**
> PayInBankwireResponse pay_ins_bankwire_bankwire_payment_by_direct(bankwire_pay_in=bankwire_pay_in)

Create a Bankwire PayIn

Create a Bankwire PayIn.

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
api_instance = swagger_client.PayInsBankwireApi()
bankwire_pay_in = swagger_client.PayInBankwirePost() # PayInBankwirePost | Redsys PayIn Request Object params (optional)

try: 
    # Create a Bankwire PayIn
    api_response = api_instance.pay_ins_bankwire_bankwire_payment_by_direct(bankwire_pay_in=bankwire_pay_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsBankwireApi->pay_ins_bankwire_bankwire_payment_by_direct: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bankwire_pay_in** | [**PayInBankwirePost**](PayInBankwirePost.md)| Redsys PayIn Request Object params | [optional] 

### Return type

[**PayInBankwireResponse**](PayInBankwireResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

