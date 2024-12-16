# Pipedrive

[Pipedrive](https://www.integry.io/apps/pipedrive) is a cloud-based CRM that helps you prioritize deals, track performance, and predict revenue. The Pipedrive App Connector enables you to sync and manage people, deals, leads, activities, users, and organizations with other third-party app accounts.&#x20;

### Specifications <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Pipedrive account with Integry, you can go through some basic specifications of the Pipedrive App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Pipedrive uses an [API Key](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) for authorization. The end-user is identified by an API key, and Integry uses this key to perform an API request to Pipedrive on behalf of that end-user.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

Pipedrive uses [webhook-based](https://tray.io/documentation/connectors/triggers/webhook-trigger/) triggers for deal, user, organization, and person objects. For these objects, as soon as an event occurs, Integry will receive the trigger right away.On the other hand, [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/) trigger is used for the lead object. In this case, Integry will send a request to Pipedrive every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Pipedrive acts as a trigger application) and perform an action in Pipedrive, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Here are some of the limitations of the Pipedrive App Connector.

* While creating a lead, you must link it to at least one of the persons or one of the organizations. If none of them exist, then you need to create one.
* In leads, the expected closing date needs to be provided in ISO 8601 format: YYYY-MM-DD.
* A deal must always be linked to a person, organization, or both.
* The probability of deals will only be shown when deal property for the pipeline of the deal is enabled.
* Pipedrive has an authenticating rate limit according to your account, details of which are:
  1. **Essential**: 20 requests per 2 seconds per API token
  2. **Advanced**: 40 requests per 2 seconds per API token
  3. **Professional**: 80 requests per 2 seconds per API token
  4. **Enterprise**: 120 requests per 2 seconds per API token
