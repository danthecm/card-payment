import React from "react";
import "./PaymentForm.css";

const PaymentForm = () => {
  return (
    <form className="form">
      <div className="form-control">
        <label>NAME:</label>
        <input className="form-input" type="text" placeholder="e.g John Doe" />
      </div>
      <div className="form-control">
        <label>CARD NUMBER:</label>
        <input
          className="form-input"
          type="number"
          placeholder="e.g 5339 2343 2343 2332"
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
          />
        </div>
      </div>
      <button className="btn-submit">Pay Now</button>
    </form>
  );
};

export default PaymentForm;
