# Monday.com

[Monday.com](https://www.integry.io/apps/monday-com) is an online tool to manage workload, track projects, and communicate with people. It also enables you to make lists of tasks and activities to be done and assign them to people in various teams. It helps in effectively managing work by adding comments, documents, and files to a task. The boards created by users automatically sync with Integry. The Monday.com App Connector manages and syncs tasks and projects with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Following are the basic specifications of the Monday.com App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Monday.com uses [API key](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) based authentication. The end-user is identified by an API key, and Integry uses this key to perform an API request to Monday.com on behalf of that end-user.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

Monday.com uses [poll-based](https://support.integry.io/hc/en-us/articles/360021913374-Creating-Poll-Based-Triggers) triggers. Integry will send a request to Monday.com every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Monday.com acts as a trigger application) and perform an action in Monday.com, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Currently, there are no limitations for this App Connector.
