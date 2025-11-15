---
title: Process C2C Convenience Store Shipments
description: Confirm orders, generate shipping label, print and dispatch, track logistics, and handle exceptions.
product:
  - EC
module:
  - Order
activ: operate
surfaces:
  - backend
devices: []
apis: []
type: tutorial
features:
  - C2C Delivery
tasks:
  - Shipping
  - Order Confirmation
  - Waybill Generation
  - Shipping Label Printing
  - Convenience Store Dispatch
  - Logistics Tracking
tnb: ""
plans: []
lang: en-US
sites:
  - TW
status: new
doc_next: ""
doc_previous: ""
tags:
  - C2C
difficulty: medium
sibs: []
wp_url:
  - https://www.cyberbiz.io/support/?p=980
  - https://www.cyberbiz.io/helpcenter/?p=6856
notes:
  - 關轉運送異常操作指示不同，一般版代客或請顧客重新下單，企業版告知客服處理。
  - add [[補印加印託運單|Reprint/Add Waybill]]
  - add [Convenience Store: Thermal Printing Waybills](https://www.cyberbiz.io/support/?p=39461)
  - Opt: Convenience store dispatch process refactor
  - add A6 熱感列印部分
---

# Process C2C Convenience Store Shipments 

:octicons-sparkles-fill-16:{ title="Applicable CYBERBIZ Extensions" } | CYBERBIZ PAYMENTS  

=== ":lucide-info: Important Notes"

	- Lost or misplaced labels can only be *reprinted within 5 days* of generation.  
	- Shipping labels are *time-sensitive*. To prevent automatic deletion, *dispatch the parcel within 5 days* of label generation.  
	- Once the parcel is collected by the logistics driver, *dispatch cancellation is not possible*.
	- Shipping fees are *not reimbursed* in cases of force majeure (e.g., natural disasters).


## Procedures
### Confirm Order
![](docs/assets/images/ec-check-order-status.png)

1. Log in to your CYBERBIZ admin, click **Orders > All Orders**.
2. Confirm whether the **Payment Status** of the order to be processed allows for shipping:
> **Cash on delivery:** Must be "Cash on Delivery".  
> **Pickup but unpaid:** Must be "Payment Received".

### Generate Shipping Label
??? warning "CYBER Coin Top-Up Requirement"
	- **Standard Plans:** Merchants must top up CYBER Coins. Insufficient balance blocks shipping label printing.  
	- **PLUS Plans:** No top-up needed; credits are automatically deducted during each billing cycle.

![](docs/assets/images/ec-download%20c2c%20shipping%20label%20and%20change%20status%20to%20shipped.png)

=== ":material-numeric-1-circle: Select Order(s)"
	1. In your CYBERBIZ admin, click **Orders → All Orders**.
	2. Select one or more orders that are [ready for shipping](#step-1-confirm-order).
	
	> To view more orders per page, use the **Display selector** at the bottom of the **Orders List**.

	??? note "Batch Operation Limitations"
		- Batch shipping is only supported for orders with the *same delivery method*.  
		- Recommended maximum: *20 orders* per batch to prevent shipping number generation failures.

=== ":material-numeric-2-circle: Download Label"

	1. Click **Actions > Download C2C Shipping Label and change status to 'Shipped'**.  
	2. The system will request a shipping number from the convenience store logistics center (~30 seconds[^3]) and generate a shipping label archive.  
    > If the system takes too long, refresh the page and select **Reprint** from **Actions**.
	
=== ":material-numeric-3-circle: Label Archive"

	1. After generating the shipping number, a compressed archive file is created.  
    > Delivery Status updates to **Shipped** in Orders List and **Shipped, Awaiting Logistics Pickup** in Order Details.  

	2. Download the archive. Check for browser pop-up blocking if download fails.  

	??? note "Files included in the shipping label archive"
		- **Shipping Label - Shipping Information:** Browser view, save as PDF if needed.  
		- **Shipping Details:** Product quantity and shipping address (no order amount).  
		- **Order Details:** Complete product content, amount, and delivery method.  
		- **Picking List:** For warehouse staff during order picking.
	
		![](https://www.cyberbiz.io/helpcenter/wp-content/uploads/%E8%B6%85%E5%95%86%E5%BA%97%E5%88%B0%E5%BA%97%E5%87%BA%E8%B2%A8-C2C06.png){ .screenshot }


### Step Print Shipping Label

??? warning "Shipping Label Expiry"
	After printing the shipping label and updating the status to Shipped:  
	
	- **Dispatch deadlines:** 7‑Eleven: 5 days, FamilyMart: 6 days, Hi‑Life: 7 days.  
	- Missed deadlines: Waybill automatically deleted; a new order must be placed (either on behalf of the customer or by the customer).

=== "Convenience Store Print"

	#### 7-Eleven
	Print at ibon machines using the **Delivery Code** (shipping number).
	
	![](../assets/images/ec-print%20shipping%20label-ibon-1.png)
	![](../assets/images/ec-print%20shipping%20label-ibon-2.png)
	
	#### FamilyMart
	Use FamiPort.  
	
	- Step 7 order amount:
	> Cash on Delivery: Enter full order amount.  
	> Prepaid/Pickup Only: Enter 0.
	
	![](../assets/images/ec-print%20shipping%20label-familymart.png)

=== "Self-Print"

	- Use A4 paper or label stickers ([Example](https://shopee.tw/%E3%80%90A4%E3%80%91A4%E7%A9%BA%E7%99%BD%E8%B2%BC%E7%B4%99-2%C3%972-%E8%B2%BC%E7%B4%99-A6%E8%87%AA%E9%BB%8F%E6%A8%99%E7%B1%A4%E8%B2%BC%E7%B4%99-A4%E6%A8%A1%E9%80%A0%E8%B2%BC%E7%B4%99-%E9%9B%BB%E8%85%A6%E6%A8%99%E7%B1%A4%E8%B2%BC%E7%B4%99-%E5%8F%AF%E9%9B%B7%E5%B0%84-%E5%99%B4%E5%A2%A8-1%E5%8C%85100%E5%BC%B5-10%E5%8C%85%E5%85%8D%E9%81%8B-i.24728499.2550119685)).  
	- Maximum: 4 labels per page (2x2). Use software conversion for continuous printers.  
	- Use laser printer for barcode clarity.  

	??? tip "Avoid Special Characters in Merchant Names"
		- Special characters in 7‑11 labels may cause order creation failure; system will auto-convert characters[^4].  
		- Failure may lead to parcel return; return shipping fees apply.
	    
    > For Hi-Life users, CYBER Coins temporarily deducted at print. If not dispatched within 14 days, coins refunded.

	<div class="grid cards" markdown>
	
	- ![](../assets/images/ec-shipping-label-a4.png){ title="A4" }
	
	</div>


### Dispatch at Convenience Store
Same-day dispatched parcels typically available for pickup *2 days later*. Some stores are excluded. (see [7-11 Excluded Store List](https://www.7-11.com.tw/form/store.pdf)). Certain stores (HSR, Taiwan Railways, campus stores) do not provide pickup.  

=== ":material-numeric-1-circle: Prepare the Parcel"

	- Longest side ≤ 45cm  
	- Length + width + height ≤ 105cm  
	- Weight ≤ 5kg
	
	??? info "Product Packaging Guidelines"
		1. Must have outer packaging, not exposed.
		2. Fragile items must not be dispatched; damage will be the responsibility of the merchant. If the item causes damage or stains to other merchants' products, the merchant will also bear full compensation responsibility.
		3. The product's seal must be securely sealed. If the product is exposed, it will not be accepted. Detachment, loss, or damage will be the responsibility of the merchant.
		4. PP bags (transparent packaging) should not be dispatched to enhance consumer privacy.
		5. Label barcodes and QR codes must not be bent or folded (which may prevent equipment from scanning properly for acceptance).
		6. Affix flat on the wider side (so the parcel can be transported stably on equipment).
		7. Label size cannot be scaled (affects scanning readability).
		8. Parcel size must be larger than the waybill (please use a carton or poly mailer for packaging to protect the product).
		9. Packaging must not be damaged (to prevent items from falling out or being missing).
	
		![](../assets/images/ec-packaging-exceptions.png)
	
	??? info "Prohibited Item List"
		1. Cash, bills, stocks, jewelry, precious metals
		2. Credit cards, ATM cards, tender documents
		3. Remains, memorial tablets, Buddha statues
		4. Animals and plants
		5. Identification documents (ID cards, passports, airplane tickets)
		6. Non-reproducible drafts, cassette tapes, magnetic disks
		7. Flammable, volatile, corrosive items
		8. Toxic, explosive, radioactive items, car/motorcycle batteries
		9. Dangerous items or items violating public order
		10. Items deemed unacceptable by the carrier
		11. Fragile items (glass, porcelain, jade, etc.)
		12. Chemicals, liquids
		13. Precision instruments (3C products with batteries, GPS)
		14. Legally restricted items for sale (tobacco, alcohol, condoms, adult toys, restricted books, etc.)

=== ":material-numeric-2-circle: Dispatch"

	1. Attach [printed shipping label](#step-3-print-shipping-label) on parcel.  
	2. Take parcel to store counter and complete dispatch.  
    > See official instructions for details:  
    > 
    > - [7-Eleven Parcel Dispatch Instructions](https://www.7-11.com.tw/service/accept.aspx)  
    > - [FamilyMart Parcel Dispatch Instructions](https://fmec.famiport.com.tw/FP_Entrance/Notice)  
	3. Verify Order Details shows status **Shipped (In Transit)[^6]**.

### Track Logistics and Notifications
#### Check Logistics Status
You can check the delivery progress directly on each logistics provider’s website:

-   [7-Eleven Logistics Tracking](https://eservice.7-11.com.tw/E-Tracking/search.aspx){ target="_blank" rel="noopener"}  
-  [FamilyMart Logistics Tracking](https://www.famiport.com.tw/distribution_search.asp?page=4){ target="_blank" rel="noopener"}  
- [Hi-Life Logistics Tracking](https://www.hilife.com.tw/serviceInfo_search.aspx){ target="_blank" rel="noopener"}

#### Pickup Notifications
When the product arrives at the convenience store, the Delivery Status updates to "Arrived at Store", and the system automatically sends a pickup SMS notification to the customer.

| Store | SMS Schedule |
|--------|---------------|
| **7-Eleven** | Day 1 and Day 4 after arrival |
| **FamilyMart** | Day 1 and Day 3 after arrival |
| **Hi-Life** | Day 1 and Day 3 after arrival |

Unclaimed parcels will be returned to the dispatch store; the system sends a return notification SMS to the sender.

## Troubleshooting
### Unclaimed Parcel Handling

??? warning "Parcel collection/pickup requires ID"  
	Parcels returned to the store require the recipient to *present valid identification* for collection.  **Do not enter a company name**, as this may prevent pickup.

- Parcels returned due to expiry: merchant *not responsible* for shipping fees.
- If a parcel is returned due to non-pickup, the sender receives an SMS notification.
- Unclaimed parcels remaining at the original store for *7 days* will be returned to the merchant’s address via cash-on-delivery using Dazhi-Tong, Reyi, or Hi-Life logistics.


![](docs/assets/images/ec-unclaimed-parcel-handling.en.png)

### Store Closure Handling

- **7-11:** CYBERBIZ sends a notification email. Contact the consumer within *2 days* of receiving the email, re-select a 7-11 store, and inform customer service for processing.  
- **Hi-Life:** CYBERBIZ sends a notification email. Contact the consumer within *2 days*, re-select a Hi-Life store, and inform customer service for processing.  
- **FamilyMart:** CYBERBIZ sends a notification email. Follow the instructions in the email for further actions.

??? example "Store Closure / Transfer Email Template"
    - `[CYBERBIZ x Merchant Name] Order #XXXX Dispatch Store Closure Notification`  
    - `[CYBERBIZ x Merchant Name] Order #XXXX Consumer Pickup Store Closure Notification`

### Delivery Exception

- Check [parcel status](#check-logistics-status) via store tracking.
- Contact CYBERBIZ Customer Service if issues persist.  
- Once a parcel has been collected by the logistics driver, *dispatch cancellation is not possible*.  
- In cases of force majeure (e.g., natural disasters causing delivery delays or interruptions), *shipping fees will not be reimbursed*.

## FAQ

??? quote "How long after shipping label generation should I dispatch?"
    It is recommended to complete dispatch within 5 days.


[^1]: Such as natural disasters leading to delivery delays or interruptions.

[^2]: Once updated to *Shipped*, shipping information and any order status cannot be modified.

[^3]: The time taken for the system to request shipping numbers from convenience store logistics centers varies depending on the number of orders.

[^4]: The system will automatically convert special characters to `_`. 

[^5]: Such as HSR stations, Taiwan Railways stations, and campus stores.

[^6]: The merchant has completed the shipping process, and the order package has entered the delivery phase.
