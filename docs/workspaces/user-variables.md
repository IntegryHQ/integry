---
icon: user
---

# User Variables

The user object in Integry is meant to represent your end-users. You can use this object if you need to pass custom user-specific data to a Flow.

#### Defining user variables <a href="#h_01j9p86yek0vxsx0vr7qknvb0r" id="h_01j9p86yek0vxsx0vr7qknvb0r"></a>

By default, the user object has:

* `userID` (Required)
  * Used to associate a user's integrations with their account in your app.
* `apiKey` (Optional)
  * Can be used to authenticate HTTP calls to your app.

If you need to add additional user variables:

1. Go to Workspace Settings -> Variables.
2. Add the variables under User Variables.

#### Accessing user variables in a flow <a href="#h_01j9p7afekr7843j6ez8071004" id="h_01j9p7afekr7843j6ez8071004"></a>

You can reference all user variables in flow steps.

1. In the body section of an HTTP Call step, click Add tag -> User Variables. ![Screenshot 2024-10-08 at 10.09.32 AM.png](https://docs.integry.ai/hc/article_attachments/38606605602585)
2. Select the variable you want to use in the step. The values shown are only to help you map. ![Screenshot 2024-10-08 at 9.58.09 AM.png](https://docs.integry.ai/hc/article_attachments/38606605605785)

Don't worry about the values shown; they're from your test account and will be replaced with your user's values at run-time.

#### Passing user variables with the SDK <a href="#h_01j9p6c77t0kp450wbfjdwwmex" id="h_01j9p6c77t0kp450wbfjdwwmex"></a>

When you [embed the marketplace widget](https://docs.integry.ai/hc/en-us/articles/23189976901529), you pass the variables in the user object.

```
user: {
    userId: "asim@integry.io",
    apiKey: "453546546754", 
}
```

#### Passing additional user variables with the SDK <a href="#h_01j9p69h67s6y8werpmchatkat" id="h_01j9p69h67s6y8werpmchatkat"></a>

The additional variables are also passed in the same user object.

```
user: {
    userId: "asim@integry.io",
    apiKey: "453546546754",
    orgId: "12",
    region: "North America",
}
```

#### FAQs <a href="#id-01j9p8pnmj1n1z5c1cg8j4grsz" id="id-01j9p8pnmj1n1z5c1cg8j4grsz"></a>

**What happens if I pass an empty value for a user variable?**

In order to protect you from accidentally breaking existing integrations (that may be using that user variable's existing value), we don't empty out the value of a user variable when you send an empty string ("").

If you really want to empty it, send a blank space (" ").
