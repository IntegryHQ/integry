# Zoho Mail

[Zoho Mail](https://www.integry.io/apps/zm) is a secure online platform for collaborative business communications. It combines email with modern collaboration tools using comments, likes, event streaming, and sharing. The security and privacy features of Zoho Mail allow you to keep your email data safe from different types of email attacks. Zoho Mail's extensive control panel enables you to manage all the settings, customizations, and configurations - all in a single place. The Zoho Mail App Connector helps you manage and sync emails with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Zoho Mail account with Integry, here are a few things you need to learn about the Zoho Mail App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Zoho Mail uses the [OAuth](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization method, where the access token expires after an hour. A refresh token is used to generate a new access token after it expires. This won't have any impact on current integrations if implemented properly. This authorization enables third-party applications (clients) to gain delegated access to protected resources in Zoho via an API. When you set up an integration, you need to allow Integry to access your Zoho Mail account.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers used in Zoho Mail are Post save triggers (manual triggers). Post save trigger is a type of [webhook-based](https://tray.io/documentation/connectors/triggers/webhook-trigger/) trigger. In this type of trigger, Integry provides a link at the end of the integration setup. That link is added to Zoho Mail's website. Payload is received on this link.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Currently, there is only one limitation of this app. The Zoho Mail connector does not support '**.cn**' domains.
