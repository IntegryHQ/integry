---
hidden: true
icon: rectangle-vertical-history
---

# Solving the Problem of Order in Multiple Updates

When the webhooks sent to Integry are out-of-order, actions performed are also in the incorrect order. The received webhooks can be out of order due to a number of reasons like network congestion, service load levels, messages being sent of different machines, parallelism, etc.

To understand this, we will create a flow: "_When a task is updated in Asana, update a task in Google Tasks."_

If you change the title of a task in Asana, it will send several webhooks to Integry. After changing every few characters, a webhook will be received. The processing order of the webhooks is not guaranteed. To avoid this, Integry has a feature called "Force Update Order" in the Flow builder.

1. Go to Flows from the top menu.
2. Create a new flow.
3.  Click on the Flow Behavior icon from the right menu.

    <figure><img src="../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>
4.  Enable the _Force Update Order_ toggle.

    * Enabling this toggle will cause the updates received from the same object will be queued according to the order they are performed.

    <figure><img src="../.gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure>
5. There a a few conditions for this feature to work:
   * The Objects should be properly defined and mapped in the incoming endpoints for the triggers used in the flow for both apps.
   * Your app needs to provide a "Last Updated" timestamp. This should be an accurate time and should not overlap with any other webhook.
   * In the Object output for the endpoint, this timestamp should be mapped with the “last\_updated” property of the object.&#x20;
6. From Asana [API documentation](https://developers.asana.com/docs/#update-a-task), we can see that the timestamp associated with updating a task is found in the “created\_at” field.&#x20;
7. &#x20;So the “last\_updated” property will be mapped in the object similar to this:

<figure><img src="../.gitbook/assets/image (52).png" alt=""><figcaption></figcaption></figure>

Doing the above will provide our back-end engine with sufficient data to handle the ordering of updates.

Whenever Asana sends an update through a webhook, it also sends an associated timestamp, mapped with the Object property named “last\_updated.” This represents the time of the update very accurately (up to microseconds). So it will be different for each of the above example webhooks. Let’s see those webhooks with the associated timestamp now. Please note that this has been simplified for your understanding.

1. My first task - edi                          (“Last updated” : “09:49:43.2488”)
2. My first task - edited                     (“Last updated” : “09:49:43.8723”)
3. My first task - edited by                (“Last updated” : “09:49:44.3113”)
4. My first task - edited by John       (“Last Updated” : “09:49:45.0082”)

As soon as a webhook starts getting processed by our back-end execution engine, it divides the above four webhooks into two parts: one getting executed and the rest that are in the queue for execution. So let’s assume the 3rd webhook is processed first. The webhooks will now be:\
\
**In process:**

My first task - edited by

**In queue:**

1. My first task - edi                             (“Last updated” : “09:49:43.2488”)
2. My first task - edited                        (“Last updated” : “09:49:43.8723”)
3. My first task - edited by John          (“Last Updated” : “09:49:45.0082”)

From the webhooks not being executed, it checks the associated timestamps. Those webhooks whose timestamping are more recent than those being executed are kept in the queue for processing afterward. And the rest of the webhooks with an older timestamp than the current one are discarded. This is because as a newer webhook has been processed, it is assumed that all the older changes have already been included in it. So now this will be the status of webhooks.

**In process:**

My first task - edited by

**In queue:**

My first task - edited by John                  (“Last Updated”: “09:49:45.0082”)

After the processing of this webhook, the next webhook in the queue starts being processed. The same process will be followed if there is still more than one webhook in the queue. One of the webhooks is taken up for processing, and the timestamp for the remaining webhooks is checked. Similarly, the ones with an older timestamp are discarded, and the remaining ones with newer timestamps are again added to the queue for processing. This is how this process will carry on until no further webhooks remain in the queue.

Note that there will always be one webhook under process, and the rest are either in the queue or discarded. This rids us from losing data due to the uncertainty of order associated with processing multiple webhooks at a time. Because we drop older updates, we always convert partial updates to full updates by fetching the entire object with a [Get call](https://support.integry.io/hc/en-us/articles/360038024314-Using-Loop-Prevention-in-Templates). Because of this reason, each update translates to 3 tasks and is more expensive to run.

### Object and Integration combination <a href="#object-and-integration-combination-0-0" id="object-and-integration-combination-0-0"></a>

Forced Updated Order also ensures that the combination of Object ID and the Integration ID is maintained. This means that your updates for the same Object, but in different integrations, can be processed in parallel. Similarly, updates for two different Objects in the same integration can be processed simultaneously.

\
