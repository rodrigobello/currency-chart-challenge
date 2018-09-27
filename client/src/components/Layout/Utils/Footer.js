import React from 'react';
import PropTypes from 'prop-types';

import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';


const styles = theme => ({
  footer: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing.unit,
    position: 'absolute',
    bottom: 0,
    width: '100%',
  },
});


const footer = ({ classes }) => (
  <footer className={classes.footer}>
    <Typography variant="subheading" align="center" color="textPrimary" gutterBottom>
      { `© ${(new Date()).getFullYear()} Currency Chart Challenge` }
    </Typography>
    <Typography variant="caption" align="center" color="textSecondary" component="p">
      <a href="https://github.com/rodrigobello">
        https://github.com/rodrigobello
      </a>
    </Typography>
  </footer>
);

footer.propTypes = {
  classes: PropTypes.shape({
    footer: PropTypes.string,
  }).isRequired,
};

export default withStyles(styles)(footer);
