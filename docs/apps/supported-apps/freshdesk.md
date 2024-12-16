# Freshdesk

[Freshdesk](http://www.freshdesk.com/) is an online cloud-based customer service software providing helpdesk support with smart automations. It streamlines customer conversations across channels like email, social media, phone, and chat. The Freshdesk App Connector manages and syncs contact, company, and ticket with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Freshdesk account with Integry, here are a few things you need to learn about the Freshdesk App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Freshdesk uses the [APIKey+URL](https://support.integry.io/hc/en-us/articles/360022115853-Authentication-Types-Supported-in-Integry) authorization. An API key +URL identifies the end-user, and Integry uses this key+URL combination to communicate with Freshdesk's API on behalf of that end-user.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The contact triggers are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/), which means Integry will send a request to Freshdesk every 5 minutes to collect data for contact triggers. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Freshdesk acts as a trigger application) and perform an action in Freshdesk, expect a 5-minute delay for the trigger to be received at Integry.The ticket trigger is [webhook-based](https://tray.io/documentation/connectors/triggers/webhook-trigger/). Therefore, as soon as an event occurs, Integry will receive the trigger instantly.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Presently, there are no limitations of the Freshdesk App Connector.
