import integry from "../integry";

interface FunctionsGetOptions {
  userId: string;
  include?: string;
  prompt?: string;
  variables?: object;
}

interface FunctionsListOptions {
  userId: string;
  app?: string;
  type?: string;
  _cursor?: string;
  connected_only?: boolean;
  include?: string;
}

interface FunctionPredictOptions {
  userId: string;
  prompt?: string;
  predict_arguments?: boolean;
  include?: string;
  variables?: object;
}

interface FunctionCallOptions {
  userId: string;
  params: object;
  connected_account_id?: string;
  variables?: object;
}

export class Functions {
  private integry: integry;

  constructor(integry: integry) {
    this.integry = integry;
  }

  /**
   * Get the specification for a specific function by its name.
   * @param functionName The name of the function to retrieve.
   * @param options The options for fetching the function.
   */
  async get(
    functionName: string,
    options: FunctionsGetOptions = { userId: "" }
  ) {
    const { userId, prompt, variables, ...queryParams } = options;
    const response = await this.integry.client.makeRequest({
      method: "POST",
      url: `/functions/${functionName}/get`,
      headers: this.integry.getHeaders(userId),
      params: queryParams,
      data: { prompt: prompt, _variables: variables },
    });
    return response.data;
  }

  /**
   * Get specifications for all functions, with optional pagination handling.
   * @param options - The options for fetching the functions.
   * @param iterable - If true, returns the raw response with pagination data; otherwise, returns an iterable of functions.
   */
  async list(options: FunctionsListOptions = { userId: "" }, iterable = false) {
    const { userId, ...queryParams } = options;
    let cursor = "";
    const allFunctions: any[] = [];

    // Loop until all pages are retrieved
    do {
      // Add the cursor to the query parameters if present
      if (cursor) {
        queryParams._cursor = cursor;
      }

      // Make the request to fetch the data
      const response = await this.integry.client.makeRequest({
        method: "POST",
        url: "/functions/list",
        headers: this.integry.getHeaders(userId),
        params: queryParams,
      });

      // If returning the raw response, break the loop and return the entire response
      if (!iterable) {
        return response.data; // Return the raw response directly
      }

      // Add functions to the allFunctions array for iteration
      allFunctions.push(...response.data.functions);

      // Get the cursor for the next page, or null if no more pages
      cursor = response.data._cursor || null;
    } while (cursor); // Continue fetching if there's a next page

    // Return all functions if pagination is handled automatically
    return allFunctions;
  }

  /**
   * Find the most relevant function based on a prompt.
   * @param options The options for predicting the function.
   * @returns The most relevant function for the prompt.
   */
  async predict(options: FunctionPredictOptions = { userId: "" }) {
    const { userId, prompt, variables, ...queryParams } = options;
    const response = await this.integry.client.makeRequest({
      method: "POST",
      url: "/functions/predict",
      headers: this.integry.getHeaders(userId),
      params: queryParams,
      data: { prompt: prompt, _variables: variables },
    });
    return response.data;
  }

  /**
   * Execute a function by its name.
   * @param functionName The name of the function to execute.
   * @param options The options for executing the function.
   */
  async call(
    functionName: string,
    options: FunctionCallOptions = { userId: "", params: {} }
  ) {
    const { userId, params, variables, ...queryParams } = options;
    const response = await this.integry.client.makeRequest({
      method: "POST",
      url: `/functions/${functionName}/call`,
      headers: this.integry.getHeaders(userId),
      params: queryParams,
      data: { ...params, _variables: variables },
    });
    return response.data;
  }
}
