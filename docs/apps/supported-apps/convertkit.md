# ConvertKit

[ConvertKit](https://www.integry.io/apps?Search=meister) is an email marketing software with features for creators. It helps you grow your email list through vibrant forms, trackable data, and automations. You can schedule targeted content for your subscribers and build personalized automated emails through the sequence builder and define rules with workflows. ConvertKit supports subscriber segmentation through tags. ConvertKit syncs and manages subscribers with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your ConvertKit account with Integry, here are a few things you need to learn about the ConvertKit App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

The authorization type used in ConvertKit is [API Secret](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry), where you have to provide just the API secret to authorize your account.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

ConvertKit uses [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/) triggers. Integry will send a request to ConvertKit every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which ConvertKit acts as a trigger application) and perform an action in ConvertKit, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Currently, there are no limitations of the ConvertKit App Connector.
