---
hidden: true
icon: comment-question
---

# Flow FAQs

**What can I do to avoid 429 errors?**

To avoid the issue of exceeding rate limits, we use 'throttling', which is sending requests to APIs according to their rate limits. If we apply throttling, we can avoid slow performance and denial of service attacks. You can define throttling at the application level and API level.&#x20;

**Is there a specific way integrations get handled in Integry?**

Each integration gets a separate queue in Integry which is used to execute all of its jobs so that the processing rate of other integrations is not affected. When one job is being executed, the rest of them wait in the queue.&#x20;

**What happens when a 429 is received?**

When a 429 error code is received, we check whether the Retry-After header is also present in the response. If it is present, we throttle the queue of that specific integration by the value of the header e.g. 5 min.  This means that the requests waiting on the queue of this specific integration are not sent out for execution for 5 min. If the Retry-After header doesn’t appear, the queue is throttled for 1 min. If the 429 error still appears after 1 min, we keep throttling the queue based on powers of 2 i.e. 2 min, 4 min, 8 min, 16 min up until 30 min.

**What happens if the error keeps appearing even after 30 minutes?**

If the error continues to appear after 30 min, we keep retrying after every 30 mins. If the queue remains throttled for 36 hours continuously, we flush all the messages that are older than 36 hours.

**What happens if the 429 error code is not received after throttling?**

When a message from the throttled queue is processed, and it doesn’t face a 429 error, the queue for that particular integration is resumed at a normal processing rate immediately.&#x20;

This implementation is done across the board for all users and integrations no matter what pricing package you are on.
