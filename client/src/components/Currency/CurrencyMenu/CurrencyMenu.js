import React from 'react';
import PropTypes from 'prop-types';

import Button from '../../UI/Button/Button';

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

const menu = ({ selectedCurrency, onClick }) => currencies.map(
  currency => (
    <Button
      key={currency.id}
      value={currency.id}
      onClick={() => onClick(currency)}
      active={selectedCurrency === currency.name}
    >
      { currency.name }
    </Button>
  ),
);

menu.propTypes = {
  selectedCurrency: PropTypes.PropTypes.shape({
    name: PropTypes.string,
    id: PropTypes.string,
  }),
  onClick: PropTypes.func.isRequired,
};

export default menu;
