# GetResponse

[GetResponse](https://www.integry.io/apps/getresponse) is an email marketing platform. You can use it to send email newsletters, campaigns, online surveys, and follow-up on autoresponders. You can also create personalized journeys for your customers based on their requirements, needs, data, etc. You can use the built-in templates for emails and campaigns. The GetResponse App Connector can help you manage and sync contacts with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your GetResponse account with Integry, here are a few things you need to learn about the GetResponse App Connector.&#x20;

#### **Authorization Type** <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

GetResponse uses an [API Key](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) based authentication. The end-user is identified by an API key, and Integry uses this key to perform an API request to GetResponse on behalf of that end-user.&#x20;

#### **Triggers** <a href="#triggers-0-2" id="triggers-0-2"></a>

Triggers in GetResponse are [webhook-based](https://tray.io/documentation/connectors/triggers/webhook-trigger/). Therefore, Integry will receive the trigger instantly as soon as an event occurs.&#x20;

### **Limitations** <a href="#limitations-0-3" id="limitations-0-3"></a>

Presently, there are the following limitations of the GetResponse App Connector:

* The action _create contact_ will take a few minutes to reflect in the GetResponse UI as it first gets added to a queue and then processed. If it still does not appear in the UI then that means the contact was rejected at some later stage.
* Campaigns can only be created or updated by adding or updating just the name field.
