# swagger_client.PayOutsApi

All URIs are relative to *https://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pay_outs_get**](PayOutsApi.md#pay_outs_get) | **GET** /v2.01/PayOuts/bankwire/{id} | SwaggerDocSummary
[**pay_outs_post**](PayOutsApi.md#pay_outs_post) | **POST** /v2.01/PayOuts/bankwire | SwaggerDocSummary


# **pay_outs_get**
> PayOutBankWireResponse pay_outs_get(id)

SwaggerDocSummary

SwaggerDocDescription

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
api_instance = swagger_client.PayOutsApi()
id = 789 # int | SwaggerDocParameter

try: 
    # SwaggerDocSummary
    api_response = api_instance.pay_outs_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayOutsApi->pay_outs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| SwaggerDocParameter | 

### Return type

[**PayOutBankWireResponse**](PayOutBankWireResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pay_outs_post**
> PayOutBankWireResponse pay_outs_post(request=request)

SwaggerDocSummary

SwaggerDocDescription

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
api_instance = swagger_client.PayOutsApi()
request = swagger_client.PayOutBankWirePost() # PayOutBankWirePost | SwaggerDocParameter (optional)

try: 
    # SwaggerDocSummary
    api_response = api_instance.pay_outs_post(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayOutsApi->pay_outs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**PayOutBankWirePost**](PayOutBankWirePost.md)| SwaggerDocParameter | [optional] 

### Return type

[**PayOutBankWireResponse**](PayOutBankWireResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

