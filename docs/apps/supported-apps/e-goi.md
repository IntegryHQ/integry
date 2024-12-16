# E-goi

[E-goi](https://www.integry.io/apps/e-goi) is an online tool for Marketing Automation that any company can use to manage its entire sales cycle, from capturing leads to customer conversion and loyalty. With E-goi schedule, you can create landing pages, forms, and pop-ups, perform advanced automation, and implement an E-mail marketing strategy, SMS, WebPush, Push Notification, and Voice campaigns. You can also do behavioral and intention tracking on web pages and online stores and have a public API. The E-goi App Connector helps to sync and manage e-mail campaigns, emails, and SMs with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your E-goi account with Integry, here are a few things you need to learn about the E-goi App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

E-goi uses [API key-based](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization type. An API key identifies the end-user. An API key identifies the end-user, and Integry uses this key to communicate with E-goi's API on behalf of that end-user.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers in E-goi are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to E-goi every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which E-goi acts as a trigger application) and perform an action in E-goi, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Presently, there are the following limitations of the E-goi App Connector:

* The 'Subject' and 'HTML Body' fields are only for HTML type e-mail campaigns.
* The 'Webpage URL' field and 'Use Webpage Title as Subject' checkboxes are only for Webpage type e-mail campaigns.
