# SolarWinds

[SolarWinds](https://www.solarwinds.com/service-desk) is an enterprise service desk and IT asset-management provider. You can use it to manage, gather, prioritize tickets and gain insights into what issues are impacting your business without disturbing the flow of things. It also helps in executing change plans while formalizing documentation and approval processes. The SolarWinds App Connector syncs and manages incidents with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your SolarWinds account with Integry, here are a few things you need to learn about the SolarWinds App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

SolarWinds uses [API-Key](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization. An API key identifies the end-user, and Integry uses this key to communicate with SolarWinds's API on behalf of that end-user.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers used in SolarWinds are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to SolarWinds every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. When you set up an integration (in which SolarWinds acts as a trigger application) and perform an action in SolarWinds, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

The date format for tasks or incidents should be (YYYY-MM-DD).
