# Help Scout

[Help Scout](https://www.helpscout.com/) is an email-based customer support platform. It helps you make personalized communications, create multiple mailboxes for a shared email address, get real-time information on who is viewing or replying, save time by using saved messages, create workflows, and save time and effort by automating repeated tasks. You can use it to get feedback from your customers, evaluate team performance, and track trends through automatically generated reports. The Help Scout App Connector syncs and manages articles and conversations with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Help Scout account with Integry, here are a few things you need to learn about the Help Scout App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

The authorization type is [OAuth](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry). The access token expires in 48 hours, and the refresh token is implemented. A new access token is generated with the help of the refresh token.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers of HelpScout are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to Help Scout every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Help Scout acts as a trigger application) and perform an action in Help Scout, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

In the Article Object, the Keyword field needs comma-separated values, e.g., Value1, Value2.
