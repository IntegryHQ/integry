# ClickSend

[ClickSend](https://www.integry.io/apps/clicksend) is a cloud-based service that lets you send and receive SMS, Email, Voice, Fax, and Letters worldwide. The app provides integratable products necessary for business communications. You can use their dashboard or APIs to send across rich media. The ClickSend App Connector helps you sync and manage contacts and campaigns with other third-party apps.‍

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your ClickSend account with Integry, here are a few things you need to learn about the ClickSend App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

ClickSend uses [API key + secret ](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry)authorization type. The end-user is identified by an API key and secret. Integry uses this information to perform an API request to ClickSend on behalf of that end-user.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers in ClickSend are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to ClickSend every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which ClickSend acts as a trigger application) and perform an action in ClickSend, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Currently, there is only one limitation of the ClickSend App Connector, there is no trigger to fetch updates in the campaign.
