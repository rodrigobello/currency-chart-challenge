import React from 'react';
import PropTypes from 'prop-types';

import ReactHighcharts from 'react-highcharts';

const chart = ({ selectedCurrency, rates }) => {
  const config = {
    title: {
      text: null,
    },
    yAxis: {
      title: {
        text: null,
      },
    },
    xAxis: {
      categories: [],
    },
    series: [{
      name: `${selectedCurrency.id} to BRL`,
      data: [],
    }],
  };

  rates.forEach((rate) => {
    config.xAxis.categories.push(rate.date);
    config.series[0].data.push(rate.quote);
  });

  return (
    <div className="chart">
      <ReactHighcharts config={config} />
    </div>
  );
};

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
