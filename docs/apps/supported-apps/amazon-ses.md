# Amazon SES

[Amazon Simple Email Service (SES)](https://www.integry.io/apps/amazon-ses) is an email service that enables developers to send mail from within any application. It can easily be configured to support several email use cases, including transactional, marketing, or mass email communications. It offers flexible IP deployment and email authentication options to help drive higher deliverability and protect the sender's reputation. The Amazon SES App Connector helps you sync and manage email templates with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Amazon SES account with Integry, here are a few things you need to learn about the Amazon SES App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Amazon SES uses [API Key,](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) API Secret, and API Region type of authorization, where you have to provide both your API key and secret along with your AWS region.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

Amazon SES supports [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/) triggers for email templates. Integry will send a request to Amazon SES every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Amazon SES acts as a trigger application) and perform an action in Amazon SES, expect a 5-minute delay for the trigger to be received at Integry.

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Currently, the name of an email template cannot be updated.
