# Slack

[Slack](https://www.integry.io/apps/slack) is a secure online messaging app for your team to stay connected internally as well as with external teams. It also enables you to automate tasks inside and outside of Slack and organize communication using channels based on teams, clients, or projects. You can also share files and audio clips with your peers or even post a bot message. The Slack App Connector can be used to manage messages, channels, and user statuses between your Slack account and other third-party app accounts.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Slack account with Integry, you can go through some basic specifications of the Slack App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Slack uses an[ OAuth2](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) based authentication and stores two types of access tokens-user access token and bot token. These access tokens never expire. When setting up an integration, you need to allow Integry to request and acquire access to your Slack account.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

No triggers are implemented as of now, but when we implement them, these will be [webhook based](https://tray.io/documentation/connectors/triggers/webhook-trigger/). This means that as soon as an event occurs, Integry will receive the trigger right away.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Here are some of the limitations of the Slack App Connector:&#x20;

* No messages can be sent to DMs or Grouped DMs using the "Post Message" activity.
* As an end-user, you can only join a public channel using the "Join Channel" activity.
* Only fixed access tokens are supported. Fixed access tokens don't expire and hence a refresh token is not needed to generate a new one.
