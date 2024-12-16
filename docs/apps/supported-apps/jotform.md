# Jotform

Integry supports a number of triggers and actions of Jotform.

#### Triggers <a href="#h_01hr556ap5m0d97s0v2hv9bk41" id="h_01hr556ap5m0d97s0v2hv9bk41"></a>

| **Name**                | **Type** | **Description**                            |
| ----------------------- | -------- | ------------------------------------------ |
| Form Submitted          | Polling  | Triggers when a form is submitted          |
| Form Submission Updated | Polling  | Triggers when a form submission is updated |

For more, please see [Jotform API docs](https://api.jotform.com/docs/). If you're not sure how triggers work in Integry, go [here](https://support.integry.io/hc/en-us/articles/29484874325017).

#### Actions <a href="#h_01hr56vpze824xf8dyw4e604x7" id="h_01hr56vpze824xf8dyw4e604x7"></a>

| **Name**               | **Method** | **Description**               |
| ---------------------- | ---------- | ----------------------------- |
| Create Form Submission | POST       | Creates a new form Submission |

For more, please see [Jotform API docs](https://api.jotform.com/docs/).

#### Authorization <a href="#h_01hr556ap450c8s3d5hf8vc37f" id="h_01hr556ap450c8s3d5hf8vc37f"></a>

Jotform uses [API Key](https://support.integry.io/hc/en-us/articles/11112617800985-Authentication-Types-Supported-in-Integry) authorization type. The end-user is identified by an API key, and Integry uses this key to perform an API request to ActiveTrail on behalf of that end-user.
