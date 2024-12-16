# Copper

[Copper](https://www.integry.io/apps/copper) is an online platform with email and marketing tools that save personal information to help boost your sales. It helps in organizing contacts, automating tasks, tracking your deals, managing projects, and getting reports. The Copper App Connector manages and syncs company, opportunity, task, and person with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Following are the basic specifications of the Copper App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Copper uses the [API key + secret](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization method. You must obtain a unique API key and App ID to get started, which can be requested in your Account's settings.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

Copper uses[ poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/) triggers. Integry will send a request to Copper every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Copper acts as a trigger application) and perform an action in Copper, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Currently, there are no limitations for this App Connector.
