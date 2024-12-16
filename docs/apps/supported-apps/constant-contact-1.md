# Constant Contact

[Constant Contact](https://www.integry.io/apps/constant-contact) is an online tool for email marketing. This platform can be used to create and manage campaigns and templates for email marketing, strengthen customer relations, and grow your contact lists. It enables you to create segmented customer lists and keep track of the sent emails. The Constant Contact App Connector helps you manage and sync contacts and email campaigns with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Constant Contact account with Integry, you can go through some basic specifications of the Constant Contact App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Constant Contact uses the [OAuth](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization type. The access token expires in 24 hours and gets refreshed automatically after expiration.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers in Constant Contact are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to Constant Contact every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Hubspot acts as a trigger application) and perform an action in Constant Contact, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

At present, there is only one limitation of the Constant Contact App Connector that while updating an email campaign, only the name can be updated.
