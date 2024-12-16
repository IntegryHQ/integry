# CleverReach

[CleverReach](https://www.integry.io/apps/cleverreach) is an email marketing platform. It helps you create automated email marketing campaigns for your customers. It also enables you to choose from the available templates to target your customers. You can manage your lists and user segments by designing personalized email campaigns for customers based on their geographic location, demographics, interests, etc. You can also gauge your email reach by analyzing client email reports and improving your campaigns. The CleverReach App Connector helps you manage and sync recipients with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Following are the specifications of the CleverReach App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

CleverReach uses the [OAuth2 ](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry)authorization method, where the access token expires after a month. A refresh token is used to generate a new access token after it expires. This won't have any impact on current integrations if implemented properly. This authorization enables third-party applications (clients) to gain delegated access to protected resources in CleverReach via an API. When you set up an integration, you need to allow Integry to access your CleverReach account.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers in CleverReach are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to CleverReach every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which CleverReach acts as a trigger application) and perform an action in CleverReach, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Currently, there are the following limitations of the CleverReach App Connector:

* Open tracking is only available for HTML-type campaigns.
* The 'Google Campaign Name' field works only if the 'Link Tracking Type' is 'Google.'
