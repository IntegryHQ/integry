import crypto from "crypto";
export const generateHash = (value: string, secret: string) => {
  const hash = crypto.createHmac("sha256", secret).update(value).digest("hex");

  return hash;
};
