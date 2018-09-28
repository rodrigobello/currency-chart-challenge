/* eslint no-console: ["error", { allow: ["warn", "error"] }] */
import React, { Component } from 'react';
import PropTypes from 'prop-types';

import { withStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';

import {
  AppBar,
  HeroUnit,
  Footer,
  Main,
} from '../components/Layout/Layout';

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
      query: 'idle',
    };
    this.onClick = this.onClick.bind(this);
  }

  onClick(currency) {
    this.setState({
      query: 'progress',
      selectedCurrency: currency,
    });

    this.fetchRates(currency);
  }

  fetchRates(currency) {
    fetch(`https://brl-rate-api.herokuapp.com/api?currency=${currency.id}&orderby=asc&days=7`)
      .then((response) => {
        if (response.status === 200) {
          return response.json();
        }
        throw new Error(response.statusText);
      })
      .then(data => this.setState({
        rates: data.quotes,
        query: 'success',
      }))
      .catch((e) => {
        console.warn(e);
        this.setState({
          query: 'error',
        });
      });
  }

  render() {
    const { classes } = this.props;
    const {
      selectedCurrency,
      rates,
      query,
    } = this.state;
    return (
      <React.Fragment>
        <CssBaseline />
        <div className={classes.layout}>
          <AppBar />
          <HeroUnit selectedCurrency={selectedCurrency} onClick={this.onClick} />
          <Main selectedCurrency={selectedCurrency} rates={rates} query={query} />
        </div>
        <Footer />
      </React.Fragment>
    );
  }
}


App.propTypes = {
  classes: PropTypes.shape({
    layout: PropTypes.string,
    root: PropTypes.string,
  }).isRequired,
};

export default withStyles(styles)(App);
