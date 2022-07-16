
import React, { Component } from "react";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoom from "./CreateRoom";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
            <Router>
                <Routes>
                    <Route exact path="/" /> <p>This is the homepage!</p>
                    <Route exact path="/join" component={RoomJoinPage} />
                    <Route exact path="/create" component={CreateRoom} />
                </Routes>
            </Router>
    );
  }
}

console.log(React.version);




//import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';


