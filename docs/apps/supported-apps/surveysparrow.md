# SurveySparrow

[SurveySparrow](https://surveysparrow.com/) is an online survey tool. It has a dual-user interface that helps you create chat-like surveys or conversational forms. The features include previews, recurring surveys, customization, rich analytics, audience management, and more. You can use it to create market research forms, employee feedback, and customer satisfaction forms. The SurveySparrow App Connector syncs and manages contacts with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your SurveySparrow account with Integry, here are a few things you need to learn about the SurveySparrow App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

SurveySparrow uses the [API-Key](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization. An API key identifies the end-user, and Integry uses this key to communicate with SurveySparrow's API on behalf of that end-user.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers used in SurveySparrow are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to SurveySparrow every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. When you set up an integration (in which SurveySparrow acts as a trigger application) and perform an action in SurveySparrow, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

There are no limitations of the SurveySparrow App Connector.
