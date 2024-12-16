# Insightly

[Insightly](https://www.integry.io/apps/insightly) is a customer relationship manager that combines marketing, sales, service, and projects. Its marketing automation helps you build new customer relationships and strengthen existing ones. In addition, you can track real-time campaign performance and ROI. The Insightly App Connector enables to sync and manage contacts with other third-party apps.&#x20;

Integry supports a number actions in Insightly.

#### Authentication <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Insightly uses API Key+URL authentication.

### Triggers <a href="#h_01hr556ap5m0d97s0v2hv9bk41" id="h_01hr556ap5m0d97s0v2hv9bk41"></a>

The triggers used in Insightly are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to Insightly every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Insightly acts as a trigger application) and perform an action in Insightly, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

| **Name**                | **Type** | **Description**                                                      |
| ----------------------- | -------- | -------------------------------------------------------------------- |
| Event Created           | Polling  | Triggers when an event is created                                    |
| Contact Created         | Polling  | Triggers when a contact is created                                   |
| Lead Created            | Polling  | Triggers when a lead is created                                      |
| Event Created/Updated   | Polling  | Triggers when an existing event is updated or a new one is created   |
| Contact Created/Updated | Polling  | Triggers when an existing contact is updated or a new one is created |
| Lead Created/Updated    | Polling  | Triggers when an existing lead is updated or a new one is created    |

For more, please see [Insightly API docs](https://api.na1.insightly.com/v3.1/).

#### Actions <a href="#h_01hr56vpze824xf8dyw4e604x7" id="h_01hr56vpze824xf8dyw4e604x7"></a>

| **Name**              | **Method** | **Description**                                                                                        |
| --------------------- | ---------- | ------------------------------------------------------------------------------------------------------ |
| Delete Contact        | DELETE     | Deletes an existing contact                                                                            |
| Create Contact        | POST       | Creates a new contact                                                                                  |
| Get Contact by ID     | GET        | Fetch the details of a contact using ID                                                                |
| Update Contact        | PUT        | Updates an existing contact                                                                            |
| Get Contacts by Email | GET        | Retrieve the list of contacts that match the email address. Only the top 50 contacts will be returned. |
| Get Event by ID       | GET        | Fetch the details of an event using ID                                                                 |
| Create Event          | POST       | Creates a new event on your calendar.                                                                  |
| Get Lead by ID        | GET        | Fetch the details of a lead using ID                                                                   |
| Create Lead           | POST       | Creates a new lead                                                                                     |
| Update Lead           | PUT        | Updates an existing lead                                                                               |
| Get Leads by Email    | GET        | Retrieve the list of leads that match the email address. Only the top 50 leads will be returned.       |
| Get Object by ID      | GET        | Fetches the details of object by their ID                                                              |

