# RedsysPreauthorizeByWebPost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** | Custom data that you can add to this item | [optional] 
**save_card** | **bool** | Whether to save or not the card for future use. SaveCard and CardId are mutually exclusive | [optional] 
**card_id** | **str** | The id of a previous saved card. SaveCard and CardId are mutually exclusive | [optional] 
**author_id** | **str** | A user&#39;s ID | [optional] 
**statement_descriptor** | **str** | A custom description to appear on the user&#39;s bank statement. It can be up to 10 characters long, and can only include alphanumeric characters or spaces | [optional] 
**success_url** | **str** | Dirección (relativa a la tienda) a la que redirigirá cuando se haya completado el pago. | 
**cancel_url** | **str** | Dirección (relativa a la tienda) a la que redirigirá en caso de error en el pago. | 
**debited_funds** | [**Money**](Money.md) | Information about the funds that are being debited | [optional] 
**language** | **str** | Valid values are ES, EN, CA, FR, DE, NL, IT, SV, PT, PL, GL and EU | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


