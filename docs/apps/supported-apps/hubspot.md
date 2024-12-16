# HubSpot

Integry supports a number of triggers and actions of HubSpot.

#### Triggers <a href="#h_01hr556ap5m0d97s0v2hv9bk41" id="h_01hr556ap5m0d97s0v2hv9bk41"></a>

| **Name**                  | **Type** | **Description**                                                   |
| ------------------------- | -------- | ----------------------------------------------------------------- |
| Contact Updated in a List | Polling  | Triggers when an existing contact is updated in a list            |
| Contact Added to a List   | Polling  | Triggers when a contact is added to a list                        |
| Contact Created           | Instant  | Triggers when a new contact is created                            |
| Contact Created/Updated   | Polling  | Triggers when a contact is created or updated                     |
| Quote Created/Updated     | Polling  | Triggers when a new quote is created or existing quote is updated |

For more, please see [Hubspot API docs](https://developers.hubspot.com/docs/api/webhooks). If you're not sure how triggers work in Integry, go [here](https://docs.integry.ai/hc/en-us/articles/29484874325017).

#### Actions <a href="#h_01hr56vpze824xf8dyw4e604x7" id="h_01hr56vpze824xf8dyw4e604x7"></a>

| **Name**                 | **Method** | **Description**                                          |
| ------------------------ | ---------- | -------------------------------------------------------- |
| Delete Contact           |  DELETE    | Deletes an existing contact                              |
| Unsubscribe Contact      | PATCH      | Unsubscribes a contact from all emails                   |
| Create Email Template    | POST       | Creates a new email template                             |
| Get Contact              | GET        | Fetches the details of a contact                         |
| Create Contact           | POST       | Creates a new contact                                    |
| Update Contact           | PATCH      | Updates an existing contact                              |
| Update Email Template    | PATCH      | Updates an existing email template                       |
| Bulk Contact Create      | POST       | Create contacts in bulk inside your account              |
| Bulk List Addition       | POST       | Add contacts into a list in bulk                         |
| Create Deal              | POST       | Creates a new deal                                       |
| Upsert Contact           | POST       | Creates a new HubSpot contact or updates an existing one |
| Remove Contact from List | POST       | Removes contact from list                                |
| Create Note Engagement   | POST       | Creates a new note engagement                            |
| Get Lifecycle Stages     | GET        | Fetches lifecycle stages of a contact                    |
| Search Company           |  POST      | Searches a company by search criteria                    |
| Update Deal              | PATCH      | Updates an existing deal                                 |
| Delete Deal              | DELETE     | Deletes an existing deal                                 |
| Get Deal                 | GET        | Fetches a specific deal by ID                            |
| Create Quote             | POST       | Creates a new quote                                      |
| Create Line Item         | POST       | Creates a new line item                                  |
| Get Quote Details        | GET        | Fetches details of a quote                               |
| Get Line Item Details    | GET        | Fetches details of a line item                           |
| Batch Read Line Items    | POST       | Reads a batch of line items                              |
| Get Quote                | GET        | Fetches details of a quote                               |

For more, please see [Hubspot API docs](https://developers.hubspot.com/docs/api/crm/contacts#endpoint?spec=POST-/crm/v3/objects/contacts).

#### Authorization <a href="#h_01hr556ap450c8s3d5hf8vc37f" id="h_01hr556ap450c8s3d5hf8vc37f"></a>

Your users will login to Hubspot via OAuth 2.0 using Integry's developer app. You can [replace it](https://docs.integry.ai/hc/en-us/articles/10887314172441) by [setting up your own](https://developers.hubspot.com/docs/api/oauth-quickstart-guide).\
