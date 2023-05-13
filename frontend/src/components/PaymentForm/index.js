import React from "react";
import "./PaymentForm.css";

const PaymentForm = () => {
  return (
    <form className="form">
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
          type="number"
          placeholder="e.g 5339 2343 2343 2332"
          required
        />
      </div>
      <div className="form-group">
        <div className="form-control">
          <label>EXPIRY DATE:</label>
          <input name="expiryDate" className="form-input" type="month" />
        </div>
        <div className="form-control">
          <label>CVV:</label>
          <input
            name="CVV"
            className="form-input cvv"
            type="number"
            placeholder="****"
            required
          />
        </div>
      </div>
      <button className="btn-submit">Pay Now</button>
    </form>
  );
};

export default PaymentForm;
