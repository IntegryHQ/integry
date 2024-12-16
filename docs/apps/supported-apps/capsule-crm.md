# Capsule CRM

[Capsule CRM](https://www.integry.io/apps/capsule-crm) is an online customer relationship manager for individuals, small businesses, and sales teams wanting a simple, effective, and affordable solution. This tool keeps customer information along with easy history tracking. The Capsule CRM App Connector is multi-purpose and can be used to sync and manage people, opportunities, tasks, and cases between your Capsule CRM account and other third-party app accounts.&#x20;

### Specifications <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Capsule CRM account with Integry, here are a few things you need to learn about the Capsule CRM App Connector.&#x20;

#### Authorization Type <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Capsule CRM uses the [OAuth ](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry)authorization method where the access token expires after seven days. A refresh token is used to generate a new access token after it expires. This won't have any impact on current integrations if implemented properly. This authorization enables third-party applications (clients) to gain delegated access to protected resources in Capsule via an API. When setting up an integration, you need to allow Integry to use your Capsule CRM account.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

Triggers in Capsule CRM are [webhook-based](https://tray.io/documentation/connectors/triggers/webhook-trigger/). Therefore, Integry will listen for events happening inside your Capsule account.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

As of now, there are the following limitations in the Capsule CRM App Connector:

* Custom fields are not supported in queries.
* While creating/updating a person or an opportunity, you can only attach a single tag.
* You can only add a single email, social site, phone, and address while creating a person.
