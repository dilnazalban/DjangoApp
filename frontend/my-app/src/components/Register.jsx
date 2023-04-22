import React, {useState} from 'react';
import {registerUser} from "../API/Auth";
import {useNavigate} from "react-router-dom";

const Register = () => {
     const navigate = useNavigate();
    const [username, setUserName] = useState("");
    const [password, setPassword] = useState("");
    const [repeatPassword, setRepeatPassword] = useState("");
    const [email, setEmail] = useState("");
    const register = () => {
        registerUser(username, password, repeatPassword, email).then(r => {
                if (r) {
                    navigate('/login')
                }
            }
        )
    }
    return (
        <center>
            <div className="container">
                <div className="col-lg-4">
                    <div className="mt-5">
                        <div className="form-group">
                            <label>Username</label>
                            <input type="text" placeholder="username" className="form-control" value={username}
                                   onChange={(e) => setUserName(e.target.value)}/>
                        </div>
                        <div className="form-group">
                            <label>Email address</label>
                            <input value={email} onChange={(e) => setEmail(e.target.value)} type="email"
                                   className="form-control" placeholder="email"/>
                        </div>
                        <div className="form-group">
                            <label>Password</label>
                            <input value={password} type="password" className="form-control" placeholder="Password"
                                   onChange={(e) => setPassword(e.target.value)}/>
                        </div>
                        <div className="form-group">
                            <label>Confirm password</label>
                            <input value={repeatPassword} onChange={(e) => setRepeatPassword(e.target.value)}
                                   type="password" className="form-control" placeholder="Confirm Password"/>
                        </div>

                        <button onClick={register} className="btn btn-primary mt-2">Submit</button>
                    </div>
                </div>
            </div>
        </center>);
};


export default Register;