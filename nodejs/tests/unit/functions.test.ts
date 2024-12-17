import integry from "@integry/server-sdk";

const IntegrySDK = require("../../src/integry");
const appKey = "3883c794-9d71-450e-b39d-dfa21ffab006";
const appSecret = "ffd3a8d4-7160-4a44-b603-08848420a108";
const userId = "yasir@integry.io";

describe("IntegrySDK", () => {
  const sdk = new integry({
    appKey: appKey,
    appSecret: appSecret,
  });

  it("should fetch list of all functions", async () => {
    const functions = await sdk.functions.list({
      userId: userId,
      app: "slack",
    });
    expect(functions).toBeDefined();
    expect(functions).toHaveProperty("functions");
    expect(functions.functions).toBeInstanceOf(Array);
    expect(functions.functions.length).toBeGreaterThan(0);
    expect(functions.functions[0]).toHaveProperty("name");
    expect(functions.functions[0]).toHaveProperty("description");
    expect(functions.functions[0]).toHaveProperty("parameters");
  });

  // Add more tests
});
