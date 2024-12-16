# MailUp

[MailUp](https://www.integry.io/apps/mailup) is an easy-to-use platform for building customizable marketing campaigns through email, SMS, and other messaging apps. Many multinational, small, and medium businesses use MailUp to promote products and services. The MailUp App Connector helps you manage and sync email, email recipient, SMS, and SMS recipient with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your MailUp account with Integry, here are a few things you need to learn about the MailUp App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

MailUp uses [OAuth](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization type. The access token expires in 1 hour and gets refreshed automatically after expiration.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

The triggers in MailUp are [poll-based](https://support.integry.io/hc/en-us/articles/360021913374-Creating-Poll-Based-Triggers). Integry will send a request to MailUp every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which MailUp acts as a trigger application) and perform an action in MailUp, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

No triggers exist to check for any update of Email, SMS, and Recipient.
