# Mailchimp Transactional

[Mailchimp Transactional](https://www.integry.io/apps/mailchimp-transactional) is a tool to send transactional emails (password resets, order placement, welcome messages) triggered by user actions, personalized 1:1 messages, and targeted e-commerce emails. This app, also known as Mandrill, is a platform for email marketing automation and can be used to send event-driven messages to your customers. You can also use it to design one-to-one personalized e-commerce emails. The Mailchimp Transactional App Connector syncs and manages templates and emails with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Mailchimp Transactional account with Integry, here are a few things you need to learn about the Mailchimp Transactional App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

In order to use Rest APIs, users need to authenticate via [API key](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry). Users can [generate](https://mailchimp.com/developer/transactional/guides/quick-start/#generate-your-api-key) a new [API key](https://mandrillapp.com/settings) from the Mandrill App. The API key is included in the request body. Integry uses the API key to identify users.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

Mailchimp Transactional supports [Webhook-based](https://support.integry.io/hc/en-us/articles/360021913434-Creating-Webhook-Triggers) triggers for specific topics. Therefore, as soon as an event occurs, Integry will receive the trigger instantly.

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Presently, there are the following limitations of the Mailchimp Transactional App Connector:

* Sorting is not supported; thus, poll-based triggers cannot be implemented.
* Pagination is also not supported, so we cannot implement either queries or custom-sort.
* Only the following events are supported by Webhooks:
  * Message Is Sent
  * Message Is Delivered
  * Message Is Delayed
  * Message Is Bounced
  * Message Is Soft-Bounced
  * Message Is Opened
  * Message Is Clicked
  * Message Is Marked As Spam
  * Message Recipient Unsubscribes
  * Message Is Rejected
  * Rejection Denylist Changes
  * Rejection Allowlist Changes

\
