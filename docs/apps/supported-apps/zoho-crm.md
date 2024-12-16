# Zoho CRM

Integry supports a number of triggers and actions of Zoho CRM.

#### Triggers <a href="#h_01hr556ap5m0d97s0v2hv9bk41" id="h_01hr556ap5m0d97s0v2hv9bk41"></a>

| **Name**         | **Type** | **Description**                     |
| ---------------- | -------- | ----------------------------------- |
| Contact Created  | Polling  | Triggers when a contact is created  |
| Contact Updated  | Polling  | Triggers when a contact is updated  |
| Contact Deleted  | Polling  | Triggers when a contact is deleted  |
| Lead Created     | Polling  | Triggers when a lead is created     |
| Lead Updated     | Polling  | Triggers when a lead is updated     |
| Lead Deleted     | Polling  | Triggers when a lead is deleted     |
| Account Created  | Polling  | Triggers when an account is created |
| Account Updated  | Polling  | Triggers when an account is updated |
| Account Deleted  | Polling  | Triggers when an account is deleted |
| Task Created     | Polling  | Triggers when a task is created     |
| Task Updated     | Polling  | Triggers when a task is updated     |
| Task Deleted     | Polling  | Triggers when a task is deleted     |
| Deal Created     | Polling  | Triggers when a deal is created     |
| Deal Updated     | Polling  | Triggers when a deal is updated     |
| Deal Deleted     | Polling  | Triggers when a deal is deleted     |
| Meeting Created  | Polling  | Triggers when a meeting is created  |
| Meeting Updated  | Polling  | Triggers when a meeting is updated  |
| Meeting Deleted  | Polling  | Triggers when a meeting is deleted  |
| Campaign Created | Polling  | Triggers when a campaign is created |
| Campaign Updated | Polling  | Triggers when a campaign is updated |

For more, please see [Zoho API docs](https://www.zoho.com/crm/developer/docs/api/v3/). If you're not sure how triggers work in Integry, go [here](https://support.integry.io/hc/en-us/articles/29484874325017).

&#x20;

#### Actions <a href="#h_01hr56vpze824xf8dyw4e604x7" id="h_01hr56vpze824xf8dyw4e604x7"></a>

| **Name**                | **Method** | **Description**                                                     |
| ----------------------- | ---------- | ------------------------------------------------------------------- |
| Create Lead             | POST       | Creates a new lead                                                  |
| Update Lead             | PUT        | Updates an existing lead                                            |
| Delete Lead             | DELETE     | Deletes an existing lead                                            |
| Get Lead                | GET        | Fetches a specific lead by ID                                       |
| Search Leads            | GET        | Retrieves the latest 200 leads meeting the specified criteria       |
| Create Account          | POST       | Creates a new account                                               |
| Update Account          | PUT        | Updates an existing account                                         |
| Delete Account          | DELETE     | Deletes an existing account                                         |
| Get Account             | GET        | Fetches a specific account by ID                                    |
| Search Accounts         | GET        | Retrieves the latest 200 accounts meeting the specified criteria    |
| Create Task             | POST       | Creates a new task                                                  |
| Update Task             | PUT        | Updates an existing task                                            |
| Delete Task             | DELETE     | Deletes an existing task                                            |
| Get Task                | GET        | Fetches a specific task by ID                                       |
| Search Tasks            | GET        | Retrieves the latest 200 tasks fulfilling the specified criteria    |
| Create Meeting          | POST       | Creates a new meeting                                               |
| Update Meeting          | PUT        | Updates an existing meeting                                         |
| Delete Meeting          | DELETE     | Deletes an existing meeting                                         |
| Get Meeting             | GET        | Fetches a specific meeting by ID                                    |
| Search Meetings         | GET        | Retrieves the latest 200 meetings fulfilling the specified criteria |
| Create Deal             | POST       | Creates a new deal                                                  |
| Update Deal             | PUT        | Updates an existing deal                                            |
| Delete Deal             | DELETE     | Deletes an existing deal                                            |
| Get Deal                | GET        | Fetches a specific deal by ID                                       |
| Search Deals            | GET        | Retrieves the latest 200 deals meeting the specified criteria       |
| Create Campaign         | POST       | Creates a new campaign                                              |
| Update Campaign         | PUT        | Updates an existing campaign                                        |
| Delete Campaign         | DELETE     | Deletes an existing campaign                                        |
| Get Campaign            | GET        | Fetches a specific campaign by ID                                   |
| Search Campaigns        | GET        | Retrieves the latest 200 campaigns meeting the specified criteria   |
| Create Contact          | POST       | Creates a new contact                                               |
| Update Contact          | PUT        | Updates an existing contact                                         |
| Delete Contact          | DELETE     | Deletes an existing contact                                         |
| Remove Tag from Contact | POST       | Removes a tag from a contact                                        |
| Tag a Contact           | POST       | Adds a tag to a contact                                             |
| Get Contact             | GET        | Fetches a specific contact by ID                                    |
| Search Contacts         | GET        | Retrieves the latest 200 contacts meeting the specified criteria    |
| Add Note                | POST       | Adds a note to a record                                             |

&#x20;

#### Authorization <a href="#h_01j1vwmb9jrpz9a1d807zsc0mt" id="h_01j1vwmb9jrpz9a1d807zsc0mt"></a>

Your users will login to Zoho CRM via OAuth 2.0 using Integry's developer app. You can [replace it](https://support.integry.io/hc/en-us/articles/10887314172441) by [setting up your own](https://www.zoho.com/crm/developer/docs/api/v3/oauth-overview.html).&#x20;

### Limitations <a href="#h_01j1vwmb9j0c6yjtqckghq7ebb" id="h_01j1vwmb9j0c6yjtqckghq7ebb"></a>

Following are the limitations in the Zoho CRM App Connector as yet.

* The Twitter and Skype ID you use should be one word with no spaces.
* The connector does not support ‘**.cn**’ domains.
