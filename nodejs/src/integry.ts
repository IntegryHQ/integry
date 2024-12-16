import { ApiClient } from "./api/client";
import {Functions} from "./services/functions";
import { Apps } from "./services/apps";

import { generateHash } from "./utils";

interface IntegrySDKOptions {
  appKey: string;
  appSecret: string;
}

class integry {
  private appKey: string;
  private appSecret: string;
  public client: any;
  public functions: Functions;
  public apps: Apps;

  constructor({ appKey, appSecret }: IntegrySDKOptions) {
    if (!appKey || !appSecret)
      throw new Error("App key and app sercret are required");
    this.appKey = appKey;
    this.appSecret = appSecret;
    this.functions = new Functions(this);
    this.apps = new Apps(this);
    this.client = new ApiClient();
  }

  public getHeaders(userId: string) {
    const hash = generateHash(userId, this.appSecret);
    return {
      app_key: this.appKey,
      user_id: userId,
      hash,
    };
  }

}

export default integry;
