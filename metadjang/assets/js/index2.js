//import React from 'react';
import ReactDOM from 'react-dom';
//import App from './App';
//import './index.css';
import React from 'react';
//import logo from './logo.svg';

//import './App.css';
//import './main.css';
import { Button } from '@sketchpixy/rubix';
class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
          <p>
		  Adding some Rubix related code:
		</p>
		<div>
		  <div><Button bsStyle='green'>Green Button!</Button></div>
		  <div><Button bsStyle='red'>Red Button!</Button></div>
		  <div><Button bsStyle='blue' outlined>Blue Button!</Button></div>
		</div>
      </div>
    );
  }
}
ReactDOM.render(
  <App />,
  document.getElementById('root')
);
