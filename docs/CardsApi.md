# swagger_client.CardsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cards_get**](CardsApi.md#cards_get) | **GET** /v2.01/Cards/{CardId} | View a Card
[**cards_get_list**](CardsApi.md#cards_get_list) | **GET** /v2.01/Cards | 
[**cards_put**](CardsApi.md#cards_put) | **PUT** /v2.01/Cards/{CardId} | Deactivate a Card


# **cards_get**
> CardResponse cards_get(card_id)

View a Card

In order to save cards, the next methods are currently available:              - Redsys Payment: Set the value of the SaveCard to true.              - Redsys Preauthorization: Set the value of the SaveCard to true.              In order to use previously saved cards, the next methods are currently available:              - Redsys Payment: Set the value of CardId. The card must belong to the user that owns the wallet where the payment will be credited.              - Redsys Preauthorization: Set the value of CardId. The card must belong to the user that owns the wallet where the payment will be credited once the preauthorization is confirmed.

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
api_instance = swagger_client.CardsApi()
card_id = 789 # int | The Id of a card

try: 
    # View a Card
    api_response = api_instance.cards_get(card_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardsApi->cards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **int**| The Id of a card | 

### Return type

[**CardResponse**](CardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_get_list**
> ResponseListCardResponse cards_get_list(page=page, per_page=per_page)



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
api_instance = swagger_client.CardsApi()
page = 56 # int |  (optional)
per_page = 56 # int |  (optional)

try: 
    api_response = api_instance.cards_get_list(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardsApi->cards_get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**ResponseListCardResponse**](ResponseListCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cards_put**
> CardResponse cards_put(card_id, card=card)

Deactivate a Card

Note that once deactivated, a card can't be reactivated afterwards

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
api_instance = swagger_client.CardsApi()
card_id = 789 # int | The Id of a card
card = swagger_client.CardPut() # CardPut | Card Object params (optional)

try: 
    # Deactivate a Card
    api_response = api_instance.cards_put(card_id, card=card)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CardsApi->cards_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **int**| The Id of a card | 
 **card** | [**CardPut**](CardPut.md)| Card Object params | [optional] 

### Return type

[**CardResponse**](CardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

