import React from 'react';
import PropTypes from 'prop-types';

import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import { withStyles } from '@material-ui/core/styles';


const styles = theme => ({
  heroUnit: {
    backgroundColor: theme.palette.grey,
  },
  heroContent: {
    maxWidth: 600,
    margin: '0 auto',
    padding: `${theme.spacing.unit * 8}px 0 ${theme.spacing.unit * 6}px`,
  },
  heroButtons: {
    marginTop: theme.spacing.unit * 4,
  },
});

const currencies = [
  {
    id: 'USD',
    name: 'US Dollar',
  },
  {
    id: 'EUR',
    name: 'Euro',
  },
  {
    id: 'ARS',
    name: 'Argentine Peso',
  },
];

const heroUnit = ({ classes, selectedCurrency, onClick }) => (
  <React.Fragment>
    <div className={classes.heroUnit}>
      <div className={classes.heroContent}>
        <Typography variant="display3" align="center" color="textPrimary" gutterBottom>
            BRL Exchange Rate
        </Typography>
        <Typography variant="title" align="center" color="textSecondary" paragraph>
          {
          'Choose one of the currencies below to plot the chart with the Brazilian Real (BRL)'
          + ' quotes in the last 7 days'
          }
        </Typography>
        <div className={classes.heroButtons}>
          <Grid container spacing={16} justify="center">
            {
              currencies.map(currency => (
                <Grid item>
                  <Button
                    variant="contained"
                    key={currency.id}
                    value={currency.id}
                    onClick={() => onClick(currency)}
                    disabled={selectedCurrency.id === currency.id}
                  >
                    { currency.name }
                  </Button>
                </Grid>
              ))
            }
          </Grid>
        </div>
      </div>
    </div>
  </React.Fragment>
);

heroUnit.propTypes = {
  classes: PropTypes.node.isRequired,
  selectedCurrency: PropTypes.PropTypes.shape({
    name: PropTypes.string,
    id: PropTypes.string,
  }),
  onClick: PropTypes.func.isRequired,
};

heroUnit.defaultProps = {
  selectedCurrency: {},
};


export default withStyles(styles)(heroUnit);
