# Breezy HR

Breezy HR is an online recruiting tool where you can post new jobs, manage applicants, and recruit the most suitable resources. It helps in reporting and analytics as well. Breezy HR is an end-to-end applicant tracking platform that offers candidates pipelines, built-in scorecards, and interview guides. You can also use it to send bulk or individual custom emails, SMS, or even custom templates. The Breezy HR App Connector helps you sync and manage candidates with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Breezy HR account with Integry, here are a few things you need to learn about the Breezy HR App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Breezy HR uses the [Basic](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization type. A username and password identify the end-user. Integry uses this to perform an API request to Breezy HR on behalf of that end-user.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers in Breezy HR are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to Breezy HR every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Breezy HR acts as a trigger application) and perform an action in Breezy HR, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Currently, there is no activity to delete candidates in the Breezy HR App Connector.
