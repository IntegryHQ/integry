import axios, { AxiosInstance, AxiosRequestConfig, AxiosError } from "axios";

export class ApiClient {
  private client: AxiosInstance | null = null;

  constructor() {
    this.init();
  }
  /**
   * Initialize the Axios client with default configuration.
   */
  init() {
    this.client = axios.create({
      baseURL: "https://api.integry.io/",
    });
  }

  /**
   * Make a request using the Axios client.
   * @param config Axios request configuration.
   */
  async makeRequest(config: AxiosRequestConfig) {
    if (!this.client) {
      throw new Error("API client is not initialized");
    }

    try {
      // Convert headers to query params
      const headers = config.headers || {};
      const url = new URL(config.url || "", "https://api.integry.io");

      for (const [key, value] of Object.entries(headers)) {
        if (typeof value === "string") {
          url.searchParams.append(key, value);
        }
      }

      // Clone config with modified URL
      const modifiedConfig: AxiosRequestConfig = {
        ...config,
        url: url.pathname + url.search, // only path and query
      };

      return await this.client(modifiedConfig);
    } catch (error: any) {
      throw new Error(JSON.stringify(error.response?.data || error.message));
    }
  }
}
