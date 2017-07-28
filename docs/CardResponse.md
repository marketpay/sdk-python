# CardResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The object owner&#39;s UserId | [optional] 
**expiration_date** | **str** | The expiry date of the card - must be in format MMYY | [optional] 
**alias** | **str** | A partially obfuscated version of the credit card number | [optional] 
**card_provider** | **str** | The provider of the card | [optional] 
**card_type** | **str** | The type of card | [optional] 
**country** | **str** | The Country where the bank account is held | [optional] 
**product** | **str** | The card product type | [optional] 
**bank_code** | **str** |  | [optional] 
**active** | **bool** | Whether the card is active or not | [optional] 
**currency** | **str** | The currency - should be ISO_4217 format | [optional] 
**validity** | **str** | Whether the card is valid or not. Once they process (or attempt to process) a payment with the card we are able to indicate if it is \&quot;valid\&quot; or \&quot;invalid\&quot;. If they didn’t process a payment yet the \&quot;Validity\&quot; stay at \&quot;unknown\&quot; | [optional] 
**id** | **str** | The item&#39;s ID | [optional] 
**creation_date** | **int** | When the item was created | [optional] 
**tag** | **str** | Custom data that you can add to this item | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


