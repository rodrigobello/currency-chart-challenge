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


Home.propTypes = {
  classes: PropTypes.node.isRequired,
};

export default withStyles(styles)(Home);
