import React, {useEffect, useState} from 'react';
import {useParams} from "react-router-dom";
import "../style.css"
const AppShow = ({apps}) => {
    const [currentApp, setCurrentApp] = useState(null);
    const {appId} = useParams()
    let id = parseInt(appId, 10);
    useEffect(()=>{
        if (!isNaN(id) && id){
        const a = apps?.find(app => app.id === id)
         setCurrentApp(a)
    }
    }, [id])
    return (
            <div className="app">
                <div className="myimg"><img width="400" height="400" src={currentApp?.poster} alt="..."/></div>
                <div className="contents">
                    <div><h1>{currentApp?.name}</h1></div>
                    <div>{currentApp?.description}   </div>
                    <div>date: {currentApp?.created_at} </div>
                    <div>installers: {currentApp?.installers} </div>
                    <div>app size: {currentApp?.size} MB</div>
                </div>
            </div>
    );
};

export default AppShow;
