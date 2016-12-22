# swagger_client.PayInsRedsysApi

All URIs are relative to *https://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pay_ins_redsys_get_payment**](PayInsRedsysApi.md#pay_ins_redsys_get_payment) | **GET** /v2.01/PayInsRedsys/payments/{PayInId} | View a Redsys payment
[**pay_ins_redsys_get_preauthorization**](PayInsRedsysApi.md#pay_ins_redsys_get_preauthorization) | **GET** /v2.01/PayInsRedsys/preauthorizations/{PreauthorizationId} | View a Redsys Preauthorization
[**pay_ins_redsys_post_pay_by_web**](PayInsRedsysApi.md#pay_ins_redsys_post_pay_by_web) | **POST** /v2.01/PayInsRedsys/payments/web | Create a Redsys PayIn Request
[**pay_ins_redsys_post_preauthorization_cancellation**](PayInsRedsysApi.md#pay_ins_redsys_post_preauthorization_cancellation) | **POST** /v2.01/PayInsRedsys/preauthorizations/{PreauthorizationId}/cancellation | Cancels a Preauthorization
[**pay_ins_redsys_post_preauthorization_confirmation**](PayInsRedsysApi.md#pay_ins_redsys_post_preauthorization_confirmation) | **POST** /v2.01/PayInsRedsys/preauthorizations/{PreauthorizationId}/confirmation | Confirms a Preauthorization
[**pay_ins_redsys_post_preauthorize_by_web**](PayInsRedsysApi.md#pay_ins_redsys_post_preauthorize_by_web) | **POST** /v2.01/PayInsRedsys/preauthorizations/web | Create a Redsys Preauthorization Request
[**pay_ins_redsys_post_refund**](PayInsRedsysApi.md#pay_ins_redsys_post_refund) | **POST** /v2.01/PayInsRedsys/payments/{PayInId}/refunds | Create a Redsys Payment Refund


# **pay_ins_redsys_get_payment**
> PayInsResponse pay_ins_redsys_get_payment(pay_in_id)

View a Redsys payment



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
api_instance = swagger_client.PayInsRedsysApi()
pay_in_id = 789 # int | The Id of a payment

try: 
    # View a Redsys payment
    api_response = api_instance.pay_ins_redsys_get_payment(pay_in_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsRedsysApi->pay_ins_redsys_get_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_in_id** | **int**| The Id of a payment | 

### Return type

[**PayInsResponse**](PayInsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_redsys_get_preauthorization**
> PreauthorizeResponse pay_ins_redsys_get_preauthorization(preauthorization_id)

View a Redsys Preauthorization



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
api_instance = swagger_client.PayInsRedsysApi()
preauthorization_id = 789 # int | The Id of a Redsys Preauthorization

try: 
    # View a Redsys Preauthorization
    api_response = api_instance.pay_ins_redsys_get_preauthorization(preauthorization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsRedsysApi->pay_ins_redsys_get_preauthorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preauthorization_id** | **int**| The Id of a Redsys Preauthorization | 

### Return type

[**PreauthorizeResponse**](PreauthorizeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_redsys_post_pay_by_web**
> PayByWebResponse pay_ins_redsys_post_pay_by_web(redsys_pay_in=redsys_pay_in)

Create a Redsys PayIn Request

Prepares a payment on Redsys. The data returned is used to show the Redsys interface to the user.  Once the payment is done, the user will be redirected to one of UrlOk or UrlKo passed parameters.  In order to redirect the user, a Post request with Content-Type of application/x-www-form-urlencoded must be executed from the user's browser.  Below there is an example of a request where the params surrounded by curly braces have to be replaced with the response's params.  curl -X POST -H \"Content-Type: application/x-www-form-urlencoded\" -H \"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\" -H \"Cache-Control: no-cache\" -H \"Postman-Token: c313f10b-0de1-227e-53d2-f721f25cd79d\" -d 'Ds_SignatureVersion={Ds_SignatureVersion}&amp;Ds_MerchantParameters={Ds_MerchantParameters}&amp;Ds_Signature={Ds_Signature}' \"{Url}\"

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
api_instance = swagger_client.PayInsRedsysApi()
redsys_pay_in = swagger_client.PayByWebPost() # PayByWebPost | Redsys PayIn Request Object params (optional)

try: 
    # Create a Redsys PayIn Request
    api_response = api_instance.pay_ins_redsys_post_pay_by_web(redsys_pay_in=redsys_pay_in)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsRedsysApi->pay_ins_redsys_post_pay_by_web: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redsys_pay_in** | [**PayByWebPost**](PayByWebPost.md)| Redsys PayIn Request Object params | [optional] 

### Return type

[**PayByWebResponse**](PayByWebResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_redsys_post_preauthorization_cancellation**
> PreauthorizationCancellationResponse pay_ins_redsys_post_preauthorization_cancellation(preauthorization_id, preauthorization_cancellation=preauthorization_cancellation)

Cancels a Preauthorization



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
api_instance = swagger_client.PayInsRedsysApi()
preauthorization_id = 789 # int | The Id of a Redsys PreauthorizationCancellation
preauthorization_cancellation = swagger_client.PreauthorizationCancellationPost() # PreauthorizationCancellationPost | PreauthorizationCancellation Object params (optional)

try: 
    # Cancels a Preauthorization
    api_response = api_instance.pay_ins_redsys_post_preauthorization_cancellation(preauthorization_id, preauthorization_cancellation=preauthorization_cancellation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsRedsysApi->pay_ins_redsys_post_preauthorization_cancellation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preauthorization_id** | **int**| The Id of a Redsys PreauthorizationCancellation | 
 **preauthorization_cancellation** | [**PreauthorizationCancellationPost**](PreauthorizationCancellationPost.md)| PreauthorizationCancellation Object params | [optional] 

### Return type

[**PreauthorizationCancellationResponse**](PreauthorizationCancellationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_redsys_post_preauthorization_confirmation**
> PreauthorizationConfirmationResponse pay_ins_redsys_post_preauthorization_confirmation(preauthorization_id, preauthorization_confirmation=preauthorization_confirmation)

Confirms a Preauthorization



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
api_instance = swagger_client.PayInsRedsysApi()
preauthorization_id = 789 # int | The Id of a Redsys PreauthorizationConfirmation
preauthorization_confirmation = swagger_client.PreauthorizationConfirmationPost() # PreauthorizationConfirmationPost | PreauthorizationConfirmation Object params (optional)

try: 
    # Confirms a Preauthorization
    api_response = api_instance.pay_ins_redsys_post_preauthorization_confirmation(preauthorization_id, preauthorization_confirmation=preauthorization_confirmation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsRedsysApi->pay_ins_redsys_post_preauthorization_confirmation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preauthorization_id** | **int**| The Id of a Redsys PreauthorizationConfirmation | 
 **preauthorization_confirmation** | [**PreauthorizationConfirmationPost**](PreauthorizationConfirmationPost.md)| PreauthorizationConfirmation Object params | [optional] 

### Return type

[**PreauthorizationConfirmationResponse**](PreauthorizationConfirmationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_redsys_post_preauthorize_by_web**
> PreauthorizeByWebResponse pay_ins_redsys_post_preauthorize_by_web(redsys_preauthorization=redsys_preauthorization)

Create a Redsys Preauthorization Request

Prepares a preauthorization on Redsys. The data returned is used to show the Redsys interface to the user.  Once the preauthoriation is done, the user will be redirected to one of UrlOk or UrlKo passed parameters.  In order to redirect the user, a Post request with Content-Type of application/x-www-form-urlencoded must be executed from the user's browser.  Below there is an example of a request where the params surrounded by curly braces have to be replaced with the response's params.  curl -X POST -H \"Content-Type: application/x-www-form-urlencoded\" -H \"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\" -H \"Cache-Control: no-cache\" -H \"Postman-Token: c313f10b-0de1-227e-53d2-f721f25cd79d\" -d 'Ds_SignatureVersion={Ds_SignatureVersion}&amp;Ds_MerchantParameters={Ds_MerchantParameters}&amp;Ds_Signature={Ds_Signature}' \"{Url}\"

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
api_instance = swagger_client.PayInsRedsysApi()
redsys_preauthorization = swagger_client.PreauthorizeByWebPost() # PreauthorizeByWebPost | RedsysPreauthorization Object params (optional)

try: 
    # Create a Redsys Preauthorization Request
    api_response = api_instance.pay_ins_redsys_post_preauthorize_by_web(redsys_preauthorization=redsys_preauthorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsRedsysApi->pay_ins_redsys_post_preauthorize_by_web: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redsys_preauthorization** | [**PreauthorizeByWebPost**](PreauthorizeByWebPost.md)| RedsysPreauthorization Object params | [optional] 

### Return type

[**PreauthorizeByWebResponse**](PreauthorizeByWebResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_ins_redsys_post_refund**
> RefundResponse pay_ins_redsys_post_refund(pay_in_id, redsys_refund=redsys_refund)

Create a Redsys Payment Refund

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
api_instance = swagger_client.PayInsRedsysApi()
pay_in_id = 789 # int | The Id of a PayIn
redsys_refund = swagger_client.RefundPost() # RefundPost | Refund Object params (optional)

try: 
    # Create a Redsys Payment Refund
    api_response = api_instance.pay_ins_redsys_post_refund(pay_in_id, redsys_refund=redsys_refund)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayInsRedsysApi->pay_ins_redsys_post_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pay_in_id** | **int**| The Id of a PayIn | 
 **redsys_refund** | [**RefundPost**](RefundPost.md)| Refund Object params | [optional] 

### Return type

[**RefundResponse**](RefundResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

