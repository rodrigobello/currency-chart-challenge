import React from 'react';
import PropTypes from 'prop-types';

import Typography from '@material-ui/core/Typography';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import Button from '@material-ui/core/Button';
import Tooltip from '@material-ui/core/Tooltip';

import CssBaseline from '@material-ui/core/CssBaseline';
import { withStyles } from '@material-ui/core/styles';

import GitHubIcon from '../../UI/Icons/GitHubIcon';


const styles = theme => ({
  toolbarMain: {
    borderBottom: `1px solid ${theme.palette.grey[300]}`,
  },
  toolbarTitle: {
    flex: 1,
  },
});

const appBar = ({ classes }) => (
  <React.Fragment>
    <CssBaseline />
    <Toolbar className={classes.toolbarMain}>
      <Button size="small">About</Button>
      <Typography
        variant="headline"
        color="inherit"
        align="center"
        noWrap
        className={classes.toolbarTitle}
      >
      Currency Chart Challenge
      </Typography>
      <Tooltip title="GitHub Repository">
        <IconButton
          aria-label="GitHub Repository"
          href="https://github.com/rodrigobello/currency-chart-challenge"
        >
          <GitHubIcon />
        </IconButton>
      </Tooltip>

    </Toolbar>
  </React.Fragment>
);

appBar.propTypes = {
  classes: PropTypes.node.isRequired,
};

export default withStyles(styles)(appBar);
