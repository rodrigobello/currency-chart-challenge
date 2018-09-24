import React, { Component } from 'react';

import Chart from '../components/Currency/CurrencyChart/CurrencyChart';
import Menu from '../components/Currency/CurrencyMenu/CurrencyMenu';

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
    const { selectedCurrency, quotes } = this.state;
    return (
      <div className="container">
        <h1>BRMED Challenge</h1>
        <Menu selectedCurrency={selectedCurrency} onClick={this.onClick} />
        <Chart quotations={quotes} />
      </div>
    );
  }
}

export default Home;
