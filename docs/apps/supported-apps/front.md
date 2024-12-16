# Front

[Front](https://app.frontapp.com/) lets you manage all of your communication channels' emails, social media, chat, and SMS in one place. You can manage your private and shared conversations from anywhere with mobile apps. It helps you assign every conversation for clear ownership, coordinate the next steps with in-line comments and mentions, and avoid duplicate replies through collision detection. You can also use the inbuilt reminders feature. The Front App Connector syncs and manages contacts, messages, and tags with other third-party apps.

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Front account with Integry, here are a few things you need to learn about the Front App Connector.

&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Front uses [API key ](https://support.integry.io/hc/en-us/articles/11112617800985-Supported-Authentication-Types)based authorization. An API key identifies the end-user, and Integry uses this key to communicate with Front's API on behalf of that end-user.

&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers in Front are[ poll-based.](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/) Integry will send a request to Front every 5 minutes to collect data for contact triggers. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Front acts as a trigger application) and perform an action in Front, expect a 5-minute delay for the trigger to be received at Integry.

&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

There are no limitations of the Front App Connector.
