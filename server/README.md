# Currency Chart Challenge (Server)

This is the REST API implementation for the challenge solution. It stores the latest quotes for each currency and then avoid repeatable requests.

## Getting Started (Local)

### Requirements

- pip
- postgreSQL

### Installing

Clone the repository and go to server directory

```
git clone https://github.com/rodrigobello/currency-chart-challenge
cd currency-chart-challenge/server/
```

Setup python virtual environment

```
virtualenv venv

source venv/bin/activate
```

Install application dependencies

```
pip install -r requirements.txt
```

Uncomment and replace following examples in the api configuration file (config.py)

```python
# CURRENCY_LAYER_KEY = 'apikey'
# SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost/database_name"
```

## Running application

```
 python run.py
```

## Running unit tests

```
 python api/tests.py
```
