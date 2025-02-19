---
icon: hammer-brush
---

# Render modes, layouts and styling

The embedded UI can be shown in an in-line container, or popped out in a modal. In addition, it can be shown in a wide or narrow layout.

### `renderMode=IntegryJS.RenderModes.INLINE`

<figure><img src="../.gitbook/assets/image (18).png" alt="" width="375"><figcaption></figcaption></figure>

```javascript
integry.showApps(
  IntegryJS.RenderModes.INLINE,
  "marketplace-container"
).then(() => {
  console.log("Marketplace rendered in-line.");
}).catch((error) => {
  console.error("Error rendering filtered marketplace:", error);
});
```

### `renderMode=IntegryJS.RenderModes.MODAL`

<figure><img src="../.gitbook/assets/image (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

```javascript
integry.showApps(
  IntegryJS.RenderModes.MODAL
).then(() => {
  console.log("Marketplace rendered in-line.");
}).catch((error) => {
  console.error("Error rendering filtered marketplace:", error);
});
```

### `layout=IntegryJS.Layouts.NARROW`

<figure><img src="../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>



```javascript
integry.showApps(
  IntegryJS.RenderModes.MODAL,
  "",
  IntegryJS.Layouts.NARROW
).then(() => {
  console.log("Marketplace rendered in-line.");
}).catch((error) => {
  console.error("Error rendering filtered marketplace:", error);
});
```

The SDK comes with some default styles which can be overridden on demand to customize different parts of the UI.

We use BEM naming to style internal components and scope the default CSS to the container used to instantiate that template via a dynamically generated class. This allows independent styling of different integration views using their respective container IDs.

### Using custom fonts <a href="#h_01j9q2xqdfnmk2py1h9x6stwqf" id="h_01j9q2xqdfnmk2py1h9x6stwqf"></a>

The views respect the `font-family` attribute and the font stack is set to the following generic one by default:

```javascript
#x-integry-container {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica,
    Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';
}
```

To update the font, override the `font-family` attribute.

### Customizing CSS <a href="#h_01j9q2j9hsh2v9zhxffty75bsf" id="h_01j9q2j9hsh2v9zhxffty75bsf"></a>

You can use this approach to override individual items with higher specificity. By specifying the ID of the container used to configure the SDK along with a custom class name, styles can be overridden for containers, controls and components.

```javascript
#my-integry-container .an_available_class {
  /* This will override styles */
}
```
