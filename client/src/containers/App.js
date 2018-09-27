/* eslint no-console: ["error", { allow: ["warn", "error"] }] */
import React, { Component } from 'react';
import PropTypes from 'prop-types';

import { withStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';

import { AppBar, HeroUnit, Footer } from '../components/Layout/Layout';

import CurrencyChart from '../components/CurrencyChart/CurrencyChart';

const styles = theme => ({
  layout: {
    width: 'auto',
    marginLeft: theme.spacing.unit * 3,
    marginRight: theme.spacing.unit * 3,
    [theme.breakpoints.up(1100 + theme.spacing.unit * 3 * 2)]: {
      width: 1100,
      marginLeft: 'auto',
      marginRight: 'auto',
    },
  },
});


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      rates: [],
    };
    this.onClick = this.onClick.bind(this);
  }

  onClick(currency) {
    this.setState({ rates: [] }); // Set selected currency and rates to initial state
    this.fetchRates(currency);
  }

  fetchRates(currency) {
    fetch(`http://localhost:5000/api/currencies/${currency.id}?orderby=asc`)
      .then((response) => {
        if (response.status === 200) {
          return response.json();
        }
        throw new Error(response.statusText);
      })
      .then(rates => this.setState({
        rates,
        selectedCurrency: currency,
      }))
      .catch(e => console.error(e));
  }

  render() {
    const { classes } = this.props;
    const { selectedCurrency, rates } = this.state;
    let chart;
    if (selectedCurrency) {
      chart = <CurrencyChart selectedCurrency={selectedCurrency} rates={rates} />;
    }
    return (
      <React.Fragment>
        <CssBaseline />
        <div className={classes.layout}>
          <AppBar />
          <HeroUnit selectedCurrency={selectedCurrency} onClick={this.onClick} />
          { chart }
        </div>
        <Footer />
      </React.Fragment>
    );
  }
}


App.propTypes = {
  classes: PropTypes.shape({
    layout: PropTypes.string,
  }).isRequired,
};

export default withStyles(styles)(App);
