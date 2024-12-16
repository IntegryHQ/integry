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
      return await this.client(config);
    } catch (error: any) {
      throw new Error(JSON.stringify(error.response.data));
    }
  }
}
