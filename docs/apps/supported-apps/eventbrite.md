# Eventbrite

[Eventbrite](https://www.integry.io/apps/eventbrite) is an event management and ticketing website. It is used to search and manage all types of local events. With this tool, you can find or create an event in your area. It also allows you to manage a secure event ticketing process and analytics. The Eventbrite App Connector enables you to automatically sync the events created or tickets purchased with any other third-party app. &#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Eventbrite account with Integry, you can go through some specifications of the Eventbrite App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Eventbrite uses the [OAuth](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization method in which the access token doesn't expire. When you set up an integration, you need to log in and allow Integry to access your Eventbrite account.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

Eventbrite uses [webhook-based](https://tray.io/documentation/connectors/triggers/webhook-trigger/) triggers for Event and Ticket objects. Therefore, as soon as an event occurs, Integry will receive the trigger instantly.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Here are some of the limitations of the Eventbrite App Connector.

* An event's start and end time fields only accept time in UTC Format: YYYY-MM-DD hh:mm:ss.
* The timezones in events should be in Area/City timezone Format, which can be found [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
* Events with passwords cannot be marked as listed.
* The currency field accepts only the ISO 4217 currency code, which can be found [here](https://en.wikipedia.org/wiki/ISO_4217).
