import React from 'react';
import PropTypes from 'prop-types';


const chart = ({ selectedCurrency, rates }) => (
  <div className="chart">
    <p>{`${selectedCurrency.name} Chart`}</p>
    {rates.map(rate => <p key={rate.quote}>{rate.date}</p>)}
  </div>
);

chart.propTypes = {
  selectedCurrency: PropTypes.shape({
    name: PropTypes.string,
    id: PropTypes.string,
  }).isRequired,
  rates: PropTypes.arrayOf(
    PropTypes.shape({
      date: PropTypes.string,
      quote: PropTypes.number,
    }),
  ).isRequired,
};

export default chart;
