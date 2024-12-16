# SendPulse

[SendPulse ](https://www.integry.io/apps/sendpulse)is an online automation platform for business promotion and customer retention. It allows you to send email and SMS campaigns, work with clients using chatbots for Telegram, Facebook Messenger, WhatsApp, and Instagram, and create landing pages. The SendPulse App Connector helps sync and manage campaigns and mailing lists with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your SendPulse account with Integry, here are a few things you need to learn about the SendPulse App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

SendPulse uses the [OAuth](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization method, where the access token expires after an hour. A refresh token is used to generate a new access token after it expires. This won't have any impact on existing integrations if implemented properly. This authorization enables third-party applications (clients) to gain delegated access to protected resources in SendPulse via an API. When you set up an integration, you need to allow Integry to access your SendPulse account.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

SendPulse uses [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/) triggers. Integry will send a request to SendPulse every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which SendPulse acts as a trigger application) and perform an action in SendPulse, expect a 5-minute delay to receive the trigger at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

SendPulse App Connector doesn't support the queries and triggers for **contact** and **deal** objects.
