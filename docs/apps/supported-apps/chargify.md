# Chargify

[Chargify](https://www.integry.io/apps/chargify) is a billing system for Web 2.0 and SaaS companies. It provides the revenue management tools you need for your business. Chargify enables you to manage billing and subscription for B2B SaaS customers. It also offers features like self-serve product plans, support for trial periods, complicated billing structures, and multiple payment collection options. The Chargify App Connector can help sync and manage customers with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Chargify account with Integry, here are a few things you need to learn about the Chargify App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Chargify uses a variant of [Basic+URL](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry). In order to authenticate, a user must enter their API key and password along with their instance URL.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

Chargify supports [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/) triggers. Integry will send a request to Chargify every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Chargify acts as a trigger application) and perform an action in Chargify, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Currently, custom fields are not supported in query mapping in the Chargify App Connector.
