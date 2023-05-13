import checkIcon from "../../images/check-icon.png";
import "./Success.css";

const Success = ({ setPageStatus }) => {
  const newPaymentHandler = () => {
    setPageStatus(undefined);
  };
  return (
    <div className="success-container">
      <img src={checkIcon} alt="check" />
      <h1>Payment Successful</h1>
      <button onClick={newPaymentHandler} className="reset-btn">
        Make another payment
      </button>
    </div>
  );
};

export default Success;
