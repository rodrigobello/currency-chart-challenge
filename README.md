# Currency Chart Challenge

The challenge consisted in plotting a line chart for the BRL exchange rate to USD, ARS and EUR currencies, in the last seven days. Try the solution online at https://currency-chart-challenge.herokuapp.com/

## Getting Started

To install and run the application locally, follow the [server](https://github.com/rodrigobello/currency-chart-challenge/tree/master/server) and [client](https://github.com/rodrigobello/currency-chart-challenge/tree/master/client) instructions.

## Backend

[Live Demo](https://brl-rate-api.herokuapp.com/)

The challenge specified a third-party API to collect the exchange rates. I chose then to develop a REST API that keep the latest quotes stored for each currency and consequently avoid repeatable requests.

## Frontend

[Live Demo](https://currency-chart-challenge.herokuapp.com/)

To build the frontend application, I chose React and used the highcharts library to plot the chart (as the challenge had specified). The app fetches the backend data and passes to the highchart component to exchange rate chart.
