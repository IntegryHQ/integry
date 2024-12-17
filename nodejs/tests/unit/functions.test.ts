import integry from "@integry/server-sdk";

const appKey = "<YOUR-INTEGRY-APP-KEY>";
const appSecret = "YOUR-INTEGRY-APP-SECRET";
const userId = "<YOUR-USER-ID>";

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

  it("should fetch a specific function", async () => {
    const functionName = "slack-post-message";
    const functionSpec = await sdk.functions.get(functionName, {
      userId: userId,
    });
    expect(functionSpec).toBeDefined();
    expect(functionSpec).toBeInstanceOf(Object);
    expect(functionSpec).toHaveProperty("name");
    expect(functionSpec).toHaveProperty("description");
    expect(functionSpec).toHaveProperty("parameters");
  });

  it("should predict a function based on the passed prompt", async () => {
    const prompt = "Post a message to slack";
    const prediction = await sdk.functions.predict({
      userId: userId,
      prompt: prompt,
    });
    expect(prediction).toBeDefined();
    expect(prediction).toBeInstanceOf(Object);
    expect(prediction).toHaveProperty("functions");
    expect(prediction.functions).toBeInstanceOf(Array);
    expect(prediction.functions.length).toBeGreaterThan(0);
    expect(prediction.functions[0]).toHaveProperty("name");
    expect(prediction.functions[0]).toHaveProperty("description");
    expect(prediction.functions[0]).toHaveProperty("parameters");
  }, 10000);

  it("should call a function", async () => {
    const functionName = "slack-post-message";
    const connected_account_id = "<YOUR-SLACK-ACCOUNT-ID>";
    const params = {
      channel: "{channel}",
      text: "Hello, world from {name}!",
    };
    const variables = {
      channel: "test_slack",
      name: "Integry",
    };
    const response = await sdk.functions.call(functionName, {
      userId: userId,
      connected_account_id: connected_account_id,
      params: params,
      variables: variables,
    });
    expect(response).toBeDefined();
    expect(response).toBeInstanceOf(Object);
    expect(response).toHaveProperty("network_code");
    expect(response.network_code).toBe("200");
  });

  // Add more tests
});
