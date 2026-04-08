import React, { useState } from "react";
import API from "../services/api";

function Login() {
  const [form, setForm] = useState({ email:"", password:"" });

  const submit = async (e) => {
    e.preventDefault();
    const res = await API.post("/login", form);

    localStorage.setItem("access", res.data.access_token);
    localStorage.setItem("refresh", res.data.refresh_token);

    alert("Login successful");
  };

  return (
    <form onSubmit={submit}>
      <input placeholder="Email" onChange={(e)=>setForm({...form,email:e.target.value})}/>
      <input type="password" onChange={(e)=>setForm({...form,password:e.target.value})}/>
      <button>Login</button>
    </form>
  );
}

export default Login;
