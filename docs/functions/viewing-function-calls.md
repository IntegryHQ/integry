---
icon: list-check
---

# Viewing Function Calls

## See Function Calls

Every function call you make will appear in the calls log in the Integry app.

<figure><img src="../.gitbook/assets/Screenshot 2024-11-19 at 11.50.34 AM.png" alt=""><figcaption></figcaption></figure>

## Steps in a Function Call

Click a function call to see the steps executed under-the-hood by Integry.

* The **first step** always represents the function call itself.
* The next set of **execution steps** represent the steps executed by Integry to execute the function.
  * In a function like `slack-post-message`, there will only be an HTTP Call.
  * In a function that supports pagination like `pipedrive-get-all-persons`, there will be multiple steps.
* The **last step** always represents the function call response.

{% tabs %}
{% tab title="slack-post-message" %}
<figure><img src="../.gitbook/assets/Screenshot 2024-11-19 at 11.57.28 AM.png" alt=""><figcaption></figcaption></figure>


{% endtab %}

{% tab title="pipedrive-get-all-persons" %}
<figure><img src="../.gitbook/assets/Screenshot 2024-11-19 at 12.44.08 PM.png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

### Function Call

&#x20;Click the step to see the function parameters and the arguments passed in the function call.

<figure><img src="../.gitbook/assets/Screenshot 2024-11-19 at 12.07.17 PM.png" alt=""><figcaption></figcaption></figure>

### Execution steps

Click a step to see execution details.

<figure><img src="../.gitbook/assets/Screenshot 2024-11-19 at 12.18.13 PM.png" alt=""><figcaption></figcaption></figure>

### Return

Click the step to see the function call response.

<figure><img src="../.gitbook/assets/Screenshot 2024-11-19 at 12.48.57 PM.png" alt=""><figcaption></figcaption></figure>
