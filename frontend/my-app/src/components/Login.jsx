import React, {useState} from 'react';
import {loginAPI} from "../API/Auth";
import {useNavigate} from "react-router-dom";

const Login = ({setUser, setIsAuth}) => {
    const navigate = useNavigate();
    const [username, setUserName] = useState("");
    const [password, setPassword] = useState("");
    const loginned = () => {
        loginAPI(username, password).then(r => {
            if (r) {
                setUser({
                    id: r?.id,
                    username: r?.username,
                    email: r?.email,
                    isAdmin: r?.is_superuser,
                })
                setIsAuth(true)
                navigate("/profile")
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
                           <input type="text" placeholder="username" className="form-control" value={username} onChange={(e) => setUserName(e.target.value)}/>
                        </div>
                         <div className="form-group">
                            <label>Password</label>
                             <input value={password} type="password" className="form-control" placeholder="Password" onChange={(e) => setPassword(e.target.value)}/>
                        </div>

                            <button className="btn btn-primary mt-2" onClick={loginned}>Submit</button>
                    </div>
                </div>
            </div>
        </center>
    );
};

export default Login;