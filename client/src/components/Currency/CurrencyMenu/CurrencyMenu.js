import React from 'react';
import PropTypes from 'prop-types';

import Button from '../../UI/Button/Button';

const currencies = ['Dollar', 'Euro', 'Peso'];

const menu = ({ selectedCurrency, onClick }) => currencies.map(
  currency => (
    <Button
      key={currency}
      onClick={() => onClick(currency)}
      active={selectedCurrency === currency}
    >
      { currency }
    </Button>
  ),
);

menu.propTypes = {
  selectedCurrency: PropTypes.string,
  onClick: PropTypes.func.isRequired,
};

export default menu;
