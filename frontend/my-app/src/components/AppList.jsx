import React from 'react';
import {Link} from "react-router-dom";

const AppList = ({apps}) => {
    return (
        <div>
            <div>
                {apps?.map(app => (
                    <div key={app.id} style={{paddingTop: "30px"}}>
                        <Link to={`/apps/${app.id}`}  style={{textDecoration: "none"}}>
                            <center>
                                <div className="card mb-3" style={{maxWidth: "840px" ,backgroundColor: "black"}}>
                                    <div className="row g-0">
                                        <div className="col-md-4">
                                            <img src={app.poster} height="300" width="300" className="img-fluid rounded-start"
                                                 alt="..."/>
                                        </div>
                                        <div className="col-md-8">
                                            <div className="card-body">
                                                <h5 className="card-title">{app.name}</h5>
                                                <p className="card-text">{app.description}</p>
                                                <p className="card-text"><small>{app.created_at}</small>
                                                </p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </center>
                        </Link>
                    </div>)
                )}
            </div>
        </div>
    );
};

export default AppList;