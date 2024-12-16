# Pipeline

[Pipeline](https://www.integry.io/apps/pipeline) is an online platform to increase your sales productivity. It combines sales engagement and CRM in one user-friendly application. The platform enables you to use intuitive tools for integrations. The Pipeline App Connector can be used to make seamless integrations with other third-party app accounts to manage your deals, leads, and contacts.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Following are the basic specifications of the Pipeline App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

The Pipeline app uses [API Key](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) based authentication. The end-user is identified by an API key, and Integry uses this key to perform an API request to Pipeline on behalf of that end-user. To use this authentication type for this app, you just need to grab your `api_key` and Allow Unregistered API from API Integrations, shown above.&#x20;

<figure><img src="../../.gitbook/assets/image (79).png" alt=""><figcaption></figcaption></figure>

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The Pipeline triggers are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to Pipeline every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. When you set up an integration (in which Pipeline acts as a trigger application) and perform an action in Pipeline, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

A specific date format is to be used in deals that is YYYY-MM-DD.
