# RedsysPreauthorizationConfirmationPost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** | Custom data that you can add to this item | [optional] 
**credited_wallet_id** | **str** | The ID of the wallet where money will be credited | [optional] 
**debited_funds** | [**Money**](Money.md) | Information about the funds that are being debited. This value must be equal o less than the value informed at the Preauthorization creation | [optional] 
**fees** | [**Money**](Money.md) | Information about the fees that were taken by the client for this transaction (and were hence transferred to the Client&#39;s platform wallet) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


