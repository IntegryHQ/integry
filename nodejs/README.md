# integry

Server-side SDK for Integry APIs.

## Installation

```bash
npm install integry
```

## Usage

```bash
const integry = require('integry');

const sdk = new integry({ appKey: 'YOUR_INTEGRY_APP_KEY', appSecret: 'YOUR_INTEGRY_APP_SECRET' });
const functions = await sdk.functions.list({
    user_id: 'YOUR APPS USER ID'
});
console.log(functions);
```

## Run tests

```bash
npm install --save-dev jest ts-jest @types/jest typescript
npx ts-jest config:init
npx jest
```
