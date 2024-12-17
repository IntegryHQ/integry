import integry from "../../dist/integry";

const appKey = "<YOUR-INTEGRY-APP-KEY>";
const appSecret = "YOUR-INTEGRY-APP-SECRET";
const userId = "<YOUR-USER-ID>";

describe("IntegrySDK", () => {
  const sdk = new integry({
    appKey: appKey,
    appSecret: appSecret,
  });

  it("should fetch list of all apps", async () => {
    const apps = await sdk.apps.list({
      user_id: userId,
    });
    expect(apps).toBeDefined();
    expect(apps).toHaveProperty("apps");
    expect(apps.apps).toBeInstanceOf(Array);
    expect(apps.apps.length).toBeGreaterThan(0);
    expect(apps.apps[0]).toHaveProperty("id");
    expect(apps.apps[0]).toHaveProperty("name");
    expect(apps.apps[0]).toHaveProperty("title");
    expect(apps.apps[0]).toHaveProperty("icon_url");
    expect(apps.apps[0]).toHaveProperty("docs_url");
    expect(apps.apps[0]).toHaveProperty("login_url");
    expect(apps.apps[0]).toHaveProperty("allow_multiple_connected_accounts");
    expect(apps.apps[0]).toHaveProperty("connected_accounts");
    expect(apps.apps[0].connected_accounts).toBeInstanceOf(Array);
  });

  it("should fetch a specific app", async () => {
    const appName = "slack";
    const appDetails = await sdk.apps.get(appName, {
      user_id: userId,
    });
    expect(appDetails).toBeDefined();
    expect(appDetails).toBeInstanceOf(Object);
    expect(appDetails).toHaveProperty("id");
    expect(appDetails).toHaveProperty("name");
    expect(appDetails).toHaveProperty("title");
    expect(appDetails).toHaveProperty("icon_url");
    expect(appDetails).toHaveProperty("docs_url");
    expect(appDetails).toHaveProperty("login_url");
    expect(appDetails).toHaveProperty("allow_multiple_connected_accounts");
    expect(appDetails).toHaveProperty("connected_accounts");
    expect(appDetails.connected_accounts).toBeInstanceOf(Array);
  });

  // Add more tests
});
