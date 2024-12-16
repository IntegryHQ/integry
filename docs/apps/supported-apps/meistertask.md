# MeisterTask

[MeisterTask](https://www.integry.io/apps/meistertask) is an online multi-platform collaboration and project management tool. You can use it to organize and manage tasks in a customizable environment that perfectly adapts to your workflow and automates recurring steps. It can be used to assign tasks to your team members, implement your ideas, and plan and visualize your tasks. It helps you communicate efficiently and save all your activities in the task's activity stream for traceability in the future. The MeisterTask App Connector syncs and manages projects with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your MeisterTask account with Integry, here are a few things you need to learn about the MeisterTask App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

MeisterTask uses the [OAuth](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization type. The access token does not expire and hence does not need to be regenerated.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The app uses [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/) triggers. Integry will send a request to MeisterTask every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which MeisterTask acts as a trigger application) and perform an action in MeisterTask, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

There are no limitations of the MeisterTask App Connector.
