import integry from "../integry";

interface AppGetOptions {
  userId: string;
}

interface AppsListOptions {
  userId: string;
  _cursor?: string;
  connected_only?: boolean;
}

export class Apps {
  private integry: integry;

  constructor(integry: integry) {
    this.integry = integry;
  }

  /**
   * Get the details of an individual app by passing appName as a path variable.
   * @param appName The name of the app to retrieve.
   * @param options The options for fetching the app.
   */
  async get(appName: string, options: AppGetOptions = { userId: "" }) {
    const { userId, ...queryParams } = options;
    const response = await this.integry.client.makeRequest({
      method: "POST",
      url: `/apps/${appName}/get`,
      headers: this.integry.getHeaders(userId),
      params: queryParams,
    });
    return response.data;
  }

  /**
   * List all apps available in Integry.
   * @param options - The options for fetching the apps.
   * @param iterable - If true, returns the raw response with pagination data; otherwise, returns an iterable of apps.
   */
  async list(options: AppsListOptions = { userId: "" }, iterable = false) {
    const { userId, ...queryParams } = options;
    let cursor = "";
    const allApps: any[] = [];

    // Loop until all pages are retrieved
    do {
      // Add the cursor to the query parameters if present
      if (cursor) {
        queryParams._cursor = cursor;
      }

      // Make the request to fetch the data
      const response = await this.integry.client.makeRequest({
        method: "POST",
        url: "/apps/list",
        headers: this.integry.getHeaders(userId),
        params: queryParams,
      });

      // If returning the raw response, break the loop and return the entire response
      if (!iterable) {
        return response.data; // Return the raw response directly
      }

      // Add apps to the allApps array for iteration
      allApps.push(...response.data.functions);

      // Get the cursor for the next page, or null if no more pages
      cursor = response.data._cursor || null;
    } while (cursor); // Continue fetching if there's a next page

    // Return all apps if pagination is handled automatically
    return allApps;
  }
}
