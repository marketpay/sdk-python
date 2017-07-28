# TransactionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debited_funds** | [**Money**](Money.md) | Information about the funds that are being debited | [optional] 
**credited_funds** | [**Money**](Money.md) | Details about the funds that are being credited (DebitedFunds – Fees &#x3D; CreditedFunds) | [optional] 
**fees** | [**Money**](Money.md) | Information about the fees that were taken by the client for this transaction (and were hence transferred to the Client&#39;s platform wallet) | [optional] 
**debited_wallet_id** | **str** | The ID of the wallet that was debited | [optional] 
**credited_wallet_id** | **str** | The ID of the wallet where money will be credited | [optional] 
**author_id** | **str** | A user&#39;s ID | [optional] 
**credited_user_id** | **str** | The user ID who was credited | [optional] 
**nature** | **str** | The nature of the transaction | [optional] 
**status** | **str** | The status of the transaction | [optional] 
**execution_date** | **int** | When the transaction happened | [optional] 
**result_code** | **str** | The result code | [optional] 
**result_message** | **str** | A verbal explanation of the ResultCode | [optional] 
**type** | **str** | The type of the transaction | [optional] 
**transaction_source** | **str** |  | [optional] 
**transaction_destination** | **str** |  | [optional] 
**id** | **str** | The item&#39;s ID | [optional] 
**creation_date** | **int** | When the item was created | [optional] 
**tag** | **str** | Custom data that you can add to this item | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


