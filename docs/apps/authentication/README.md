---
icon: key
---

# Authentication

When your user click an app's name in the Integry marketplace, or you directly call [`connectApp()`](../../apis-and-sdks/js-sdk-reference/#connect-an-app) or [`showApp()`](../../apis-and-sdks/js-sdk-reference/#show-an-app-beta), Integry asks the user to connect their account in that app. Once they connect, Integry automatically adds the user's auth credentials in onwards HTTP requests to that app.

The authentication process for some apps may be as Basic as asking for a username and password that Integry will include in the Headers of HTTP requests. Many apps today require using the [OAuth 2.0](https://oauth.net/2/) protocol to get an access token that Integry will include in the HTTP request. If the token has expired, Integry will refresh the token and retry the request.

## Authentication types

### OAuth 2.0

#### Use Integry's developer app for OAuth 2.0

By default, most apps that use OAuth 2.0 for authentication are configured to use Integry's built-in developer app. This means that we don't make you set up a new developer app to perform actions in that app. That said, whenever you're ready to do it, you can simply switch to [using your developer app for OAuth 2.0.](./#use-your-developer-app-for-oauth-2.0)

_Note: Some apps like Zoom can only be connected with your developer app. Follow the same steps below to provide your developer app credentials and you're all set._

#### Use your developer app for OAuth 2.0

In this tutorial, we white-label OAuth 2.0 for HubSpot by creating a developer app in your HubSpot developer account. Skip to step 10 if you already have a developer app. We don't have guides for other apps but the steps will be quite similar.

1. Go to HubSpot's [developer site](https://app.hubspot.com/developer/).
2. Enter your login credentials.
   * If you don't have a developer account on HubSpot, you can create [one for free](https://developers.hubspot.com/get-started).
3.  Go to Apps.

    <figure><img src="../../.gitbook/assets/image (64).png" alt=""><figcaption></figcaption></figure>
4.  Click "Create app".

    <figure><img src="../../.gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>
5.  In the "App Info" tab, enter your app's name.

    * The name you enter here will appear on the authentication and authorization screens when your users will set up a flow with HubSpot.

    <figure><img src="../../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>
6.  Upload your app's logo.

    * The logo you upload here will appear on the authentication and authorization screens when your users will set up a flow with HubSpot.

    <figure><img src="../../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>
7.  Go to the Auth tab and enter [`https://app.integry.io/auth/redirect/`](https://app.integry.io/auth/redirect/) as the redirect URL.

    * When your users connect their HubSpot account while setting up the integration, they will be taken to HubSpot's authentication server. After being verified by the authentication server, they will be redirected to the above URL.&#x20;

    <figure><img src="../../.gitbook/assets/image (68).png" alt=""><figcaption></figcaption></figure>
8. Scroll down to select scopes.
   * Scopes will determine the permissions to read/write data from/in your HubSpot account.
   * Select the following scopes:
     * `crm.schemas.deals.readcrm.objects.contacts.readcrm.objects.contacts.writecrm.objects.companies.readcrm.objects.companies.writecrm.lists.readcrm.lists.writecrm.objects.deals.readcrm.objects.deals.writecrm.schemas.contacts.readcrm.schemas.companies.readcontentoauth`
   *   Copy each scope and paste it in the search bar.

       <figure><img src="../../.gitbook/assets/image (69).png" alt=""><figcaption></figcaption></figure>
   *   Select the "read" or "write" permission by clicking the checkbox. Your selected scope will be added.

       <figure><img src="../../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>
   *   This is how the permissions section will appear on the authorization screen for your users.

       <figure><img src="../../.gitbook/assets/image (71).png" alt=""><figcaption></figcaption></figure>
9.  Click on Create App. When your app is created, a "Client ID" and "Client secret" will be generated for your developer app. Go to the "Auth" tab to copy your Client ID and Client secret. You will use these credentials while configuring white-labeled OAuth in Integry.

    <figure><img src="../../.gitbook/assets/image (72).png" alt=""><figcaption></figcaption></figure>
10. Go to the 'Flows' tab.
11. Click on the three-dots menu for flow with HubSpot.
12. Click on 'Auth Settings.
13. Enter your Client ID, Client secret, and scopes in the respective fields.
    * The scopes you enter here should match with the scopes you select in your developer app.
    *   Copy scopes from here: `content oauth crm.schemas.deals.read crm.objects.contacts.write crm.objects.companies.write crm.lists.write crm.objects.companies.read crm.lists.read crm.objects.deals.read crm.schemas.contacts.read crm.objects.deals.write crm.objects.contacts.read crm.schemas.companies.read`

        <figure><img src="../../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>
14. Click Tes&#x74;**.**
    * As a result, an authentication UI opens up in your browser.
    *   After a successful login, an authorization UI opens in your browser. The permissions you see here are the scopes you selected while creating your app. Click on Connect app.

        <figure><img src="../../.gitbook/assets/image (74).png" alt=""><figcaption></figcaption></figure>
15. If your test is successful, you'll see a green tick.

    <figure><img src="../../.gitbook/assets/image (75).png" alt=""><figcaption></figcaption></figure>
16. In case of an error, you'll see an error icon, click 'See details' to view error details.

    *   You'll see the steps performed by Integry on behalf of Doneday to authenticate and authorize the user. Check the Network Code to see which step failed.

        <figure><img src="../../.gitbook/assets/image (77).png" alt=""><figcaption></figcaption></figure>
    * Click "View Payload" to see the details of the API call and troubleshoot accordingly. Here are some potential error messages you may encounter:
      * `invalid_grant`: Indicates that the OAuth client key or secret is not properly configured with the necessary grants or scopes
      * `BAD_CLIENT_SECRET`: Indicates an invalid or incorrect client secret was provided
      * `Unauthorized`: Indicates that the client key or secret provided is not authorized to perform the requested action

    <figure><img src="../../.gitbook/assets/image (76).png" alt=""><figcaption></figcaption></figure>
17. Click on Enable to enable white-labeled OAuth in your flows.

    <figure><img src="../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

Once enabled, any new users who set up integrations with Hubspot will see your app's branding (instead of Integry) on the Hubspot authorization screen, and we will use your developer app when we call Hubspot's API on their behalf. However, existing integrations will continue to use Integry's developer app because that's what the existing users used to login. If/When they disconnect their Hubspot account and reconnect, they will also login using your developer app (and not see Integry).

### API-Key <a href="#h_01hyd00d82nvkf3cpgaejgm51m" id="h_01hyd00d82nvkf3cpgaejgm51m"></a>

API-key based authorization type is known for its simplicity. The end-user signs into TPA, gets their API key, and copies it in their application to use. API-key is the name given to a secret token that is submitted to a web service along with a request. The key identifies the end-user in the TPA and performs an API request on behalf of that end-user. For the scope of Integry, once you enter your API-key while authenticating, Integry will consume your API-key for future communication.&#x20;

API-key based authentication is not a highly recommended auth type due to security loopholes. As an entity gets hold of the end-user's API key, they have to keep it safe (just like a password), because it maybe dangerous if an unauthorized entity accesses it.&#x20;

### API-Key and Secret <a href="#h_01hyd00d824zawdddcmr4dza8f" id="h_01hyd00d824zawdddcmr4dza8f"></a>

This is a modification of API-key. A combination of API-key and API Secret is used for authentication. It works the same as API-key. When an application is registered with the API, it generates a key and a secret for that application. Whenever the application makes a request, its request consists of the key and secret as well.&#x20;

### API-Key with URL <a href="#h_01hyd00d824y35s559v9fm5zcx" id="h_01hyd00d824y35s559v9fm5zcx"></a>

This works the same as API key, but the API calls are sent to the URL specified by the end-user while they're authenticating their TPA accounts.&#x20;

### Basic <a href="#h_01hyd00d8215cdess603v0q1qe" id="h_01hyd00d8215cdess603v0q1qe"></a>

It only requires a username and password for authentication. It is the least recommended way of authentication.

### Basic with URL <a href="#h_01hyd00d82xfgw4kjg26tgmab9" id="h_01hyd00d82xfgw4kjg26tgmab9"></a>

In addition to their username and password, it requires your end-users to provide a custom URL.

### Basic with API-Key <a href="#h_01hyd00d82jnkyy85qv0xxkr67" id="h_01hyd00d82jnkyy85qv0xxkr67"></a>

In addition to their username and password, it requires your end-users to provide a custom authorization URL and an API-key.

## Connect one/multiple account(s)

By default, all apps are configured to allow a user to connect one account per app. To allow multiple connected accounts for an app, do the following:

1. Go to Public Apps.
2. Click the configure button for the app.
3. Go to Authentication.
4. Set "Users can connect" to "Multiple accounts".

Note: Once a user has connected multiple accounts for an app, you must include a `connectedAccountID` when you call [`disconnectApp()`](../../apis-and-sdks/js-sdk-reference/#disconnect-an-app), [`showFunctionUI()`](../../apis-and-sdks/js-sdk-reference/#show-the-function-ui) and [`invokeFunction()`](../../apis-and-sdks/js-sdk-reference/#call-a-function). You can call [`getConnectedAccounts()`](../../apis-and-sdks/js-sdk-reference/#get-connected-accounts-of-an-app) to get the list of connected accounts for an app.
