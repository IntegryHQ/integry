# Zoho Books

[Zoho Books](https://www.integry.io/apps/zoho-books) is a great online tool for bookkeeping your company's financial records and staying on top of business trends in the fintech world. It is also used as accounting software to manage your finances, automate your business workflows, track stock, and manage projects by helping you work jointly across departments. The Zoho Books App Connector enables you to sync all kinds of accounting entries between your Zoho Books account and other third-party app accounts.&#x20;

### Specifications <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Zoho Books account with Integry, here are a few things you need to learn about the Zoho Books App Connector.&#x20;

#### Authorization Type <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

&#x20;Zoho Books uses the [OAuth](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization method where the access token expires after an hour. A refresh token is used to generate a new access token after it expires. This won't have any impact on current integrations if implemented properly. When you set up an integration, you need to allow Integry to access your Zoho Books account.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

Zoho Books triggers are [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/). Integry will send a request to Zoho Books every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. When you set up an integration (in which Zoho Books acts as a trigger application) and perform an action in Zoho Books, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

As of now, following are the limitations of the Zoho Books App Connector.&#x20;

* Only correct email addresses can be used to test this App Connector.
* The _Update_ action for invoices and items only updates the created date and not the due date.
* While creating an invoice, the discount is only applicable when it is applied on the entity level.
* The discount should not exceed the invoice total.
* If the discount is applied on the item level, the 'discount before tax' checkbox must be checked while creating an invoice.
* At least one item must be selected to create an invoice.
* The stock keeping unit (SKU) of every item should be unique.
* We are only catering to US region, for now.
