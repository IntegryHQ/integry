# Ontraport

Integry supports a number of triggers and actions of Ontraport.

### Authentication <a href="#h_01hr556ap450c8s3d5hf8vc37f" id="h_01hr556ap450c8s3d5hf8vc37f"></a>

Ontraport uses API key + secret authentication.

### Triggers <a href="#h_01hr556ap5m0d97s0v2hv9bk41" id="h_01hr556ap5m0d97s0v2hv9bk41"></a>

| **Name**         | **Type** | **Description**                              |
| ---------------- | -------- | -------------------------------------------- |
| Contact Created  | Webhook  | Triggers when a contact is created           |
| Product Created  | Polling  | Triggers when a product is created           |
| Deal Created     | Polling  | Triggers when a deal is created              |
| Company Created  | Polling  | Triggers when a company is created           |
| Campaign Created | Webhook  | Triggers when a campaign is created          |
| Product Deleted  | Polling  | Triggers when an existing product is deleted |
| Company Updated  | Polling  | Triggers when a company is updated           |
| Deal Updated     | Polling  | Triggers when a deal is updated              |
| Create Product   | Webhook  | Creates a new product                        |
| Update Product   | Webhook  | Updates an existing product                  |
| Delete Product   | Webhook  | Deletes an existing product                  |

For more, please see [Ontraport API docs](https://api.ontraport.com/doc/).

## Actions <a href="#h_01hr56vpze824xf8dyw4e604x7" id="h_01hr56vpze824xf8dyw4e604x7"></a>

| **Name**        | **Method** | **Description**                       |
| --------------- | ---------- | ------------------------------------- |
| Create Contact  | POST       | Creates a new contact in your account |
| Create Campaign | POST       | Creates a new campaign                |
| Create Company  | POST       | Creates a new company                 |
| Update Company  | PUT        | Updates an existing company           |
| Delete Contact  | DELETE     | Deletes an existing contact           |
| Update Contact  | PUT        | Updates an existing contact           |
| Create Deal     | POST       | Creates a new deal                    |
| Create Product  | POST       | Creates a new product                 |
| Update Product  | PUT        | Updates an existing product           |
| Delete Product  | DELETE     | Deletes an existing product           |

