# swagger_client.TransfersApi

All URIs are relative to *https://localhost/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transfers_get**](TransfersApi.md#transfers_get) | **GET** /v2.01/Transfers/{TransferId} | View a Transfer
[**transfers_get_list**](TransfersApi.md#transfers_get_list) | **GET** /v2.01/Transfers | 
[**transfers_post**](TransfersApi.md#transfers_post) | **POST** /v2.01/Transfers | Create a Transfer


# **transfers_get**
> TransferResponse transfers_get(transfer_id)

View a Transfer

A Transfer is a request to relocate e-money from one wallet to another wallet.

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
api_instance = swagger_client.TransfersApi()
transfer_id = 789 # int | The Id of a transfer

try: 
    # View a Transfer
    api_response = api_instance.transfers_get(transfer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->transfers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_id** | **int**| The Id of a transfer | 

### Return type

[**TransferResponse**](TransferResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfers_get_list**
> ResponseListTransferResponse transfers_get_list(page=page, per_page=per_page)



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
api_instance = swagger_client.TransfersApi()
page = 56 # int |  (optional)
per_page = 56 # int |  (optional)

try: 
    api_response = api_instance.transfers_get_list(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->transfers_get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**ResponseListTransferResponse**](ResponseListTransferResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfers_post**
> TransferResponse transfers_post(transfer=transfer)

Create a Transfer



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
api_instance = swagger_client.TransfersApi()
transfer = swagger_client.TransferPost() # TransferPost | Transfer Object params (optional)

try: 
    # Create a Transfer
    api_response = api_instance.transfers_post(transfer=transfer)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->transfers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer** | [**TransferPost**](TransferPost.md)| Transfer Object params | [optional] 

### Return type

[**TransferResponse**](TransferResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

