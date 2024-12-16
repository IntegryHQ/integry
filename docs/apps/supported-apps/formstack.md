# Formstack

[Formstack](http://www.formstack.com/) is an online data management solution that helps users collect information through various types of online forms, including surveys, job applications, event registrations, and payment forms. You can use it to create responsive forms, customize them through easy drag and drop, and integrate them in minutes. The forms can be created from scratch, or via pre-built templates. Formstack is extremely secure and can help in online payments as well. The Formstack App Connector syncs and manages forms with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Formstack account with Integry, here are a few things you need to learn about the Formstack App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

The authorization type in Formstack is [OAuth 2](https://support.integry.io/hc/en-us/articles/11112617800985-Supported-Authentication-Types).&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The _form created_ and form updated triggers in Front are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). which means Integry will send a request to Front every 5 minutes to collect data for contact triggers. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Front acts as a trigger application) and perform an action in Front, expect a 5-minute delay for the trigger to be received at Integry.The _new submission added_ trigger is [webhook-based](https://tray.io/documentation/connectors/triggers/webhook-trigger/). Therefore, as soon as an event occurs, Integry will receive the trigger instantly.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

There are no limitations of the Formstack App Connector.
