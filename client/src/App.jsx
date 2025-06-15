import React from "react";
import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";

import Register from './Pages/Register';
import Login from './Pages/Login';
import Home from './Pages/home'
import PDF from './Pages/pdf';
import NavBar from "./Components/navbar";
import ChatBot from "./Pages/chatbot";


const App = () => {
  const location = useLocation();

  const noNavBarPaths = ['/login','/signup'];



  return (
    <div className="container">
      {!noNavBarPaths.includes(location.pathname) && <NavBar />}
      <Routes>
        <Route exact path="/pdf" element={<PDF />} />
        <Route exact path="/chatbot" element={<ChatBot />} />
        <Route exact path="/login" element={<Login />} />
        <Route exact path="/signup" element={<Register />} />
        <Route exact path="/home" element={<Home />} />
      </Routes>
    </div>
  );
};

// eslint-disable-next-line react-refresh/only-export-components
export default () => (
  <BrowserRouter>
    <App />
  </BrowserRouter>
);