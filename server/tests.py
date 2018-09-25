import unittest
from api.app import create_app
from utils.currencies import CURRENCIES
import random


class TestRates(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config="testing")
        self.client = self.app.test_client

    def test_get_currencies(self):
        """ Test all currencies rates [GET Request] """
        response = self.client().get('/api/currencies')
        assert response.status_code == 200

    def test_get_currency(self):
        """ Test specific currency rates [GET Request] """
        currency = random.choice(CURRENCIES)[0]

        response = self.client().get(f'/api/currencies/{currency}')

        if currency in ['USD', 'EUR', 'ARS']:
            assert response.status_code == 200
        else:
            assert response.status_code == 404


if __name__ == "__main__":
    unittest.main()
