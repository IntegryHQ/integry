# Notion

[Notion](https://www.notion.so/) is a note-taking software platform that enables companies to collaborate and manage global remote teams on the same page. It helps members of companies or organizations manage their knowledge for greater efficiency and productivity. Their customers include Pixar, loom, Typeform, codeacademy, and Blinklist. The Notion App Connector syncs and manages pages and database items with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Following are the basic specifications of the Notion connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Notion uses [OAuth ](https://support.integry.io/hc/en-us/articles/11112617800985-Supported-Authentication-Types)type authorization. The access token in Notion does not expire so token refresh is not needed.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

Notion uses [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/) triggers. Integry will send a request to Notion every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. When you set up an integration (in which Notion acts as a trigger application) and perform an action in Notion, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Currently, there are no limitations of the Notion App Connector.
