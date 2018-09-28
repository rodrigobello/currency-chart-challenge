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
  currencyButton: {
    width: '150px',
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
        {
          selectedCurrency.id
            ? (
              <Typography variant="display2" align="center" color="textPrimary" gutterBottom>
                { `${selectedCurrency.id} to BRL Exchange Rate` }
              </Typography>
            )
            : (
              <Typography variant="title" align="center" color="textSecondary" gutterBottom>
                {
                'Choose one of the currencies below to plot the chart with the Brazilian Real (BRL)'
                + ' quotes in the last 7 days'
                }
              </Typography>
            )
        }

        <div className={classes.heroButtons}>
          <Grid container spacing={16} justify="center">
            {
              currencies.map(currency => (
                <Grid item key={currency.id}>
                  <Button
                    className={classes.currencyButton}
                    variant="contained"
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
  classes: PropTypes.shape({
    heroUnit: PropTypes.string,
    heroContent: PropTypes.string,
    heroButtons: PropTypes.string,
    currencyButton: PropTypes.string,
  }).isRequired,
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
