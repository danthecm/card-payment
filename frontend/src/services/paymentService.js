import axios from "axios";
import { PAYMENT_URL } from "../config/urls";

export const sendPaymentRequest = async (data) => {
  try {
    await axios.post(PAYMENT_URL, data);
    return { message: "success" };
  } catch (error) {
    const response = error?.response;
    const data = response?.data;
    return { message: "error", data };
  }
};
