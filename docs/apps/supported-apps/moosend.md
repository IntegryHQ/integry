# Moosend

[Moosend](https://www.integry.io/apps/moosend) is a web-based marketing automation tool that helps you seamlessly manage your email campaigns, so you can grow your business. This email platform helps small and medium businesses to increase lead generation and nurture audience. The Moosend App Connector can be used to sync and manage campaigns and members with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Moosend account with Integry, you can go through some basic specifications of the Moosend App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

The auth type used in Moosend is [API Key](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry). An API key identifies the end-user, and Integry uses this key to communicate with Moosend's API on behalf of that end-user.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

Moosend triggers are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to Moosend every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. When you set up an integration (in which Moosend acts as a trigger application) and perform an action in Moosend, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

The Moosend app has the following limitations:

* While creating an A/B campaign you need to fill the Web location B field if the campaign type is content, Sender B if the campaign type is sender, and subject B if the content type is Subject Line respectively.
* A regular campaign cannot be updated to an A/B campaign and vice versa.
