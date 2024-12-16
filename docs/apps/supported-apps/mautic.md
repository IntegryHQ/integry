# Mautic

Integry supports the flowing actions of Mautic.

#### Actions <a href="#h_01hr56vpze824xf8dyw4e604x7" id="h_01hr56vpze824xf8dyw4e604x7"></a>

| **Name**     | **Method** | **Description**           |
| ------------ | ---------- | ------------------------- |
| Create Email | POST       | Creates a new email       |
| Update Email | PATCH      | Updates an existing email |

For more, please see [Mautic API docs](https://developer.mautic.org/).

#### Authorization <a href="#h_01hr556ap450c8s3d5hf8vc37f" id="h_01hr556ap450c8s3d5hf8vc37f"></a>

Mautic uses [Basic with URL](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization type. The end-user is identified through a combination of basic authentication (username and password) and a specific URL. Integry uses these credentials to perform API requests to Mautic on behalf of the end-user.

&#x20;

#### FAQs <a href="#id-01hw60a621etfhwyaqdtv9jkj2" id="id-01hw60a621etfhwyaqdtv9jkj2"></a>

**Why was my campaign created, but there was no HTML inside it?**\
This issue occasionally occurs due to a problem with the Mautic API. Since this is a problem on Mautic's end, there's not much we can do to resolve it directly. However, this issue is rare, and retrying after some time usually resolves it. We have reported this problem to Mautic for further investigation.
