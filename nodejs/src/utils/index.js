import crypto from "crypto";
export const generateHash = (value, secret) => {
    const hash = crypto
      .createHmac("sha256", secret)
      .update(value)
      .digest("hex");

    return hash;
}
