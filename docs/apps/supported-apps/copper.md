# Copper

Integry supports a number of triggers and actions of Copper.

#### Authentication <a href="#h_01hr556ap450c8s3d5hf8vc37f" id="h_01hr556ap450c8s3d5hf8vc37f"></a>

Copper uses OAuth 2.0.

#### Triggers <a href="#h_01hr556ap5m0d97s0v2hv9bk41" id="h_01hr556ap5m0d97s0v2hv9bk41"></a>

| **Name**               | **Type** | **Description**                              |
| ---------------------- | -------- | -------------------------------------------- |
| Company Created        | Polling  | Triggers when a new company is created       |
| Company Updated        | Polling  | Triggers when a new company is updated       |
| Company Deleted        | Instant  | Triggers when an existing company is deleted |
| Lead Created/Updated   | Polling  | Triggers when a lead is created or updated   |
| Opportunity Deleted    | Instant  | Triggers when a new opportunity is deleted   |
| Opportunity Created    | Polling  | Triggers when a new opportunity is created   |
| Opportunity Updated    | Polling  | Triggers when a new opportunity is updated   |
| Person Created         | Polling  | Triggers when a person is created            |
| Person Created/Updated | Polling  | Triggers when a person is created or updated |
| Task Created           | Polling  | Triggers when a new task is created          |
| Task Updated           | Polling  | Triggers when a task is updated              |
| Task Deleted           | Instant  | Triggers when an existing task is deleted    |

For more, please see [Copper API docs](https://developer.copper.com/).

#### Actions <a href="#h_01hr56vpze824xf8dyw4e604x7" id="h_01hr56vpze824xf8dyw4e604x7"></a>

| **Name**            | **Method** | **Description**                                                           |
| ------------------- | ---------- | ------------------------------------------------------------------------- |
| Delete Company      |  DELETE    | Deletes an existing company                                               |
| Create Company      | POST       | Creates a new company                                                     |
| Update Company      | PUT        | Updates an existing company                                               |
| Delete Lead         | DELETE     | Deletes an existing lead                                                  |
| Create Lead         | POST       | Creates a new lead                                                        |
| Update Lead         | PUT        | Updates an existing lead in your copper account                           |
| Get Lead by Email   | GET        | Fetches details of a lead record by email                                 |
| Get Lead by ID      | GET        | Fetches details of a lead by ID                                           |
| Upsert Lead         | PATCH      | Create a new lead if it does not match the criteria, else update the lead |
| Delete Task         | DELETE     | Deletes an existing task                                                  |
| Create Task         | POST       | Creates a new task                                                        |
| Update Task         | PUT        | Updates an existing task                                                  |
| Delete Opportunity  | DELETE     | Deletes an existing opportunity                                           |
| Create Opportunity  | POST       | Creates a new opportunity                                                 |
| Update Opportunity  | PUT        | Updates an existing opportunity                                           |
| Delete Person       | DELETE     | Deletes an existing person                                                |
| Create Person       | POST       | Creates a new person                                                      |
| Update Person       |  PUT       | Updates an existing person                                                |
| Get Person by Email | GET        | Fetches details of a person record by email                               |
| Get Person by ID    | GET        | Fetches details of a person record by ID                                  |

For more, please see [Copper API docs](https://developer.copper.com/).
