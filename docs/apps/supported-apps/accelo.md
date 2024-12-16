# Accelo

[Accelo](https://www.integry.io/apps/accelo) is an online platform to manage your projects, services, sales, and retainers. It is an intelligent system for project management, invoices and payments, and CRM features. It helps in tracking time and progress, managing CRM contacts, dealing with client requests, and also coordinating with your team. The Accelo App Connector syncs and manages contacts with other third-party apps.&#x20;

### Authentication  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Accelo uses [Basic](../authentication/#h_01hyd00d8215cdess603v0q1qe) authentication.

### Triggers <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

Accelo uses poll-based triggers. Integry will send a request to Accelo every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Accelo acts as a trigger application) and perform an action in Accelo, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

In the Accelo App Connector, the custom fields are not supported in activities.
