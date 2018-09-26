import React from 'react';
import PropTypes from 'prop-types';

import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';


const styles = theme => ({
  footer: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing.unit * 6,
  },
});


const footer = ({ classes }) => (
  <footer className={classes.footer}>
    <Typography variant="title" align="center" gutterBottom>
        Footer
    </Typography>
    <Typography variant="subheading" align="center" color="textSecondary" component="p">
        Something here to give the footer a purpose!
    </Typography>
  </footer>
);

footer.propTypes = {
  classes: PropTypes.node.isRequired,
};

export default withStyles(styles)(footer);
