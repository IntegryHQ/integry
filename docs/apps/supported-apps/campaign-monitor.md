# Campaign Monitor

[Campaign Monitor](https://www.integry.io/apps/campaign-monitor) is an online email marketing and automation platform that helps users to create, send, manage, and track branded emails for themselves and their clients. It enables you to create personalized customer journeys and smart segments and send relevant emails to potential customers. It also offers campaign customization and template management. The Campaign Monitor App Connector helps sync with and manage your subscribers with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Campaign Monitor account with Integry, here are a few things you need to learn about the Campaign Monitor App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

The Campaign Monitor App Connector uses the [OAuth2 ](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry)authorization type. The access token used here usually expires in 14 days, and once it expires, Integry makes an internal call to get a new access token.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

Triggers in Campaign Monitor use [webhook](https://tray.io/documentation/connectors/triggers/webhook-trigger/) subscriptions. This means that as soon as an event occurs, Integry will receive the trigger instantly.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Currently, there is only one limitation of the Campaign Monitor App Connector. In triggers and queries, multi-select or single-select dropdowns are not supported for mapping.
