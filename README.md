# Currency Chart Challenge

The challenge consisted in plotting a line chart for the BRL exchange rate to USD, ARS and EUR currencies, in the last seven days.

## Backend

The challenge specified a third-party API to collect the exchange rates. I chose then to develop a REST API that keep the latest quotes stored for each currency and consequently avoid repeatable requests.

### Getting Started

To install and run the server application, [go to server instructions](https://github.com/rodrigobello/currency-chart-challenge/blob/master/server/README.md).

## Frontend

To build the frontend application, I chose React and used the highcharts library to plot the chart (as the challenge had specified). The app fetches the backend data and passes to the highchart component to exchange rate chart.

### Getting Started

To install and run the client application, [go to client instructions](https://github.com/rodrigobello/currency-chart-challenge/blob/master/client/README.md).
