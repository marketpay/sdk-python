# PreauthorizeResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debited_funds** | [**Money**](Money.md) | Information about the funds that are being debited | [optional] 
**status** | **str** | The status of the transaction | [optional] 
**execution_date** | **int** | When the transaction happened | [optional] 
**result_code** | **str** | The result code | [optional] 
**result_message** | **str** | A verbal explanation of the ResultCode | [optional] 
**execution_type** | **str** | The type of execution for the payin | [optional] 
**card_id** | **str** | The Id of the card saved, if any. | [optional] 
**statement_descriptor** | **str** | A custom description to appear on the user&#39;s bank statement. It can be up to 10 characters long, and can only include alphanumeric characters or spaces | [optional] 
**author_id** | **str** | A user&#39;s ID | [optional] 
**id** | **str** | The item&#39;s ID | [optional] 
**creation_date** | **int** | When the item was created | [optional] 
**tag** | **str** | Custom data that you can add to this item | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


