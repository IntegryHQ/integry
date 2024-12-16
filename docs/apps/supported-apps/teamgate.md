# Teamgate

[Teamgate ](https://www.integry.io/apps/teamgate)is a customer relationship management tool designed to increase your sales. It is easy to use and helps streamline the sales process by gathering leads and closing deals. The Teamgate App Connector helps you manage and sync contacts and leads with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Insightly account with Teamgate, you can go through some basic specifications of the Teamgate App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Teamgate uses [API Key + secret](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization type. The end-user is identified by an API key and a secret, and Integry uses this key+secret combination to perform API requests to Teamgate on behalf of that end-user.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers in Teamgate are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to Teamgate every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Teamgate acts as a trigger application) and perform an action in Teamgate, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Currently, there are no limitations in the Teamgate App Connector.
