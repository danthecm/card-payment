import { useState } from "react";
import "./PaymentForm.css";
import LoadingSpinner from "../LoadingSpinner";
import { formatDate } from "../../utils/dateHelpers";
import { sendPaymentRequest } from "../../services/paymentService";
import { formatCardNumber, removeSpaces } from "../../utils/cardHelpers";

const PaymentForm = ({ setPageStatus }) => {
  const [isLoading, setIsLoading] = useState(false);

  const cardNumberInputHandler = (event) => {
    const cardNumber = formatCardNumber(event.target.value);
    event.target.value = cardNumber;
  };

  const formSumbitHandler = (e) => {
    e.preventDefault();
    setIsLoading(true);
    const name = e.target.name.value;
    const cardNumber = e.target.cardNumber.value;
    const cleanCardNumber = removeSpaces(cardNumber);
    const expiry_date = e.target.expiryDate.value;
    const formattedDate = formatDate(expiry_date);
    const cvv = e.target.cvv.value;
    const card_details = {
      name,
      card_number: cleanCardNumber,
      expiry_date: formattedDate,
      cvv,
    };
    sendPaymentRequest(card_details).then((result) => {
      setPageStatus(result);
      setIsLoading(false);
    });
  };
  return (
    <form className="form" onSubmit={formSumbitHandler}>
      <div className="form-control">
        <label>NAME:</label>
        <input
          name="name"
          className="form-input"
          type="text"
          placeholder="e.g John Doe"
          required
        />
      </div>
      <div className="form-control">
        <label>CARD NUMBER:</label>
        <input
          name="cardNumber"
          className="form-input"
          type="text"
          placeholder="e.g 5339 2343 2343 2332"
          onInput={cardNumberInputHandler}
          required
        />
      </div>
      <div className="form-group">
        <div className="form-control">
          <label>EXPIRY DATE:</label>
          <input
            name="expiryDate"
            className="form-input"
            type="month"
            required
          />
        </div>
        <div className="form-control">
          <label>CVV:</label>
          <input
            name="cvv"
            className="form-input cvv"
            type="number"
            placeholder="****"
            required
          />
        </div>
      </div>
      <button className="btn-submit" disabled={isLoading}>
        {isLoading ? <LoadingSpinner /> : "Pay Now"}
      </button>
    </form>
  );
};

export default PaymentForm;
