import React from 'react';
import ReactDOM from 'react-dom'
import $ from 'jquery'
import { isBrowser } from '@sketchpixy/rubix';
import './main.css';
import { Button } from '@sketchpixy/rubix';

class App extends React.Component {



    render() {
        return (

            <div className="row">
                <span>Lobby Components will go here....</span>
            </div>

        )
    }
}

App.propTypes = {
    socket: React.PropTypes.string
};






















// renders out the base component
function render_component(){
    ReactDOM.render(
        <App />,
        document.getElementById('root')
    );
}


render_component()
