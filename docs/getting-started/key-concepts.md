---
hidden: true
icon: key
---

# Key Concepts

Here are the key concepts that you need to know to use Integry.

## Flow <a href="#h_01hnbfr5vv3pygsg5gddx48qdc" id="h_01hnbfr5vv3pygsg5gddx48qdc"></a>

A **flow** moves data from one app to another. It is comprised of one or more blocks that run and execute steps when triggered. Flows sync data [from another app](../flows/markdown/sync-data-from-another-app-to-your-app.md) to your app, [to another app](../flows/markdown/sync-data-to-another-app-from-your-app.md) from your app, or both. Learn how to [build a flow.](../flows/editor.md) You can also do our [AI Quickstart](https://docs.integry.ai/hc/en-us/articles/28305439384473-AI-Quickstart) as well.

<figure><img src="https://docs.integry.ai/hc/article_attachments/28183793226649" alt=""><figcaption></figcaption></figure>



## Block <a href="#h_01hnbfr93q0v3w0d65rg0mgacj" id="h_01hnbfr93q0v3w0d65rg0mgacj"></a>

A (trigger) **block** is comprised of one trigger and one or more subsequent steps. Each block must have a trigger that will run the block.

<figure><img src="../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

## Trigger <a href="#h_01hnbh26nyfh3rkp2jd3gwwcnp" id="h_01hnbh26nyfh3rkp2jd3gwwcnp"></a>

A **trigger** is an event, a poll, a webhook, or a scheduler that runs a block of an integration of a flow.

## Step <a href="#h_01hnbh34tmjhr6bt4zt1datn1c" id="h_01hnbh34tmjhr6bt4zt1datn1c"></a>

A run executes one or more **steps** in the flow. A step can be a query, an action, a control step, a condition, or execute custom code. Some steps are considered [tasks](key-concepts.md#h_01hnbhz2dst2q97m0pn2en40xj) and are charged.

## Query <a href="#h_01hnbhrzmymy75tjrbm82s9yzg" id="h_01hnbhrzmymy75tjrbm82s9yzg"></a>

A query pulls data from an API endpoint by making one (or more) HTTP call(s). It can be used as a step, or as the source of a dynamic dropdown, custom fields, etc.

## Action <a href="#h_01hnbhs1k1cn1knfzgcx5tqvdj" id="h_01hnbhs1k1cn1knfzgcx5tqvdj"></a>

An action pushes data to an API endpoint by making an HTTP call.

## Setup form <a href="#h_01hnbh34tk0tzxzq6zrwrktvm4" id="h_01hnbh34tk0tzxzq6zrwrktvm4"></a>

The **setup form** of a flow is what a user sees when they are setting up an integration of the flow. It can have one or more pages, and a page can have one or more fields.

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

## Marketplace <a href="#h_01hnbh34tm0bzhbpt0k9p0gnqd" id="h_01hnbh34tm0bzhbpt0k9p0gnqd"></a>

The marketplace is what you [embed in your app](broken-reference) using the SDK so your users can setup integrations. You can control what flows to show by tagging them, and filtering on those tags. The widget emits a number of different [events](../apis-and-sdks/js-sdk-reference/events.md) that you can leverage to control the user journey.

<figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

## Tag <a href="#h_01hnbk5zapq1tyf4ntsgmz8pss" id="h_01hnbk5zapq1tyf4ntsgmz8pss"></a>

A tag is a piece of text you can use to label flows to selectively show them in the [widget](broken-reference).

## User <a href="#h_01hnbk5zapk504515xhby98h3s" id="h_01hnbk5zapk504515xhby98h3s"></a>

A user is a user of your app who will setup integrations with other apps using the Integry widget embedded  within your app. [Learn more...](broken-reference)

## App <a href="#h_01hnbqkn50yx6g99ss7kk8v4ek" id="h_01hnbqkn50yx6g99ss7kk8v4ek"></a>

An app (or "application") is a web application that you can make HTTP calls to, or receive HTTP calls from, in a flow. It could be your application (referred to as "your app") or a third-party application like Mailchimp (referred to as "another app" or "third-party apps"). All calls from Integry to any app are [authenticated](key-concepts.md#h_01hnbqkn504cjnvrj2qb0drkwb).

## Authentication <a href="#h_01hnbqkn504cjnvrj2qb0drkwb" id="h_01hnbqkn504cjnvrj2qb0drkwb"></a>

All HTTP calls made by Integry to any API endpoint are authenticated. If it's a call to _your app_, it will use an API key. If it's a call to _another app_, it will use OAuth 2.0 (if supported -- you can use your own developer app), or another such method.

## Account <a href="#h_01hnbkcnwepqwy0cpan8nxb3gq" id="h_01hnbkcnwepqwy0cpan8nxb3gq"></a>

Before they setup an integration of a flow with an app, users will have to connect to that app to give Integry access to their account in that app. You can allow users to connect and setup integrations with multiple accounts of an app.&#x20;

## Integration <a href="#h_01hnbfrb883b2v83p77esmk0xn" id="h_01hnbfrb883b2v83p77esmk0xn"></a>

An **integration** is an instance of a flow with a third-party app setup by your user using a [account](key-concepts.md#h_01hnbkcnwepqwy0cpan8nxb3gq) of that app. You can allow users to setup one or more integrations of a flow.&#x20;

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

## Run <a href="#h_01hnbfrd7hb30hzw0nc853fcxd" id="h_01hnbfrd7hb30hzw0nc853fcxd"></a>

A block of an integration **runs** when it is triggered by an event, on a schedule, or by a user action, and executes one or more steps in the block.

## Task <a href="#h_01hnbhz2dst2q97m0pn2en40xj" id="h_01hnbhz2dst2q97m0pn2en40xj"></a>

A **task** is a step that executes an HTTP call or runs custom code. If such a step is in a loop, a task will be charged every time that step executes in a run.

## Workspace <a href="#h_01hnjq030nre13cev40r2mxt2y" id="h_01hnjq030nre13cev40r2mxt2y"></a>

A workspace is your organization's private space for building and launching flows and managing integrations created by your users. Organizations with an Enterprise account can create multiple workspaces.&#x20;
