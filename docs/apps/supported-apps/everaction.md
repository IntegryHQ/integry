# EverAction

[EveryAction](https://www.integry.io/apps/everyaction) is a CRM that handles fundraising, donor management, and advocacy. It helps you segment and manage fundraising data, volunteers, and donors. You can effectively manage your campaigns through features such as integration with social networks, one-click donations, and better event management. It also helps with marketing automation, predictive analysis, and membership management. EveryAction App Connector syncs and manages contacts with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your EveryAction account with Integry, here are a few things you need to learn about the EveryAction App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

EveryAction uses the [Basic](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization type. This authorization type asks for your username and password and authenticates using those.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The EveryAction connector used [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/) triggers. Integry will send a request to EveryAction every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which EveryAction acts as a trigger application) and perform an action in EveryAction, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Presently, there are no limitations of the EveryAction App Connector.
