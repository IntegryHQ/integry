---
icon: left-right
---

# Create a two-way flow

### The Problem - Integration Loops <a href="#h_01hnjrheq166g66dycd8kgarav" id="h_01hnjrheq166g66dycd8kgarav"></a>

In a two-way sync integration, a change in one app is reflected in the other app and vice versa. This brings some problems with it that cannot be left overlooked while creating integration Flows.&#x20;

An update or addition of data in one app can cause continuous back and forth updates between the two synced apps, making it an infinite cycle.&#x20;

Let’s better understand this with an example.&#x20;

Consider you have created an integration that syncs your contacts between [Sendinblue](https://www.sendinblue.com/) and [MailChimp](https://mailchimp.com/). Now let’s say you update a contact’s information in Sendinblue. This will [Trigger](../../getting-started/key-concepts.md#h_01hnbh26nyfh3rkp2jd3gwwcnp) a response from Sendinblue in the integration that will cause the contact to be updated in MailChimp as well.&#x20;

However, the reflection of this update in MailChimp will again Trigger a response. For the two-way sync to work, this update will again have to reflect in the first app. &#x20;

This is because the integration listens to all update events, and the app sends these events to their respective Triggers even if we’re the ones doing the updates. This will cause an infinite loop of back and forth updates of that contact in both apps.&#x20;

A similar problem will arise in the case of contact creation that is synced both ways.&#x20;

### The Loop Prevention Feature <a href="#h_01hnjrheq1b591wkbm5t9kkash" id="h_01hnjrheq1b591wkbm5t9kkash"></a>

To ensure you don’t get hindered by loops in your integrations, we bring you the loop prevention feature in the Flow builder. With one single click, your Flow will become free of any potential loops that can be originated. You can enable loop prevention for your Flow with the toggle button found in the Flow UI configuration section, as seen below.&#x20;

<figure><img src="../../.gitbook/assets/image (45).png" alt="" width="375"><figcaption></figcaption></figure>

When loop prevention is turned on, its corresponding backend algorithms become available to be used in Flows. They are designed specifically to support the smooth execution of two-way sync use-cases in Flows by making sure no loops are introduced. Let’s see the mechanism behind this feature for the “Update” and “Create” use-case examples for contacts in Flows.

### Requirements for Loop Prevention Feature to Work <a href="#h_01hnjrheq155wypdbnhjpry78h" id="h_01hnjrheq155wypdbnhjpry78h"></a>

Before using loop prevention in a specific Flow, you need to set up a few things. These are the core requirements without which loop prevention is impossible.&#x20;

1. Triggers for the required operations in a use-case should be present in the Flow for both apps. The “contact updated” and “contact created” Triggers are to be used for the update and create use-cases, respectively.
2. The Actions and Triggers used in the Flow should be using Objects to handle the data.&#x20;
3. The apps being used in your Flow should have a separate “Get Record” Action implemented. This Action applies a Get call on an input Object. This is the Object on which “Update” or “Create” is being performed in the Flow. The Get call fetches the latest information on the Object (e.g., contact) and the associated data from the respective app. This “Get Record” Action is implicitly used on the backend once you enable loop prevention in the Flow. You can have this Action activity set up in your app settings and configure the Get call in the Object section.

&#x20; 4\. The **loop prevention** toggle button in the Flow should be ON.

### The “Update” Use-Case <a href="#h_01hnjrheq2knq2hdgjq012wtxe" id="h_01hnjrheq2knq2hdgjq012wtxe"></a>

The example mentioned above will have four major steps for the update use-case. There will be a Trigger for when a contact is updated in Sendinblue and an Action that will execute in response to this Trigger that will update the subscriber in MailChimp.&#x20;

Since this is a two-way sync Flow, there will be steps for this process in the reverse direction as well. A Trigger for the subscriber being updated in MailChimp and an Action to update that contact in Sendinblue.&#x20;

Please note that only the relevant Flow steps are shown in the examples for this document for simplicity and user’s understanding.

#### **1**. **Contact Updated in Sendinblue** <a href="#h_01hnjrheq2jfe2tnnpwgmxrah7" id="h_01hnjrheq2jfe2tnnpwgmxrah7"></a>

When you update a contact in Sendinblue, it will execute the Trigger at the first step of the Flow in the image shown below. As a result of this Trigger, the Action to update that subscriber in MailChimp will be performed at the next step. &#x20;

<figure><img src="../../.gitbook/assets/image (46).png" alt="" width="375"><figcaption></figcaption></figure>

&#x20;

#### **2**. **Subscriber Updated in MailChimp** <a href="#h_01hnjrheq2zvfece2jjyvbk1br" id="h_01hnjrheq2zvfece2jjyvbk1br"></a>

Continuing the above example, it has already been mentioned that this Flow is a two-way sync between apps. So there will also exist a Trigger in this Flow for when a subscriber is updated in MailChimp and an Action to update that contact in Sendinblue. These steps are shown below.&#x20;

<figure><img src="../../.gitbook/assets/image (47).png" alt="" width="375"><figcaption></figcaption></figure>

In our current example, the contact was updated in Sendinblue and has already been updated in MailChimp. The Trigger shown above will now be executed. However, this time, the process will not continue to the Action as the update has already been performed. Thus, the loop will be discontinued. All of this is controlled through the backend algorithm.&#x20;

### The “Create” Use-Case <a href="#h_01hnjrheq2gnzng0fr5yqfd8zm" id="h_01hnjrheq2gnzng0fr5yqfd8zm"></a>

Along with the “update contact” use-case, loops can arise from the “create contact” use-case as well. For loop prevention in this use case, we implement a similar type of algorithm as talked above. This use-case will again have four major steps in the Flow. Let’s see the details below.&#x20;

#### **1.** **Contact created in Sendinblue** <a href="#h_01hnjrheq2t88g531zk0m6yqbe" id="h_01hnjrheq2t88g531zk0m6yqbe"></a>

When you create a contact in Sendinblue, it will execute a Trigger for “contact created in Sendinblue.” Let’s again make this the first step of the Flow, as shown in the image below. As a result of this Trigger, the Action to create that subscriber in MailChimp will be performed at the next step.&#x20;

<figure><img src="../../.gitbook/assets/image (48).png" alt=""><figcaption></figcaption></figure>

#### &#x20;**2. Subscriber created in MailChimp** <a href="#h_01hnjrheq2zz9qgrtae22xkfkn" id="h_01hnjrheq2zz9qgrtae22xkfkn"></a>

For two-way sync in contact creation, there will also exist a Trigger in the Flow for when a subscriber is created in MailChimp and an Action to create that contact in Sendinblue. Let's assume they are the steps shown below.&#x20;

<figure><img src="../../.gitbook/assets/image (49).png" alt=""><figcaption></figcaption></figure>

Once again, as the contact has already been created in both the apps, the above Trigger will not prompt the Action step to run, and the process will be discontinued after the contact is created in both apps once.&#x20;

So the loop will be prevented. Similar to the above examples, you can use the loop prevention feature in all your two-way operations in the Flow that might prompt a loop to occur.&#x20;

Just make sure you have fulfilled the requirements for it mentioned in this article. Using the loop prevention feature may affect your task usage for the integration.&#x20;
