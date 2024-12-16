# Keap

[Keap](https://keap.com/) is an automated email marketing and sales platform to deliver personalized service to clients. Keap includes products to manage customers, customer relationships, marketing, and e-commerce. You can use it to collect leads, write emails and texts, send emails to segmented lists, and carry out auto follow-ups. The Keap App Connector syncs and manages contacts with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Keap account with Integry, here are a few things you need to learn about the Keap App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

The Keap App Connector uses the [OAuth](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization type. The access token is valid for 24 hours. After the expiration, a new access token is generated using a refresh token which is valid for 45 days.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers used in Keap are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to Keap every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Keap acts as a trigger application) and perform an action in Keap, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

The following are the limitations of the Keap App Connector:

* In the contact object, the country field only accepts ISO-based codes, e.g., PAK or AUS.
* In the contact object, the birthday and anniversary fields only accept dates in YYYY-MM-DD format.
