import React from 'react';
import PropTypes from 'prop-types';

import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

import ReactMarkdown from 'react-markdown';

const info = `
This challenge consisted in plotting a line chart with the **BRL** exchange rate, in the last seven days, to **USD**, **ARS** and **EUR**.

[Source code here](https://github.com/rodrigobello/currency-chart-challenge)
`;

const about = ({
  aboutOpen,
  aboutCloseHandler,
  aboutOpenHandler,
}) => (
  <React.Fragment>
    <Button
      size="small"
      onClick={aboutOpenHandler}
    >
      About
    </Button>
    <Dialog
      open={aboutOpen}
      onClose={aboutCloseHandler}
      scroll="paper"
      aria-labelledby="scroll-dialog-title"
    >
      <DialogTitle id="scroll-dialog-title">Currency Chart Challenge</DialogTitle>
      <DialogContent>
        <DialogContentText>
          <ReactMarkdown source={info} />
        </DialogContentText>
      </DialogContent>
    </Dialog>
  </React.Fragment>
);

about.propTypes = {
  aboutOpenHandler: PropTypes.func.isRequired,
  aboutCloseHandler: PropTypes.func.isRequired,
  aboutOpen: PropTypes.bool.isRequired,
};

export default about;
