# swagger_client.ShipmentSeurApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shipment_seur_seur_cancel_shipment**](ShipmentSeurApi.md#shipment_seur_seur_cancel_shipment) | **POST** /v2.01/ShipmentSeur/shipments/{ShipmentId}/cancellation | Cancels a shipment
[**shipment_seur_seur_create_shipment**](ShipmentSeurApi.md#shipment_seur_seur_create_shipment) | **POST** /v2.01/ShipmentSeur/shipments | Creates a shipment
[**shipment_seur_seur_get_shipment**](ShipmentSeurApi.md#shipment_seur_seur_get_shipment) | **GET** /v2.01/ShipmentSeur/shipments/{ShipmentId} | Cancels a shipment


# **shipment_seur_seur_cancel_shipment**
> SeurShipmentCancellationResponse shipment_seur_seur_cancel_shipment(shipment_id)

Cancels a shipment

Cancels a shipment

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
api_instance = swagger_client.ShipmentSeurApi()
shipment_id = 789 # int | The Id of a Shipment

try: 
    # Cancels a shipment
    api_response = api_instance.shipment_seur_seur_cancel_shipment(shipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentSeurApi->shipment_seur_seur_cancel_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**| The Id of a Shipment | 

### Return type

[**SeurShipmentCancellationResponse**](SeurShipmentCancellationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_seur_seur_create_shipment**
> SeurShipmentResponse shipment_seur_seur_create_shipment(shipment=shipment)

Creates a shipment

Creates a shipment

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
api_instance = swagger_client.ShipmentSeurApi()
shipment = swagger_client.SeurShipmentPost() # SeurShipmentPost | Seur Shipment Object params (optional)

try: 
    # Creates a shipment
    api_response = api_instance.shipment_seur_seur_create_shipment(shipment=shipment)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentSeurApi->shipment_seur_seur_create_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment** | [**SeurShipmentPost**](SeurShipmentPost.md)| Seur Shipment Object params | [optional] 

### Return type

[**SeurShipmentResponse**](SeurShipmentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/json-patch+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shipment_seur_seur_get_shipment**
> SeurShipmentResponse shipment_seur_seur_get_shipment(shipment_id)

Cancels a shipment

Cancels a shipment

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
api_instance = swagger_client.ShipmentSeurApi()
shipment_id = 789 # int | The Id of a Shipment

try: 
    # Cancels a shipment
    api_response = api_instance.shipment_seur_seur_get_shipment(shipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ShipmentSeurApi->shipment_seur_seur_get_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **int**| The Id of a Shipment | 

### Return type

[**SeurShipmentResponse**](SeurShipmentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

