# RedsysPayByWebPost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** | Custom data that you can add to this item | [optional] 
**save_card** | **bool** | Whether to save or not the card for future use. SaveCard and CardId are mutually exclusive | [optional] 
**card_id** | **str** | The id of a previous saved card. SaveCard and CardId are mutually exclusive | [optional] 
**credited_wallet_id** | **str** | The ID of the wallet where money will be credited | 
**statement_descriptor** | **str** | A custom description to appear on the user&#39;s bank statement. It can be up to 10 characters long, and can only include alphanumeric characters or spaces | [optional] 
**success_url** | **str** | Dirección (relativa a la tienda) a la que redirigirá cuando se haya completado el pago. | 
**url_ok** | **str** | Url to redirect the browser in case the payment is completed successfully | [optional] 
**cancel_url** | **str** | Dirección (relativa a la tienda) a la que redirigirá en caso de error en el pago. | 
**url_ko** | **str** | Url to redirect the browser in case the payment is not completed successfully | [optional] 
**debited_funds** | [**Money**](Money.md) | Information about the funds that are being debited | 
**fees** | [**Money**](Money.md) | Information about the fees that were taken by the client for this transaction (and were hence transferred to the Client&#39;s platform wallet) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

