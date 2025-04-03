---
icon: right-from-bracket
---

# Sync data FROM another app to your app

A Flow moves data from one app to another. A Flow can have one or more Triggers that execute steps when run. Flows can sync data from or to your app from another app.

In this quick tutorial, we will build and run a flow that sends every new subscriber in a Mailchimp audience to your API endpoint.&#x20;

To make things interesting, you will get to map custom fields in your Mailchimp account to fields of the API endpoint.

{% hint style="info" %}
**Note:** You will need to login to a Mailchimp account, sign up for a [free trial](https://login.mailchimp.com/signup/?plan=free_monthly_plan_v0\&subscribers=500)
{% endhint %}

#### Create a flow <a href="#h_01hev188pb696nwg83zdnc0e1n" id="h_01hev188pb696nwg83zdnc0e1n"></a>

1. Navigate to Flows and click [Create a Flow](https://app.integry.io/platform/flow/create) button
2.  Select the trigger: "Subscriber Created" in Mailchimp.\


    <figure><img src="../../.gitbook/assets/Screenshot 2024-10-27 at 8.21.35 PM.png" alt=""><figcaption></figcaption></figure>
3.  Click "Add a step" and select "HTTP Call". We will use this to call your API with the Mailchimp Subscriber data. If you don't have an API, Integr can write to your database, or Integry's own local store and expose an API.



    <figure><img src="../../.gitbook/assets/Screenshot 2024-10-27 at 8.22.21 PM.png" alt=""><figcaption></figcaption></figure>
4. Configure the HTTP Call: in this example, we will use [webhook.site](https://webhook.site/) as a sample API endpoint
   1.  On webhook.site: Click "Copy" to copy the unique URL\


       <figure><img src="../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>
   2.  Back in Integry's HTTP Call: Set the method HTTP call method to POST, and paste the URL.&#x20;

       <figure><img src="../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>
   3. Switch to the "Body" tab of the HTTP call
   4. Define the JSON payload. In this example, we will send three fields to the API endpoint.
      1. Paste this JSON in the body:&#x20;
         * ```json
           {
              "email":"",
              "first_name":"",
              "last_name":""
           }
           ```
      2. Map the email field from the trigger to the body.
         1.  Place your cursor in between the "" you just added, and click +. The mapping menu will popup.&#x20;

             <figure><img src="../../.gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>
         2. Click "Subscriber Created" under the Subscriber Created (Block)
         3.  Click the ">" next to "Out" to access the output.&#x20;

             <figure><img src="../../.gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure>
         4.  In this example, event type and timestamp are at the root, while the data is in an array. Click "data" to open the array, and click "email".

             <figure><img src="../../.gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>
         5.  Confirm that the body looks like this: \


             <figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>
         6. Now would be a good time to rename the flow and save it.
      3. Add the other two fields to the setup form.
         1. Click "Add fields to setup form..." at the bottom of the body container.
         2.  Unselect "email" because we already mapped it. We want the user to map the other two at setup time. You can rename the titles if you want.&#x20;

             <figure><img src="../../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>
         3. Click "Add fields".
         4.  Click "Setup Form" in the left pane, and go to the second page. Instead of "Acme Co.", it should have your app's name. You will see the two fields that you just added.&#x20;

             <figure><img src="../../.gitbook/assets/image (33).png" alt=""><figcaption></figcaption></figure>
         5. Click "First Name" or "Last Name". You can see that the fields have been automatically configured to allow users to map fields from the trigger step. You don't need to do anything.
         6.  Go back to "Trigger Blocks" and to the "Body" tab in "HTTP Call". You will see that the fields in the setup form (that you just added) have been automatically wired as the values of the fields to be sent to the API endpoint. You don't need to go anything here either. \


             <figure><img src="../../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>
   5. Now, simply Click "Test" to run this HTTP call to confirm that it's working.&#x20;
      1.

          <figure><img src="../../.gitbook/assets/image (37).png" alt=""><figcaption></figcaption></figure>
      2.  Integry will ask you to provide an API key. Enter "123" and click Proceed.



          <figure><img src="../../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

          * You see this screen because Integry is assuming that webhook.site is your app, and the API call to the endpoint has to be authenticated with your credentials. Don't worry, your users won't have to give the API key in this manner because you will pass the key through the SDK when you embed the widget.
   6.  You can see the request and response below.&#x20;

       * "email" contains a sample value from the trigger's output that you mapped.
       * "first\_name" and "last\_name" are empty because they've not been mapped as yet. You will get to map them (like your users) in the next section when you setup an integration of this flow.

       <figure><img src="../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>
5. Save the flow and go back to the Flows list.

That's it! The flow is ready to use.

#### Set up an integration of the flow <a href="#h_01hev2zavgk1s46ekb4mgvr37g" id="h_01hev2zavgk1s46ekb4mgvr37g"></a>

1. Click "Embed". You'll see the flow you created. In this example, that's "Sync new subscribers from Mailchimp".
2. Click "Setup and enable".
3. Login to Mailchimp.
4. Configure Mailchimp.
   1.  Select the audience you want to monitor for new subscriber and click Next.&#x20;

       <figure><img src="../../.gitbook/assets/image (41).png" alt=""><figcaption></figcaption></figure>
5. Configure Acme Co.
   1.  Map Acme Co. fields to Mailchimp fields.&#x20;

       <figure><img src="../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>
6. Click Save to initialize the integration.

Almost there! The integration is now live and ready to be triggered.

### Run the integration <a href="#h_01hexket3180hrha4jn5ybpjw5" id="h_01hexket3180hrha4jn5ybpjw5"></a>

In this example, we are using a Mailchimp trigger so steps 1-5 will happen in Mailchimp.

1. Open [mailchimp.com](https://mailchimp.com/) in a browser.
2. Log in with the same user account you used while setting up the integration.
   1. If you have multiple team accounts, select the same team account you selected earlier.
3. Click "Add subscriber".
4.  Fill out the form with a new user's details.&#x20;

    <figure><img src="../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>
5.  Give permission to email the user, and click Subscribe.

    <figure><img src="../../.gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>
6. Go back to webhook.site. A new request with the details you entered should have been received.
7. You can also see how the run actually executed by clicking the count of users against this flow (in the flows list), drill down to runs, and then steps.

We're done! You just created a flow between two apps, setup an integration of the flow, and the integration ran.

#### Next steps <a href="#h_01hneavbezh46z9tyxsmgjwztw" id="h_01hneavbezh46z9tyxsmgjwztw"></a>

* Make flows that [send data to another app](sync-data-to-another-app-from-your-app.md), import data from an app, export data to an app, or even sync both ways between another app and your app.&#x20;
* [Embed the Integry widget](broken-reference) in your app so your users can set up integrations from within your app

\
