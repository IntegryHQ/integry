# ActiveCampaign

[ActiveCampaign](https://www.integry.io/apps/activecampaign) is an automated email marketing app. You can use it to send personalized content to your end-users based on their interests and past actions. It also helps to create automated workflows. The ActiveCampaign App Connector manages and syncs contacts with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Insightly account with ActiveCampaign, you can go through some basic specifications of the ActiveCampaign App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

ActiveCampaign uses an [API Key + URL](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) based authentication. Both the API key and the URL to your instance can be found inside the settings of your Active Campaign account.

#### &#x20;

#### Trigger Type <a href="#trigger-type-0-3" id="trigger-type-0-3"></a>

ActiveCampaign connector supports both [webhook-based](https://tray.io/documentation/connectors/triggers/webhook-trigger/) and [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/) triggers.

* Contact object has poll-based triggers. This means for the contact object, Integry will send a request to ActiveCampaign every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which ActiveCampaign acts as a trigger application) and perform an action in ActiveCampaign, expect a 5-minute delay for the trigger to be received at Integry.
* Campaign and Deal objects have webhook-based triggers. Therefore, for campaign and deal objects, Integry will receive the trigger instantly, as soon as an event occurs.

#### Limitations <a href="#limitations-0-4" id="limitations-0-4"></a>

The following types of custom fields are not supported for mapping in the triggers/queries:

* List box
* Dropdown
* Checkbox
* Radio
