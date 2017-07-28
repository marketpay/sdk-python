# UniversalPayTokenRequestPost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_funds** | [**Money**](Money.md) | Amount that will be charged to authorize the card. Default value is 1 euro. Authorizations with zero amount may be rejected by the credit card issuer and are not guaranteed to succeed. | [optional] 
**tag** | **str** | Custom data that you can add to this item | [optional] 
**credited_wallet_id** | **str** | The ID of the wallet where money will be credited | 
**secure_mode** | **str** |  | [optional] 
**success_url** | **str** | Url to redirect the browser in case the payment is completed successfully | [optional] 
**cancel_url** | **str** | Url to redirect the browser in case the payment is not completed successfully | [optional] 
**language** | **str** | Valid values are ES, EN, FR | [optional] 
**customer** | [**CustomerDetail**](CustomerDetail.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


