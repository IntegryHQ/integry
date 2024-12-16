# Zoho Campaigns

[Zoho Campaigns](https://www.integry.io/apps/zoho-campaigns) is an online platform for email marketing. It helps in managing the email database of your leads and contacts. You can use it to create personalized emails and automated workflows and also build relations with potential customers. The Zoho Campaigns App Connector helps you sync and manage campaigns, topics, and contacts with other third-party apps.&#x20;

### ‍Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Zoho Campaigns account with Integry, here are a few things you need to learn about the Zoho Campaigns App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Zoho Campaigns uses the [OAuth ](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry)authorization method, where the access token expires after an hour. A refresh token is used to generate a new access token after it expires. This won't have any impact on current integrations if implemented properly. This authorization enables third-party applications (clients) to gain delegated access to protected resources in Zoho via an API. When you set up an integration, you need to allow Integry to access your Zoho Campaigns account.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers in Zoho Campaigns are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to Zoho Campaigns every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Zoho Campaigns acts as a trigger application) and perform an action in Zoho Campaigns, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Currently, there is only one limitation of this app. The Zoho Campaigns connector does not support '**.cn**' domains.
