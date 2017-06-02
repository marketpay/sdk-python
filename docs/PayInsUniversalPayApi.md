# swagger_client.PayInsUniversalPayApi

All URIs are relative to *https://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pay_ins_universal_pay_universal_pay_get_payment**](PayInsUniversalPayApi.md#pay_ins_universal_pay_universal_pay_get_payment) | **GET** /v2.01/PayInsUniversalPay/payments/{PayInId} | View a UniversalPay payment
[**pay_ins_universal_pay_universal_pay_post_payment_by_web**](PayInsUniversalPayApi.md#pay_ins_universal_pay_universal_pay_post_payment_by_web) | **POST** /v2.01/PayInsUniversalPay/payments/web | Create a UniversalPay PayIn Request
[**pay_ins_universal_pay_universal_pay_post_refund**](PayInsUniversalPayApi.md#pay_ins_universal_pay_universal_pay_post_refund) | **POST** /v2.01/PayInsUniversalPay/payments/{PayInId}/refunds | Create a UniversalPay Payment Refund
[**pay_ins_universal_pay_universal_pay_save_card**](PayInsUniversalPayApi.md#pay_ins_universal_pay_universal_pay_save_card) | **POST** /v2.01/PayInsUniversalPay/cards | 


# **pay_ins_universal_pay_universal_pay_get_payment**
> UniversalPayPayInsResponse pay_ins_universal_pay_universal_pay_get_payment(pay_in_id)

View a UniversalPay payment



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
api_instance = swagger_client.PayInsUniversalPayApi()
pay_in_id = 789 # int | The Id of a payment

try: 
    # View a UniversalPay payment
    api_response = api_instance.pay_ins_universal_pay_universal_pay_get_payment(pay_in_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsUniversalPayApi->pay_ins_universal_pay_universal_pay_get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_in_id** | **int**| The Id of a payment | 

### Return type

[**UniversalPayPayInsResponse**](UniversalPayPayInsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_universal_pay_universal_pay_post_payment_by_web**
> UniversalPayPayByWebResponse pay_ins_universal_pay_universal_pay_post_payment_by_web(universal_pay_pay_in=universal_pay_pay_in)

Create a UniversalPay PayIn Request

Prepares a payment on UniversalPay. The data returned is used to show the UniversalPay interface to the user.  Once the payment is done, the user will be redirected to one of UrlOk or UrlKo passed parameters.  In order to redirect the user, a Post request with Content-Type of application/x-www-form-urlencoded must be executed from the user's browser.  Below there is an example of a request where the params surrounded by curly braces have to be replaced with the response's params.  curl -X POST -H \"Content-Type: application/x-www-form-urlencoded\" -H \"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\" -H \"Cache-Control: no-cache\" -H \"Postman-Token: c313f10b-0de1-227e-53d2-f721f25cd79d\" -d 'Ds_SignatureVersion={Ds_SignatureVersion}&amp;Ds_MerchantParameters={Ds_MerchantParameters}&amp;Ds_Signature={Ds_Signature}' \"{Url}\"

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
api_instance = swagger_client.PayInsUniversalPayApi()
universal_pay_pay_in = swagger_client.UniversalPayPayByWebPost() # UniversalPayPayByWebPost | UniversalPay PayIn Request Object params (optional)

try: 
    # Create a UniversalPay PayIn Request
    api_response = api_instance.pay_ins_universal_pay_universal_pay_post_payment_by_web(universal_pay_pay_in=universal_pay_pay_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsUniversalPayApi->pay_ins_universal_pay_universal_pay_post_payment_by_web: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **universal_pay_pay_in** | [**UniversalPayPayByWebPost**](UniversalPayPayByWebPost.md)| UniversalPay PayIn Request Object params | [optional] 

### Return type

[**UniversalPayPayByWebResponse**](UniversalPayPayByWebResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_universal_pay_universal_pay_post_refund**
> UniversalPayRefundResponse pay_ins_universal_pay_universal_pay_post_refund(pay_in_id, universal_pay_refund=universal_pay_refund)

Create a UniversalPay Payment Refund

A PayIn Refund is a request to reimburse a user on their payment card. The money which has already been paid will automatically go back to the user’s bank account.              Minimum amount to refund is 1€.              If you're doing a partial Refund, note that you can only refund the same amount on the same transaction once per day (this is to prevent unintended duplicate refunds). After 24h you can do another refund of the same amount on the same transaction. If it is a different amount on the same transaction, there is not this limit.              If you do not specify DebitedFunds and Fees parameters, it will automatically fully refund the PayIn. However if you do provide one or the other, you must provide both. Note that Fees must be negative if you wish to refund them - adding a positive value for the Fees is a way to charge your customers for the Refund (in the same way you might for a PayIn, Transfer or any other Transaction

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
api_instance = swagger_client.PayInsUniversalPayApi()
pay_in_id = 789 # int | The Id of a PayIn
universal_pay_refund = swagger_client.UniversalPayRefundPost() # UniversalPayRefundPost | Refund Object params (optional)

try: 
    # Create a UniversalPay Payment Refund
    api_response = api_instance.pay_ins_universal_pay_universal_pay_post_refund(pay_in_id, universal_pay_refund=universal_pay_refund)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsUniversalPayApi->pay_ins_universal_pay_universal_pay_post_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_in_id** | **int**| The Id of a PayIn | 
 **universal_pay_refund** | [**UniversalPayRefundPost**](UniversalPayRefundPost.md)| Refund Object params | [optional] 

### Return type

[**UniversalPayRefundResponse**](UniversalPayRefundResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_universal_pay_universal_pay_save_card**
> UniversalPayPayByWebResponse pay_ins_universal_pay_universal_pay_save_card(universal_pay_save_card=universal_pay_save_card)



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
api_instance = swagger_client.PayInsUniversalPayApi()
universal_pay_save_card = swagger_client.UniversalPayTokenRequestPost() # UniversalPayTokenRequestPost |  (optional)

try: 
    api_response = api_instance.pay_ins_universal_pay_universal_pay_save_card(universal_pay_save_card=universal_pay_save_card)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsUniversalPayApi->pay_ins_universal_pay_universal_pay_save_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **universal_pay_save_card** | [**UniversalPayTokenRequestPost**](UniversalPayTokenRequestPost.md)|  | [optional] 

### Return type

[**UniversalPayPayByWebResponse**](UniversalPayPayByWebResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

