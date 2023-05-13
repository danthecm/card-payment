import "./App.css";
import PaymentForm from "./components/PaymentForm";

function App() {
  return (
    <main className="main">
      <div className="container">
        <h1>Your Payment Details</h1>
        <PaymentForm />
      </div>
    </main>
  );
}

export default App;
