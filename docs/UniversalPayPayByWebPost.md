# UniversalPayPayByWebPost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debited_funds** | [**Money**](Money.md) | Information about the funds that are being debited | 
**fees** | [**Money**](Money.md) | Information about the fees that were taken by the client for this transaction (and were hence transferred to the Client&#39;s platform wallet) | 
**card_id** | **str** | The id of a previous saved card. SaveCard and CardId are mutually exclusive | [optional] 
**save_card** | **bool** | Whether to save or not the card for future use. SaveCard and CardId are mutually exclusive | [optional] 
**statement_descriptor** | **str** |  | 
**tag** | **str** | Custom data that you can add to this item | [optional] 
**credited_wallet_id** | **str** | The ID of the wallet where money will be credited | 
**secure_mode** | **str** |  | [optional] 
**success_url** | **str** | Url to redirect the browser in case the payment is completed successfully | [optional] 
**cancel_url** | **str** | Url to redirect the browser in case the payment is not completed successfully | [optional] 
**language** | **str** | Valid values are ES, EN, FR | [optional] 
**customer** | [**CustomerDetail**](CustomerDetail.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


