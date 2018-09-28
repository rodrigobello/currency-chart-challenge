import React from 'react';
import PropTypes from 'prop-types';
import CircularProgress from '@material-ui/core/CircularProgress';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import grey from '@material-ui/core/colors/grey';

import { withStyles } from '@material-ui/core/styles';

import CurrencyChart from '../../CurrencyChart/CurrencyChart';


const styles = theme => ({
  chart: {
    ...theme.mixins.gutters(),
    paddingTop: theme.spacing.unit * 8,
    paddingBottom: theme.spacing.unit * 2,
    textAlign: 'center',
  },
  error: {
    ...theme.mixins.gutters(),
    padding: theme.spacing.unit * 4,
    width: '500px',
    margin: '0 auto',
  },
  loading: {
    margin: '0 auto',
    textAlign: 'center',
  },
});


const main = ({
  classes,
  selectedCurrency,
  rates,
  query,
}) => {
  switch (query) {
    default:
      return null;
    case 'success':
      return (
        <Paper className={classes.chart} elevation={1}>
          <CurrencyChart selectedCurrency={selectedCurrency} rates={rates} />
        </Paper>
      );
    case 'progress':
      return (
        <div className={classes.loading}>
          <CircularProgress style={{ color: grey[800] }} size={80} />
        </div>
      );
    case 'error':
      return (
        <Paper className={classes.error} elevation={1}>
          <Typography variant="headline" component="h3">
            Oops, an error occurred while trying to connect to server
          </Typography>
          <Typography component="p">
            Please wait before trying again or, if you prefer, feel free to report it.
            To access the repository, click on the icon in the upper right corner.
          </Typography>
        </Paper>
      );
  }
};

main.propTypes = {
  classes: PropTypes.shape({
    chart: PropTypes.string,
    error: PropTypes.string,
    loading: PropTypes.string,
  }).isRequired,
  selectedCurrency: PropTypes.PropTypes.shape({
    name: PropTypes.string,
    id: PropTypes.string,
  }),
  rates: PropTypes.arrayOf(
    PropTypes.shape({
      date: PropTypes.string,
      quote: PropTypes.number,
    }),
  ).isRequired,
  query: PropTypes.string.isRequired,
};

main.defaultProps = {
  selectedCurrency: {},
};


export default withStyles(styles)(main);
