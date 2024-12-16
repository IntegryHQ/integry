# Nimble

[Nimble ](https://www.integry.io/apps/nimble)is an online platform that combines high-end CRM systems and social media. You can use the dashboard available in Nimble to monitor the history of your customers. Nimble automatically syncs your data and brings your customers' data to one place. The Nimble CRM App Connector helps you manage and sync contacts with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Following are the basic specifications of the Nimble App Connector:&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Nimble CRM uses [API Key](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization type. The end-user is identified by an API key, and Integry uses this key to perform an API request to Nimble CRM on behalf of that end-user.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers in Nimble are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to Nimble every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Nimble acts as a trigger application) and perform an action in Nimble, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

This API is still under development and subject to change.
