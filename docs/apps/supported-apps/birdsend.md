# BirdSend

[BirdSend](https://www.integry.io/apps/birdsend) is a cloud-based platform for email marketing that enables content creators to streamline marketing operations through drip email campaigns, contact segmentation, and revenue tracking. You can set up sequence or drip email campaigns on a single page to automatically follow up with your subscribers and make sales. You can also use it to send broadcast emails. BirdSend helps you sync and manage broadcasts and contacts with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your BirdSend account with Integry, here are a few things you need to learn about the BirdSend App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

BirdSend uses the [OAuth](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization type. The access token expires in 60 days and refresh token is implemented.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers used in BirdSend are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to BirdSend every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which BirdSend acts as a trigger application) and perform an action in BirdSend, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

While creating a contact, a sequence has to be LIVE for it to appear in the dropdown.
