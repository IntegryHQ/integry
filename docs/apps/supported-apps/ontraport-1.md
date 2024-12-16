# Ontraport

[Ontraport](https://www.integry.io/apps/ontraport) is a sales, marketing, and business automation software for entrepreneurs, solopreneurs, and small businesses. It incorporates tools like CRM, marketing automation, ECommerce, and reporting. The contacts and products created in Ontraport automatically sync with Integry. The Ontraport App Connector manages and syncs contacts and products with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Ontraport account with Integry, you can go through some specifications of the Ontraport App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Ontraport uses the [API key + secret](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization method. You must obtain a unique API key and App ID to get started, which can be requested in your [Administration settings](https://app.ontraport.com/#!/api_settings/listAll).&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

Ontraport uses [Poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/) triggers. Integry will send a request to Ontraport every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Ontraport acts as a trigger application) and perform an action in Ontraport, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Here are some of the limitations of the Ontraport Connector:

* The Product Updated, Campaign Update, and Contact Updated/Deleted Activities are not supported in the Ontraport App Connector.
* The Product object does not support custom fields.
* For date fields in Contact Object, you must map with a field that uses the YYYY-MM-DD format.
* Some objects (deals, companies, etc.) are not visible by default in your Ontraport account. You need to turn on the toggle button for these objects from the app's settings here:[https://app.ontraport.com/#!/app\_marketplace/view](https://app.ontraport.com/#!/app_marketplace/view).
