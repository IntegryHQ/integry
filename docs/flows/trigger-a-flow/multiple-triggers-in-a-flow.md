# Multiple Triggers in a Flow

A flow can have more than one trigger. Each trigger will have it's own set of steps that will execute when that trigger fires.

For example, this flow will trigger when a contact is created in Hubspot, look it up in Acme, and create a contact in Acme (if it's not found) or update the contact in Acme (if it's found).

For example, this flow will trigger when a contact is added to a list in Hubspot, or a contact is updated in a list in Hubspot. In the latter case, the contact ID in Acme will be looked up, and then the contact will be updated.

<figure><img src="../../.gitbook/assets/image (9) (1).png" alt=""><figcaption></figcaption></figure>

All triggers in a flow share a common setup form (so your users don't have to answer the same questions twice).
