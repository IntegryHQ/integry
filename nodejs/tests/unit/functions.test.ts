const IntegrySDK = require("../../src/integry");

describe("IntegrySDK", () => {
  const sdk = new IntegrySDK({
    apiKey: "test_api_key",
    userId: "test_user_id",
  });

  it("should fetch a function spec", async () => {
    const spec = await sdk.getFunctionSpec("test_function_id");
    expect(spec).toBeDefined();
  });

  // Add more tests
});
