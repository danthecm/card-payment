import { useState } from "react";
import "./App.css";
import Success from "./components/Success";
import Error from "./components/Error";
import PaymentForm from "./components/PaymentForm";

function App() {
  const [pageStatus, setPageStatus] = useState();
  return (
    <main className="main">
      <div className="container">
        {pageStatus?.message === "success" ? (
          <Success />
        ) : pageStatus?.message === "error" ? (
          <Error />
        ) : (
          <>
            <h1>Your Payment Details</h1>
            <PaymentForm setPageStatus={setPageStatus} />
          </>
        )}
      </div>
    </main>
  );
}

export default App;
