import React, { Component } from 'react';

import Chart from '../components/Currency/CurrencyChart/CurrencyChart';
import Menu from '../components/Currency/CurrencyMenu/CurrencyMenu';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      rates: [],
    };

    this.onClick = this.onClick.bind(this);
  }

  onClick(currency) {
    this.setState({ selectedCurrency: currency });
  }

  render() {
    const { selectedCurrency, rates } = this.state;
    let chart;
    if (selectedCurrency) {
      chart = <Chart selectedCurrency={selectedCurrency} rates={rates} />;
    } else {
      chart = <p>Select a currency to plot the chart</p>;
    }
    return (
      <div className="container">
        <h1>BRMED Challenge</h1>
        <Menu selectedCurrency={selectedCurrency} onClick={this.onClick} />
        { chart }
      </div>
    );
  }
}

export default Home;
