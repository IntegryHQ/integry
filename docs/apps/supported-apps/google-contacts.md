# Google Contacts

[Google Contacts](https://contacts.google.com/) is an online platform that allows you to manage your contacts and keep track of all your conversations. You can use it to manage all your contacts online in one place, review your recent conversations and create notes about your contacts. It also lets you save the details of contacts that you email the most. The Google Contacts App Connector syncs and manages contacts with other third-party apps.&#x20;

### Specifications  <a href="#specifications-0-0" id="specifications-0-0"></a>

Before you connect your Google Contacts account with Integry, here are a few things you need to learn about the Google Contacts App Connector.&#x20;

#### Authorization Type  <a href="#authorization-type-0-1" id="authorization-type-0-1"></a>

Google Contacts uses the [OAuth ](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry)authorization type.The auth token expires after 1 hour and a new token is generated via refresh token.&#x20;

#### Trigger Type <a href="#trigger-type-0-2" id="trigger-type-0-2"></a>

It uses [poll-based](https://www.testpreptraining.com/tutorial/describe-polling-triggers-and-their-usage/) triggers. Integry will send a request to Google Contacts every 5 minutes to collect data. In case of an occurrence of selected events, a trigger will be received at Integry with the required payload. Therefore, when you set up an integration (in which Google Contacts acts as a trigger application) and perform an action in Google Contacts, expect a 5-minute delay for the trigger to be received at Integry.&#x20;

### Limitations <a href="#limitations-0-3" id="limitations-0-3"></a>

Following are the limitations of the Google Contacts App Connector. User's refresh token will stop working when:

1. The user has revoked your app's access (ref:[https://support.google.com/accounts/answer/3466521#remove-access](https://support.google.com/accounts/answer/3466521#remove-access))
2. The refresh token has not been used for six months.
3. The user account has exceeded the maximum number of granted (live) refresh tokens. The limit is 100 live refresh tokens. After the 101 is added, it will revoke the first refresh token
