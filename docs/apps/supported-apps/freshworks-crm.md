# Freshworks CRM

[Freshworks CRM](https://www.freshworks.com/crm/) is an online platform to get leads, boost customer engagement, drive deals to closure, and nurture existing customers. You can use it to view your customer’s interactions and automate your tasks. It also provides customized infographics to the user. The Freshworks App Connector manages and syncs contacts with other third-party apps.

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Freshworks account with Integry, here are a few things you need to learn about the Freshworks App Connector.

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Freshworks uses [API key+URL](https://support.integry.io/hc/en-us/articles/360022115853-Authentication-Types-Supported-in-Integry) authorization type. The API key and URL identify the end-user, and Integry uses this key to perform an API communication with Freshworks on behalf of that end-user.

You can find the above at Avatar > Settings > API Settings. Provide the API key as API Key and Bundle alias as URL.

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers used are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to Freshworks every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Freshworks acts as a trigger application) and perform an action in Freshworks, expect a 5-minute delay for the trigger to be received at Integry.

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Presently, there are no limitations of the Freshworks App Connector.
