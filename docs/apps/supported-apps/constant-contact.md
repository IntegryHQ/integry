# Constant Contact

Integry supports a number of triggers and actions of Constant Contact.

### Authentication <a href="#h_01hr556ap450c8s3d5hf8vc37f" id="h_01hr556ap450c8s3d5hf8vc37f"></a>

Your users will login to Constant Contact via OAuth 2.0.

### Triggers <a href="#h_01hr556ap5m0d97s0v2hv9bk41" id="h_01hr556ap5m0d97s0v2hv9bk41"></a>

| **Name**                   | **Type** | **Description**                               |
| -------------------------- | -------- | --------------------------------------------- |
| **Email Campaign Created** | Polling  | Triggers when a new campaign is created       |
| Contact Created/Updated    | Polling  | Triggers when a contact is created or updated |

For more, please see [Constant Contact API docs](https://developer.constantcontact.com/api_reference/index.html).

### Actions <a href="#h_01hr56vpze824xf8dyw4e604x7" id="h_01hr56vpze824xf8dyw4e604x7"></a>

| **Name**                     | **Method** | **Description**                           |
| ---------------------------- | ---------- | ----------------------------------------- |
| Create Email Campaign        |  POST      | Creates a new email campaign              |
| Update Email Campaign's Name |  PATCH     | Updates an existing email campaign's name |
| Delete Email Campaign        | DELETE     | Deletes an existing email campaign        |
| Delete Contact               |  DELETE    | Deletes an existing contact               |
| Unsubscribe Contact          |  PUT       | Unsubscribes an existing contact          |
| Create Contact               | POST       | Creates a new contact                     |
| Update Contact               | PATCH      | Updates an existing contact               |
| Get Contact by ID            |  GET       | Fetches a contact details by ID           |
| Create Tag                   | POST       | Creates a new tag                         |

For more, please see [Constant Contact API docs](https://developer.constantcontact.com/api_reference/index.html).
