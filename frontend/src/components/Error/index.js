import errorIcon from "../../images/error-icon.png";
import "./Error.css";

const Error = ({ setPageStatus, pageStatus }) => {
  const retryHandler = () => {
    setPageStatus(undefined);
  };
  const errors = pageStatus?.data?.detail;
  return (
    <div className="error-container">
      <img src={errorIcon} alt="check" />
      <h1>Payment Failed</h1>
      {errors.map((error) => (
        <p className="error-message">{error?.msg}</p>
      ))}
      <button onClick={retryHandler} className="retry-btn">
        Try Again
      </button>
    </div>
  );
};

export default Error;
