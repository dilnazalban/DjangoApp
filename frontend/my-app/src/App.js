import Navbar from "./components/Navbar";
import {useEffect, useState} from "react";
import {Route, Routes} from "react-router-dom";
import Login from "./components/Login";
import Register from "./components/Register";
import Profile from "./components/Profile";
import AppList from "./components/AppList";
import AppShow from "./components/AppShow";
import Home from "./components/Home";
import {appList, categoryList} from "./API/App";
import CategoryApps from "./components/CategoryApps";


function App() {
    const [user, setUser] = useState(null)
    const [isAuth, setIsAuth] = useState(false);
    const [cats, setCats] = useState(null)
     const [apps, setApps] = useState(null);
    useEffect(() => {
        categoryList().then(categories => {
            if (categories)
                setCats(categories)
        })
        appList().then(r => {
            if (r) {
                setApps(r)
            }
        })
    }, [])



    return (
        <div className="App">
            <Navbar isAuth={isAuth} cats={cats} setIsAuth={setIsAuth} setUser={setUser}/>
            <Routes>
                <Route element={<Home/>} path={"/"}/>
                <Route element={<Login setUser={setUser} setIsAuth={setIsAuth}/>} path={"/login"}/>
                <Route element={<Register/>} path={"/register"}/>
                <Route element={<Profile user={user}/>} path={"/profile"}/>
                <Route element={<CategoryApps apps={apps}/>} path={"/cat_apps/:catId"}/>
                <Route element={<AppList apps={apps}/>} path={"/apps"}/>
                <Route element={<AppShow apps={apps}/>} path={"/apps/:appId"}/>
            </Routes>
        </div>
    );
}

export default App;
