---
icon: calendar-circle-exclamation
---

# Trigger a Flow

## Event in another app

Integry offers 200+ ready-to-use triggers for popular apps. Simply add it, configure it (if needed), and you're good to go.

Some triggers [instantly receive new data](./#h_01hr564dmfajbt87rj45ja14y0) (via webhooks) while others use [polling to get new data](./#h_01hr564fqgbsnm9yz0heqz2efz).

### Instant <a href="#h_01hr564dmfajbt87rj45ja14y0" id="h_01hr564dmfajbt87rj45ja14y0"></a>

Instant triggers use incoming webhooks. Whenever there is new data, the app will call the Integry webhook URL with the event data in the payload.

### Polling <a href="#h_01hr564fqgbsnm9yz0heqz2efz" id="h_01hr564fqgbsnm9yz0heqz2efz"></a>

If the app does not support webhooks for a particular event (eg. Contact Added to a List in HubSpot), a polling trigger can be used. A polling triggers works by:

1. Establishing a baseline of existing data when the integration is setup
2. Checking (or polling) for new data every 5 minutes
3. Running the trigger block in the flow for every new record found

## Webhook <a href="#h_01hrsr5f4rawex3d4bqmrtdjck" id="h_01hrsr5f4rawex3d4bqmrtdjck"></a>

When a particular event occurs in your app, you can trigger a flow by calling a webhook and passing a JSON payload. Let's say, you're building a flow, _When a contact is creating in AcmeSaaS, add a subscriber in Mailchimp list_. Your app will send a JSON payload to Integry when a contact is created in your app. That payload could look like this:

```json
{
    “id”: 123,
    “email”: “john@appleseed.com”,
    “first_name” : “John”,
    “last_name” : “Apple”
}
```

You can also name the payload if you want to pass different sample fields and/or values in the marketplace embed code.

## On schedule <a href="#h_01hrsr5h5zsjegw0y3gpag6dbk" id="h_01hrsr5h5zsjegw0y3gpag6dbk"></a>

A flow can be triggered on a schedule.

## Integration created <a href="#h_01hrsr5khn1b9bcpzvdn55765m" id="h_01hrsr5khn1b9bcpzvdn55765m"></a>

This is useful if you want to want to execute any steps when the integration is setup by your user. For example, you can register the webhook URL by making an HTTP call.

