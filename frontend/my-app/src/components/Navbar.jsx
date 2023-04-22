import React from 'react';
import {Link, useNavigate} from "react-router-dom";
import {logoutAPI} from "../API/Auth";

const Navbar = ({isAuth, cats, setUser, setIsAuth}) => {
    const navigate = useNavigate()
    const logout = () => {
        logoutAPI().then(
            setUser(null),
            setIsAuth(false),
            navigate('login')
        )

    }
    return (<nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <span className="navbar-brand">Navbar</span>
        <button className="navbar-toggler" type="button" data-toggle="collapse"
                data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav mr-auto">
                <li className="nav-item active">
                    <Link to={'/apps'} className="nav-link">All Apps <span className="sr-only"></span></Link>
                </li>
                <li className="nav-item">
                    <span className="nav-link">Top Apps</span>
                </li>
                <li className="nav-item dropdown">
                        <span className="nav-link dropdown-toggle" id="navbarDropdown" role="button"
                              data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            categories
                        </span>
                    <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                        {cats?.map(cat => <Link to={`cat_apps/${cat.id}`} key={cat.name}
                                                className="dropdown-item">{cat.name}</Link>)}

                    </div>
                </li>
                {!isAuth
                    ? (<>
                        <li className="nav-item">
                            <Link to={'/register'} className="nav-link">Register</Link>
                        </li>
                        <li className="nav-item">
                            <Link to={'/login'} className="nav-link">Login</Link>
                        </li>
                    </>)
                    : (<>
                        <li className="nav-item">
                            <Link to={'/profile'} className="nav-link">Profile</Link>
                        </li>
                        <li className="nav-item">
                            <span onClick={logout} className="nav-link">Logout</span>
                        </li>
                    </>)
                }

            </ul>
        </div>
    </nav>);
};

export default Navbar;