# Aha!

The [Aha!](https://www.integry.io/apps/aha) app organizes and integrates content from the web between your phone and car for easy access on the go. It is an online tool to run your product campaigns, work on roadmaps, and chalk out detailed features and user stories. Aha! works with a bug tracking system for the timely execution of products and their features. The Aha! App Connector helps you sync and manage ideas with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Aha! account with Integry, here are a few things you need to learn about the Aha! App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Aha! uses [API key + URL](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization type. An API key and URL identify the end-user. Integry uses this key to perform an API request to Aha! on behalf of that end-user.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers in Aha! are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to Aha! every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Aha! acts as a trigger application) and perform an action in Aha!, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Presently there are no limitations of the Aha! App Connector.
