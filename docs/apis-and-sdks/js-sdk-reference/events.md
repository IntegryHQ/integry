---
hidden: true
icon: calendar-circle-exclamation
---

# Events

The SDK emits a number of different events when it loads, a user connects an account, sets up an integration, etc. You can leverage these events to plug in your own logic in the user journey.

_Note: Events emitted by the SDK are scoped to the instance on which the `eventEmitter` object is configured. There is no possiblilty of naming collision with global events, or even with the same event subscribed on multiple SDK instances._

This article lists all the events that can be leveraged, and explains how to subscribe and unsubscribe to/from them.

### Marketplace initialized <a href="#h_01hra2ec7n9rv27g5rhnbyxvmg" id="h_01hra2ec7n9rv27g5rhnbyxvmg"></a>

`eventEmitter.on('ready')`[​](https://sdk.integry.io/docs/core-concepts/events/#eventemitteronready)

Fired when the SDK finishes initialization by authorizing the client. This event is not fired if the credentials provided are incorrect.

```javascript
mySDKInstance.eventEmitter.on('ready', (data) => {

});
```

### Account connected[​](https://sdk.integry.io/docs/core-concepts/events/#authorization) <a href="#h_01hra2epknq3ch3bagkkerdhev" id="h_01hra2epknq3ch3bagkkerdhev"></a>

`eventEmitter.on('did-add-authorization')`[​](https://sdk.integry.io/docs/core-concepts/events/#eventemitterondid-add-authorization)

Fired when an authorization is added successfully in the flow setup form. You can use the `alreadyExists` key to check if a user is adding a previously connected account again.

```javascript
CopymySDKInstance.eventEmitter.on('did-add-authorization', (data) => {
/**
* data:
* identity: string;
* authorizationId: number;
* flowId: number;
* alreadyExists: boolean;
*/
});
```

### Account disconnected <a href="#h_01hra2gyr5e517txdw8atnk9sk" id="h_01hra2gyr5e517txdw8atnk9sk"></a>

`eventEmitter.on('did-remove-authorization')`[​](https://sdk.integry.io/docs/core-concepts/events/#eventemitterondid-remove-authorization)

Fired when an authorization is deleted in the flow setup form.

```javascript
CopymySDKInstance.eventEmitter.on('did-remove-authorization', (data) => {
  /**
   * data:
   *   authorizationId: number;
   */
});
```

### Integration created[​](https://sdk.integry.io/docs/core-concepts/events/#integration-creation) <a href="#h_01hra2h7k3ca6n32jb8treyaye" id="h_01hra2h7k3ca6n32jb8treyaye"></a>

`eventEmitter.on('did-save-integration')`[​](https://sdk.integry.io/docs/core-concepts/events/#eventemitterondid-save-integration)

Fired when an integration is saved successfully. If a user edits an existing integration and saves it, this will fire again.

```javascript
CopymySDKInstance.eventEmitter.on('did-save-integration', (data) => {
  console.log(`Hey, we set up integration ${data.integrationId} successfully!`);
  /**
   * data:
   *   flowId: number;
   *   integrationId: number;
   *   name: string; **Name of the integration**
   *   status: 'ACTIVE' | 'INACTIVE';
   *   callbackUrl: string;
   *   event:  'EDIT' | 'CREATE';
   *   flowName: string;
   *   flowDescription: string;
   *   brandingApp: {
         name: string,
         description: string,
         icon_url: string
       };
   */
});
```

### Integration enabled[​](https://sdk.integry.io/docs/core-concepts/events/#integration-creation) <a href="#id-01hzhcpqjvkftxy077x34x88jv" id="id-01hzhcpqjvkftxy077x34x88jv"></a>

`eventEmitter.on('did-enable-integration')`[​](https://sdk.integry.io/docs/core-concepts/events/#eventemitterondid-save-integration)

Fired when an integration is enabled using the toggle on integrations listing screen.

```javascript
CopymySDKInstance.eventEmitter.on('did-enable-integration', (data) => {
  console.log(`Hey, we enabled integration ${data.integrationId} successfully!`);
  /**
   * data:
   *   integrationId: number;
   *   name: string; **Name of the integration**
   *   status: 'ACTIVE' | 'INACTIVE';
   */
});
```

### Integration disabled[​](https://sdk.integry.io/docs/core-concepts/events/#integration-creation) <a href="#id-01hzhcst84daxtt6dabtyfpqd9" id="id-01hzhcst84daxtt6dabtyfpqd9"></a>

`eventEmitter.on('did-disable-integration')`[​](https://sdk.integry.io/docs/core-concepts/events/#eventemitterondid-save-integration)

Fired when an integration is disabled using the toggle on integrations listing screen.

```javascript
CopymySDKInstance.eventEmitter.on('did-disable-integration', (data) => {
  console.log(`Hey, we disabled integration ${data.integrationId} successfully!`);
  /**
   * data:
   *   integrationId: number;
   *   name: string; **Name of the integration**
   *   status: 'ACTIVE' | 'INACTIVE';
   */
});
```

### Integration renamed[​](https://sdk.integry.io/docs/core-concepts/events/#integration-creation) <a href="#id-01j41hrtgt9t0wd564th7f34cg" id="id-01j41hrtgt9t0wd564th7f34cg"></a>

`eventEmitter.on('did-rename-integration')`[​](https://sdk.integry.io/docs/core-concepts/events/#eventemitterondid-save-integration)

Fired when an integration is renamed.

```javascript
CopymySDKInstance.eventEmitter.on('did-rename-integration', (data) => {
  console.log(`Hey, we renamed integration ${data.integrationId} successfully!`);
  /**
   * data:
   *   integrationId: number;
   *   name: string; **Name of the integration**
   *   status: 'ACTIVE' | 'INACTIVE';
   */
});
```

### Integration deleted <a href="#h_01hra2hd5nmdpmf05yxdh46qah" id="h_01hra2hd5nmdpmf05yxdh46qah"></a>

`eventEmitter.on('did-delete-integration')`[​](https://sdk.integry.io/docs/core-concepts/events/#eventemitterondid-delete-integration)

Fired when an integration is deleted successfully.

```javascript
CopymySDKInstance.eventEmitter.on('did-delete-integration', (data) => {
  console.log(
    `Hey, we deleted integration ${data.integrationId} successfully!`,
  );
  /**
   * data:
   *   flowId: number;
   *   integrationId: number;
   */
});
```

### Subscribe to an event <a href="#subscribing-to-events" id="subscribing-to-events"></a>

Call `eventEmitter.on('<event_name>')` method​ to subscribe to an event.

For example, here's how you would subscribe to the _did-save-integration_ event to get the callback URL you need to run the integration.

```javascript
CopymySDKInstance.eventEmitter.on('did-save-integration', (data) => {
  console.log(`Hey, we set up integration ${data.integrationId} successfully!`);
  /**
   * data:
   *   flowId: number;
   *   integrationId: number;
   *   name: string;
   *   status: string;
   *   callbackUrl: string;
   *   event:  'EDIT' | 'CREATE';
   */
});
```

### Unsu​bscribe from an event <a href="#h_01hfwe5zx4hq9r6zncvsf00qmz" id="h_01hfwe5zx4hq9r6zncvsf00qmz"></a>

Call `eventEmitter.unsub('<event_name>')` method​ to unsubscribe from an event.

Here's an example:

```javascript
Copyfunction integrationSavedCallback(data: CallbackData) {
  console.log(`Integration with name ${data.name} was created!`);
}
// subscribe
mySDKInstance.eventEmitter.on('did-save-integration', integrationSavedCallback);

// unsubscribe
mySDKInstance.eventEmitter.unsub('did-save-integration', integrationSavedCallback);
```

\
