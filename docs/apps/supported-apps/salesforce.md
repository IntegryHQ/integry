# Salesforce

Integry supports a number of triggers and actions of Salesforce.

#### Triggers <a href="#h_01hr556ap5m0d97s0v2hv9bk41" id="h_01hr556ap5m0d97s0v2hv9bk41"></a>

| **Name**            | **Type** | **Description**                                                                                         |
| ------------------- | -------- | ------------------------------------------------------------------------------------------------------- |
| Contact Created     | Polling  | Triggers when a contact is created                                                                      |
| Contact Updated     | Polling  | Triggers when a contact is updated                                                                      |
| Contact Deleted     | Polling  | Triggers when a contact is deleted                                                                      |
| Lead Created        | Polling  | Triggers when a lead is created                                                                         |
| Lead Updated        | Polling  | Triggers when a lead is updated                                                                         |
| Lead Deleted        | Polling  | Triggers when a lead is deleted                                                                         |
| Lead Merged         | Polling  | Triggers when a lead is merged into another lead and returns the lead that gets deleted after the merge |
| Task Created        | Polling  | Triggers when a new task is created                                                                     |
| Task Updated        | Polling  | Triggers when an existing task is updated                                                               |
| Task Deleted        | Polling  | Triggers when an existing task is deleted                                                               |
| Account Created     | Polling  | Triggers when a new account is created                                                                  |
| Account Updated     | Polling  | Triggers when an existing account is updated                                                            |
| Account Deleted     | Polling  | Triggers when an existing account is deleted                                                            |
| Opportunity Created | Polling  | Triggers when a new opportunity is created                                                              |
| Opportunity Updated | Polling  | Triggers when an existing opportunity is updated                                                        |
| Opportunity Deleted | Polling  | Triggers when an existing opportunity is deleted                                                        |
| Campaign Created    | Polling  | Triggers when a new campaign is created                                                                 |
| Campaign Updated    | Polling  | Triggers when an existing campaign is updated                                                           |
| Campaign Deleted    | Polling  | Triggers when an existing campaign is deleted                                                           |
| Product Created     | Polling  | Triggers when a new product is created                                                                  |
| Product Updated     | Polling  | Triggers when an existing product is updated                                                            |
| Order Created       | Polling  | Triggers when a new order is created                                                                    |
| Order Updated       | Polling  | Triggers when an existing order is updated                                                              |

&#x20;

For more, please see [Salesforce API docs](https://developer.salesforce.com/docs/apis). If you're not sure how triggers work in Integry, go [here](https://support.integry.io/hc/en-us/articles/29484874325017).

#### Actions <a href="#h_01hr56vpze824xf8dyw4e604x7" id="h_01hr56vpze824xf8dyw4e604x7"></a>

| **Name**                                | **Method** | **Description**                                                      |
| --------------------------------------- | ---------- | -------------------------------------------------------------------- |
| Delete Contact                          | DELETE     | Deletes an existing contact                                          |
| Contact Opt In/Out of Email             | PATCH      | Opts a contact in or out of email services                           |
| Lead Opt In/Out of Email                | PATCH      | Opts a lead in or out of email services                              |
| Create Task                             |  POST      | Creates a new task                                                   |
| Delete Task                             | DELETE     | Deletes an existing task                                             |
| Update Task                             | PATCH      | Updates an existing task                                             |
| Delete Opportunity                      | DELETE     | Deletes an existing opportunity                                      |
| Delete Account                          | DELETE     | Deletes an existing account                                          |
| Create Opportunity                      | POST       | Creates a new opportunity                                            |
| Update Opportunity                      |  PATCH     | Updates an existing opportunity                                      |
| Create Account                          | POST       | Creates a new account                                                |
| Update Account                          | POST       | Updates an existing account                                          |
| Create Campaign                         | POST       | Creates a new campaign                                               |
| Update Campaign                         | PATCH      | Updates an existing campaign                                         |
| Create Product                          | POST       | Creates a new product                                                |
| Update Product                          | PATCH      | Updates an existing product                                          |
| Create Order                            | POST       | Creates a new order                                                  |
| Update Order                            | PATCH      | Updates an existing order                                            |
| Delete Lead                             | DELETE     | Deletes an existing lead                                             |
| Create Lead                             | POST       | Creates a new lead                                                   |
| Update Lead                             | PATCH      | Updates an existing lead                                             |
| Get All Lead Statuses                   | GET        | Fetches the list of all the lead statuses from your account          |
| Create User                             | POST       | Creates a new user in your Salesforce organization                   |
| Get Lead by ID                          | GET        | Fetches the details of a lead                                        |
| Get Contact by ID                       |  GET       | Fetches the details of a contact                                     |
| Add Lead or Contact to Campaign Members | POST       | Adds the selected lead or contact to the selected campaign's members |
| Create Contact                          | POST       | Creates a new contact                                                |
| Update Contact                          | PATCH      | Updates an existing contact                                          |

For more, please see [Salesforce API docs](https://developer.salesforce.com/docs/apis).

#### Authorization <a href="#h_01hr556ap450c8s3d5hf8vc37f" id="h_01hr556ap450c8s3d5hf8vc37f"></a>

Your users will login to Salesforce via OAuth 2.0 using Integry's developer app. You can [replace it](https://support.integry.io/hc/en-us/articles/10887314172441) by [setting up your own](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm).&#x20;

#### Limitations <a href="#id-01hw7xga6eebx1ryc0zn192pt8" id="id-01hw7xga6eebx1ryc0zn192pt8"></a>

Following are the limitations in the Salesforce App Connector as yet.

* Boolean type custom fields are not supported for field mapping.
* Sandbox environment is not supported for Flow testing.
* If you try to connect an account that is not API enabled, you won't be able to authenticate your account.&#x20;

#### FAQs <a href="#id-01hw60a621etfhwyaqdtv9jkj2" id="id-01hw60a621etfhwyaqdtv9jkj2"></a>

**What does the “OAUTH\_APP\_BLOCKED” error in Salesforce mean, and how can I resolve it?**\
The “OAUTH\_APP\_BLOCKED” error indicates that the app you are trying to access is blocked by an administrator. This can happen if the app's access has been restricted within the Salesforce CRM settings.

To resolve this issue, you need to check the “Connected Apps OAuth Usage” settings within an admin account and unblock the app. Follow these steps to do so:

1. Sign in to Salesforce CRM as an administrator.
2. Navigate to **Setup**.
3. Go to **Platform Tools > Apps > Connected Apps > Connected Apps OAuth Usage**.
4. Locate the app that is blocked.
5. Select **Unblock** for the app.

&#x20;

**What does the “INVALID\_SESSION\_ID” error in response mean in salesforce and how can I resolve it?**\
The “INVALID\_SESSION\_ID” error indicates that your access token has become invalid. This situation can occur for various reasons, such as the user revoking the app’s access or changes made to the user’s security settings.\
When this error occurs, it is necessary for you to re-authenticate in order to restore the integration’s functionality, simply trying to enable the integration again will result in the same error message.\
Here is an example of what the error payload will look like:

```json
[
    {
        "message": "Session expired or invalid",
        "errorCode": "INVALID_SESSION_ID"
    }
]
```

\
