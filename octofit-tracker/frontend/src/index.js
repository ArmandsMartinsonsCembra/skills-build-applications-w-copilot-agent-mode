import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';

// Log the API base URL for debugging
const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
const apiBaseUrl = codespaceName ? `https://${codespaceName}-8000.app.github.dev/api/` : '/api/';
console.log('API Base URL:', apiBaseUrl);
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
