# Mailjet

[Mailjet](https://www.integry.io/apps/mailjet) is a cloud-based email delivery and tracking system which allows users to send marketing and transactional emails. The app is easy-to-use and enables you to design and send out automated email marketing campaigns and newsletters. The Mailjet App Connector can be used to manage and sync campaigns, contacts, and contact lists with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Following are the basic specifications of the Mailjet App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Mailjet uses [API Key+secret](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) type authorization. The end-user is identified by an API key+secret, and Integry uses this key to perform an API request to Mailjet on behalf of that end-user.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

[Poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/) triggers are used in Mailjet. Integry will send a request to Mailet every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Mailjet acts as a trigger application) and perform an action in Mailjet, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Currently, there are no limitations of the Mailjet App Connector.
