# ClickUp

[ClickUp](https://www.integry.io/apps/clickup) is a productivity platform that helps make management, communication, and collaboration smooth and simple with its built-in tools. You can use it to create custom workflows, communicate effectively through assigned comments, and work on multiple tasks through the multitask toolbar. It offers a tree structure view of your tasks. You can also customize the interface according to your needs. The ClickUp App Connector syncs and manages tasks with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your ClickUp account with Integry, here are a few things you need to learn about the ClickUp App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

ClickUp uses the [OAuth](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry/#scopes) authorization type. The end-user logs in and grants access to their ClickUp account. The ClickUp API notifies Integry that the end-user has given access to their account. Integry is then able to communicate with ClickUp's API on behalf of that end-user.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers in ClickUp are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to ClickUp every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which ClickUp acts as a trigger application) and perform an action in ClickUp, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Currently, there are no limitations of the ClickUp App Connector.
