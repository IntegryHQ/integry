# Sendy

Integry supports the flowing actions of Sendy.

#### Actions <a href="#h_01hr56vpze824xf8dyw4e604x7" id="h_01hr56vpze824xf8dyw4e604x7"></a>

| **Name**        | **Method** | **Description**        |
| --------------- | ---------- | ---------------------- |
| Create Campaign | POST       | Creates a new campaign |

For more, please see [Sendy API docs](https://sendy.co/api).

#### Authorization <a href="#h_01hr556ap450c8s3d5hf8vc37f" id="h_01hr556ap450c8s3d5hf8vc37f"></a>

Sendy uses [API Key](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization type. The end-user is identified by an API key, and Integry uses this key to perform an API request to Sendy on behalf of that end-user.

&#x20;

#### FAQs <a href="#id-01hw60a621etfhwyaqdtv9jkj2" id="id-01hw60a621etfhwyaqdtv9jkj2"></a>

**Why am I unable to send campaigns on Sendy?**\
If you're having trouble sending campaigns with Sendy, ensure that your account is fully configured. Initially, you need to set up your Sendy installation correctly by connecting it to an SMTP service, as Sendy does not have built-in capabilities to send emails on its own. Ensure that all SMTP settings are correctly entered in the 'Settings' section of your Sendy dashboard. This setup is essential for Sendy to function properly and send out campaigns.
