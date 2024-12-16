# Coda

[Coda ](https://www.integry.io/apps/coda)is a tool that combines features of documents, spreadsheets, databases, notes, and project management tools. It enables you to collaborate with your team and populate your documents with text and infographics. You can use it to add text, reports, graphs, invoices, etc., and organize them into folders. It has adaptive views to enable your team or manager to work off the same data. The Coda App Connector syncs and manages documents with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Coda account with Integry, here are a few things you need to learn about the Coda App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Coda uses the [API key](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization method. An API key identifies the end-user, and Integry uses this key to communicate with Coda's API on behalf of that end-user.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

Coda triggers are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to Coda every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. When you set up an integration (in which Coda acts as a trigger application) and perform an action in Coda, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

The documents can not be updated through the API.
