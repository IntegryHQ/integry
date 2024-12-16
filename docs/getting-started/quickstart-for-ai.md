---
icon: sparkles
---

# Quickstart for AI

In this guide, we will use the [Integry.JS SDK](../apis-and-sdks/js-sdk-reference/) and [Integry Functions API](../apis-and-sdks/api-reference.md) to enable users to connect apps and invoke functions in those apps from your AI application.

Before you proceed, please [sign up](https://app.integry.io/accounts/register/v3/signup/?product=functions) for a free trial (if you haven't).

## Set up the SDK

Follow the steps [here](../apis-and-sdks/js-sdk-reference/#setting-up).

## Enable your users to connect apps

Your users have to first connect an app before you can invoke functions in that app. You could use or more of the following options.

### Shows apps in the Integry marketplace

Call the [`showApps()`](../apis-and-sdks/js-sdk-reference/#show-apps) method to easily show all (or some) available apps as a marketplace. Users will simply click an app to connect.

<figure><img src="../.gitbook/assets/Screenshot 2024-11-12 at 8.13.04 PM.png" alt="" width="375"><figcaption></figcaption></figure>

### Show apps in your own marketplace

Build your own apps marketplace and call the [`connectApp()`](../apis-and-sdks/js-sdk-reference/#connect-an-app) method when they click on an app.

<pre class="language-javascript"><code class="lang-javascript"><strong>integry.connectApp("slack").then((connectedAccountId) => {
</strong>  console.log("Connected to Slack with account ID:", connectedAccountId);
}).catch((error) => {
  console.error("Failed to connect to Slack:", error);
});
</code></pre>

### Connect apps when needed

Call [`isAppConnected()`](../apis-and-sdks/js-sdk-reference/#check-if-app-is-connected) method (when they try to use a function of an app) to check if the app is connected. If not, ask them to [`connectApp()`](../apis-and-sdks/js-sdk-reference/#connect-an-app).

```javascript
integry.isAppConnected("slack").then((result) => {
  if(result) {
    renderFunctionUI("slack-post-message");
  } else {
    integry.connectApp("slack").then((response) => {
      renderFunctionUI("slack-post-message")
    });
  }
}).catch((error) => {
  console.error("Failed to determine auth status:", error);
});
```

## Predict the function to invoke

Let's say your user says they want to _"send a message saying hello! to the random channel on slack"_.

In order to execute the `slack-post-message` function, you have to first predict that its the most relevant function.

You can simply pass the prompt to Integry and [predict the function with Integry AI](quickstart-for-ai.md#predict-the-function-with-integry-ai), or [predict it yourself](quickstart-for-ai.md#predict-the-function-yourself) (by listing all available functions).

### Predict the function with Integry AI

Call the [`functions/predict`](../apis-and-sdks/api-reference.md#predict-functions) API endpoint with `{"prompt: "<user_message>"}` to get the most relevant function. You can also have Integry [predict the arguments](quickstart-for-ai.md#predict-the-arguments-with-integry-ai).

```python
import requests

# Example 2: Basic Prediction
message = "send a message saying hello! to the random channel on slack"
response = requests.post(
    "https://api.integry.io/functions/predict/",
    json={"prompt": message},
    headers={
        "User-ID": "<string>",
        "App-Key": "<string>",
        "Hash": "<string>"
    },
)
function = response
```

Sample Response:

```json
{
    "functions": [
        {
            "name": "slack-post-message",
            "description": "Sends a message to a channel",
            "parameters": {
                "type": "object",
                "properties": {
                    "channel": {
                        "type": "string",
                        "description": "Select channel you want to post the message to. Call `slack-list-conversations` to get available channels"
                    },
                    "text": {
                        "type": "string",
                        "description": "The message text to be posted to Slack"
                    }
                },
                "required": [
                    "channel",
                    "text"
                ]
            }
        }
    ]
}
```

The `functions` array will be empty if Integry is unable to predict the function. You can ask the user to improve the `prompt` and try again.

### Predict the function yourself

Retrieve a list of available functions using the [`/functions/list`](../apis-and-sdks/api-reference.md#list-all-functions) endpoint and pass them to your AI model. Your model will predict the function to use.

If you need to call an endpoint that is not supported by Integry, you can make a [Passthrough Request](../apps/passthrough-requests.md).

## Prepare the arguments

In order to invoke a function, you have to first prepare the arguments based on the parameters that the function requires.

Similar to predicting the function, you can simply pass the prompt to Integry and [predict the arguments with Integry AI](quickstart-for-ai.md#predict-the-arguments-with-integry-ai), or [predict them yourself](quickstart-for-ai.md#predict-the-arguments-yourself) (using the function spec).

{% hint style="info" %}
**Parameter vs Argument**: A function parameter is the placeholder name of the type of input the function expects. The actual value passed is called the argument.
{% endhint %}

### Predict the arguments with Integry AI

Call the [`functions/predict`](../apis-and-sdks/api-reference.md#predict-functions) API endpoint with `predict_arguments=true` to get the most relevant function with populated arguments.

```python
# Example 1: Prediction with Populated Arguments
message = "send a message saying hello! to the random channel on slack"
response = requests.post(
    "https://api.integry.io/functions/predict/",
    params={"predict_arguments": "true"},
    json={"prompt": message},
    headers={
        "User-ID": "<string>",
        "App-Key": "<string>",
        "Hash": "<string>",
    },
)
function = response
```

Sample Response for Prediction with Populated Arguments:

```json
{
  "functions": [
    {
      "name": "slack-post-message",
      "description": "Sends a message to a channel",
      "parameters": {
            "type": "object",
            "properties": {
              "channel": {
                "type": "string",
                "description": "Select channel you want to post the message to. Call `slack-list-conversations` to get available channels"
              },
              "text": {
                "type": "string",
                "description": "The message text to be posted to Slack"
              }
            },
            "required": [
              "channel", "text"
            ]
          },
      "arguments": {
        "channel": "random",
        "text": "hello!"
      }
    }
  ]
}
```

Alternatively, if you predicted the function yourself and want Integry to predict the arguments, call the [`functions/<function_name>/get`](../apis-and-sdks/api-reference.md#get-a-function) API endpoint with `prompt` in the body to get the function with populated arguments.

```javascript
message = "send a message saying hello! to the random channel on slack"
response = requests.post(
    "https://api.integry.io/functions/slack-post-message/get/",
    json={"prompt": message},
    headers={
        "User-ID": "<string>",
        "App-Key": "<string>",
        "Hash": "<string>",
    },
)
function = response
```

The response is the same as above.

### Predict the arguments yourself

Call the [`functions/<function_name>/get`](../apis-and-sdks/api-reference.md#get-a-function) endpoint to get the function spec and pass it to your AI model. Your model will predict and populate the arguments.

You may need to make additional calls to [source functions](../functions/source-functions.md) to fetch options. Once you have the related data from the source function, use your model to pick the most relevant value from the set.

If you use predict the arguments with Integry AI, we handle this for you.

### Show the Function UI to the user

Before you invoke the function, if you want the user to confirm the predicted arguments, or provide one (or more) required arguments that could not be predicted, you can call [`showFunctionUI()`](../apis-and-sdks/js-sdk-reference/#show-the-function-ui) method to show the Function UI to the user (with pre-filled arguments, if any).

```javascript
const arguments = {
  "channel": "random",
  "text": "hello!"
}

integry.showFunctionUI("slack-post-message", arguments).then((result) => {
  console.log("Function parameters filled-in by the user:", result);
}).catch((error) => {
  console.error("Failed to load function UI:", error);
});
```

This will open the Function UI (with the pre-filled arguments) in a modal.

<figure><img src="../.gitbook/assets/Screenshot 2024-11-12 at 9.19.57 PM.png" alt="" width="375"><figcaption></figcaption></figure>

This method returns a `result` object with the filled-in arguments that you can use to invoke the function.

{% hint style="warning" %}
Functions that mutate data can potentially do irreversible damage. Even if you have predicted the arguments, consider always showing the Function UI to the user (with the predicted arguments) so they can confirm before you execute.
{% endhint %}

## Execute the function

### Call the function

Call [`invokeFunction()`](../apis-and-sdks/js-sdk-reference/#call-a-function) with the `<function_name>` and `arguments` object to execute the function.

```javascript
const arguments = {
  "channel": "random",
  "text": "hello!"
}

integry.invokeFunction("slack-post-message", arguments).then((result) => {
  console.log("Received response from Slack:", result);
}).catch((error) => {
  console.error("Failed to invoke function:", error);
});
```

### Process the result

The `result` object will have the response from the app if the function was executed (or error details if it wasn't).

In this case, you should see the following success response from Slack in the console:

<figure><img src="../.gitbook/assets/Screenshot 2024-11-12 at 9.50.38 PM.png" alt=""><figcaption></figcaption></figure>

That's it! You have enabled your users to connect apps and execute functions in those apps from your AI application using Integry Functions.

## Next steps

Try fetching data using a function like `pipedrive-get-all-persons` . It supports paginated calls so the result will include a `next_page` cursor that you will include in the arguments in the next invocation.
