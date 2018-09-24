import React, { Component } from 'react';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedCurrency: '',
      quotes: [],
    };

    this.onClick = this.onClick.bind(this);
  }

  onClick(currency) {
    this.setState({ selectedCurrency: currency });
  }

  render() {
    return (
      <div className="container">
        <h1>BRMED Challenge</h1>
      </div>
    );
  }
}

export default Home;
