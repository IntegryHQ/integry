# Snappy

[Snappy](https://www.integry.io/apps/snappy) is an online email ticketing, knowledge base, and support widget for your growing customer base. It works like a helpdesk with a quick email ticketing system. It helps track performances using custom reports. You can also create your customer self-help through the built-in knowledge base. Snappy lets your end-users insert knowledge base articles in your tickets and merge, reply or tag to multiple tickets at once. The Snappy App Connector manages and syncs tickets with other third-party apps.

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Snappy account with Integry, here are a few things you need to learn about the Snappy App Connector.

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Snappy uses the [Basic](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization type. The Basic auth type usually asks for your username and password and authenticates using those. If anything else is needed, we add the details for it in the auth popup.

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

It uses [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/) triggers. Integry will send a request to Snappy every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Snappy acts as a trigger application) and perform an action in Snappy, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Since the API does not support pagination, Import or Query is also not supported.
